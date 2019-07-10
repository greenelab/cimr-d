
"""Reading and parsing through the contributor's yaml file.
(c) YoSon Park

This is the default uploading skim for bulk files using zenodo. 
For PR-based file uploader, check .circleci/deploy.sh and
.circleci/process_submitted_data.py
"""

import sys
import yaml
import pandas
import pathlib
import logging
import subprocess


CONFIG_FILE_EXTENSION = ('yml', 'yaml')


def check_yaml_via_git():
    """A git-status-dependent function used when locally applying 
    parse_yaml.py. It searches for a new or modified yml/yaml file and 
    returns its pathlib path.
    """
    status_check = 'git status --porcelain'
    jobsplit = subprocess.check_output(
        status_check,
        stderr=subprocess.STDOUT,
        shell=True,
        universal_newlines=True
    ).replace('\n', '').split('?? ')
    for job in jobsplit:
        if job.endswith(CONFIG_FILE_EXTENSION):
            yaml_file = pathlib.Path('.cimr-d/' + job.split('/')[-1])
    return(yaml_file)


def load_yaml(yaml_file):
    """Read the found yaml file and return the read object."""
    with open(yaml_file, 'r') as args:
        try:
            return(yaml.safe_load(args))
        except yaml.YAMLError as exc:
            logging.error(f' {exc}')
            sys.exit(0)


def verify_weblink(path):
    import urllib
    weburl = urllib.request.urlopen(path)
    if weburl.getcode() == 200:
        return True
    else:
        return False


def download_file(path, outdir='./'):
    """Download file based on the provided link.
    Progress bar added based on the following reference:
    https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests/37573701
    """
    from tqdm import tqdm
    import requests
    import math
    r = requests.get(path, stream=True)
    total_size = int(r.headers.get('content-length', 0));
    block_size = 1024
    wrote = 0
    file_name = path.split('/')[-1]
    file_path = outdir + file_name
    with open(file_path, 'wb') as f:
        for data in tqdm(r.iter_content(block_size), 
                         total=math.ceil(total_size//block_size), 
                         unit='KB', 
                         leave=True,
                         ncols=42,
                         unit_scale=True,
                         unit_divisor=1024):
            wrote = wrote + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        logging.error(f' check the file link and try again.')


class Yamler:
    """A collection of utilities to parse the yaml file, check metadata
    and trigger cimr processing of the contributed file
    """

    def __init__(self, yaml_data):
        self.yaml_data = yaml_data
        self.data_type = None
        self.keys = None


    def key_picking(self):
        """List keys for the dictionarized yaml data and store in self.
        The following keys are expected:
        ['defined_as', 'data_file', 'contributor', 'data_info', 'method']
        """
        self.keys = self.yaml_data.keys()


    def get_data_type(self):
        """One of the following data_type variables are expected:
        ['gwas', 'twas', 'eqtl', 'sqtl', 'pqtl', 'tad']
        """
        if self.yaml_data['data_info']['data'] is not None:
            self.data_type = self.yaml_data['data_info']['data_type']
        else:
            logging.error(f' there is no data_type indicated.')
            sys.exit(0)


    def download(self):
        """Check if provided weblink to the file exists. 
        Download if verified.
        """
        path = self.yaml_data['data_file']['location']['url']
        outdir = 'submitted_data/' + self.data_type + '/'
        if verify_weblink(path):
            logging.info(f' starting download')
            download_file(path, outdir)
        else:
            logging.error(f' file unavailable')


    def single_upload(self):
        print('single upload parser')


    def bulk_upload(self):
        print('bulk upload parser')


    def check_defined(self):
        """whether the submitted data is a single file or not"""
        if self.yaml_data['defined_as'] == 'upload':
            self.single_upload()
        elif self.yaml_data['defined_as'] == 'upload_bulk':
            self.bulk_upload()
        else:
            logging.error(f' accepted \'defined_as\' variables are \'upload\' and \'upload_bulk\'.')
            sys.exit(0)


    def parse_metadata(self):
        pass


    def fill_missing_metadata(self):
        pass


    def extend_metadata(self):
        """fill metadata/${data_type}.txt file with parsed yaml"""
        self.get_data_type()
        self.metadata_file = 'metadata/'+str(self.data_type)
        try:
            with open(self.metadata_file, 'a') as metafile:
                self.parse_metadata()
                metadata = self.fill_missing_metadata()
                metafile.write(metadata)
        except:
            pass

            
    def check_data_file(self):
        ARGS = ['doc', 'location']
        pass


yaml_file = check_yaml_via_git()

try:
    yaml_file_path = yaml_file.resolve(strict=True)
    logging.info(f' processing metadata {yaml_file_path} for data upload.')
    print(' processing metadata %s for data upload.' % (yaml_file_path))
    yaml_data = load_yaml(yaml_file)
    print(yaml_data)
    y = Yamler(yaml_data)
    y.check_defined()
    y.download_file()
except FileNotFoundError:
    logging.info(f' no new yml file found to process data.')
    print(' no new yml file found to process data.')
    sys.exit(0)

