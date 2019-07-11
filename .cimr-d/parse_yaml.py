
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
COMPRESSION_EXTENSION = ('gz')
BULK_EXTENSION = ('tgz')
FILE_EXTENSION = ('txt', 'tsv')

logging.basicConfig(level='INFO')


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
    """Verify the provided link to the contributed file."""
    import urllib

    weburl = urllib.request.urlopen(path)

    if weburl.getcode() == 200:
        return True
    else:
        return False


def download_file(path, outdir='./'):
    """Download data based on the provided link.

    Note;
    Progress bars added based on the following reference:
    https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests/37573701
    """
    from tqdm import tqdm
    import requests
    import math
    
    r = requests.get(path, stream=True)
    total_size = int(r.headers.get('content-length', 0))
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


def validate_hash(path, hash):
    """Validate a file against an MD5 hash value."""
    import hashlib

    md5 = hashlib.md5()
    
    with open(path, 'rb') as f:
        while True:
            chunk = f.read(10000000)
            if not chunk:
                break
            md5.update(chunk)
    
    return md5.hexdigest() == hash


class Yamler:
    """A collection of utilities to parse the yaml file, check metadata
    and trigger cimr processing of the contributed file
    """

    def __init__(self, yaml_data):
        self.yaml_data = yaml_data
        self.data_type = None
        self.keys = None
        self.hash = None
        self.outdir = None
        self.downloaded_file = None


    def pick_keys(self):
        """List keys for the dictionarized yaml data and store in self.
        The following keys are expected:
        ['defined_as', 'data_file', 'contributor', 'data_info', 'method']
        """
        self.keys = self.yaml_data.keys()


    def get_data_type(self):
        """One of the following data_type variables are expected:
        ['gwas', 'twas', 'eqtl', 'sqtl', 'pqtl', 'tad']
        """
        if self.yaml_data['data_info']['data_type'] is not None:
            self.data_type = self.yaml_data['data_info']['data_type']
        else:
            logging.error(f' there is no data_type indicated.')
            sys.exit(0)


    def download(self):
        """Check if provided weblink to the file exists. 
        Download if verified.
        """
        path = self.yaml_data['data_file']['location']['url']
        self.downloaded_file = path.split('/')[-1]
        outdir_root = 'submitted_data/'
        pathlib.Path(outdir_root).mkdir(exist_ok=True)
        self.outdir = outdir_root + str(self.data_type) + '/'
        pathlib.Path(self.outdir).mkdir(exist_ok=True)

        if verify_weblink(path):
            logging.info(f' starting download')
            download_file(path, self.outdir)
            self.hash = self.yaml_data['data_file']['location']['md5']
        else:
            logging.error(f' file unavailable')
            sys.exit(0)


    def bulk_download(self):
        """Bulk download option assumes one of the following file types:
        ['tar.gz', 'tgz']
        """
        import tarfile

        self.download()

        if tarfile.is_tarfile(self.downloaded_file):
            tarred_data = tarfile.open(
                self.downloaded_file, 
                mode='r:*'
            )
            tarred_data.extractall(path=self.outdir)
    

    def check_hash(self):
        """Compare md5 of the downloaded file to the provided value"""
        if validate_hash(self.downloaded_file, self.hash):
            logging.info(f' data is ready for cimr processing.')
            return True
        else:
            logging.error(f' provided md5 hash didn\'t match the downloaded file.')
            return False


    def check_defined(self):
        import os

        """Check whether the submitted data is a single file"""
        if self.yaml_data['defined_as'] == 'upload':
            self.download()
            self.check_hash()
        elif self.yaml_data['defined_as'] == 'upload_bulk':
            self.bulk_download()
            if self.check_hash():
                os.remove(self.outdir + self.downloaded_file)
        else:
            logging.error(f' accepted \'defined_as\' variables are \'upload\' and \'upload_bulk\'.')
            sys.exit(0)


    def check_data_file(self):
        """Standard set of Yamler functions to check information on the
        contributed data file for ci cimr processing.
        """
        self.get_data_type()
        self.check_defined()


if __name__ == '__main__':

    if len(sys.argv) == 1:
        yaml_file = check_yaml_via_git()
    else:
        yaml_file = pathlib.Path(sys.argv[1])

    try:
        yaml_file_path = yaml_file.resolve(strict=True)
        logging.info(f' processing metadata {yaml_file_path}.')
        yaml_data = load_yaml(yaml_file)
        print(yaml_data)
        y = Yamler(yaml_data)
        y.check_data_file()
    except FileNotFoundError:
        logging.info(f' no new yaml file found to process.')
        sys.exit(0)

