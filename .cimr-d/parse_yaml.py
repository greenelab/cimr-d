

import sys
import yaml
import pathlib
import logging
import subprocess


CONFIG_FILE_EXTENSION = ('yml', 'yaml')


def check_config_file():
    status_check = 'git status --porcelain'

    jobsplit = subprocess.check_output(
        status_check,
        stderr=subprocess.STDOUT,
        shell=True,
        universal_newlines=True
    ).replace('\n', '').split('?? ')

    for job in jobsplit:
        if job.endswith(CONFIG_FILE_EXTENSION):
            config_file = pathlib.Path('.cimr-d/' + job.split('/')[-1])

    return(config_file)


def parse_yaml(config_file):
    with open(config_file, 'r') as config:
        try:
            deposit = yaml.safe_load(config)
            return(deposit)

        except yaml.YAMLError as exc:
            logging.error(f' {exc}')
            sys.exit(0)


config_file = check_config_file()

try:
    config_file_path = config_file.resolve(strict=True)
    logging.info(f' processing metadata {config_file_path} for data upload.')
    print(' processing metadata %s for data upload.' % (config_file_path))
    deposit = parse_yaml(config_file)
    print(deposit)

except FileNotFoundError:
    logging.info(f' no new yml file found to process data.')
    print(' no new yml file found to process data.')
    sys.exit(0)

