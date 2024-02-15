import logging
import pathlib
import ftplib
import shutil
import os

from .ftp import authenticate, file_names
from .logging_config import configure_logging
from .import_config import import_config


logger = logging.getLogger(__name__)


def main() -> None:
    configure_logging()
    config = import_config()['FTP']

    temp_directory = pathlib.Path('temp')
    internal_network = pathlib.Path('network')
    os.makedirs(temp_directory, exist_ok=True)
    os.makedirs(internal_network, exist_ok=True)

    with ftplib.FTP() as ftp:
        authenticate(ftp, config)
        for file_name in file_names(ftp):
            file_path = temp_directory / file_name
            logger.info('Downloading: %s', file_name)
            with open(file_path, 'wb') as file:
                ftp.retrbinary('RETR ' + file_name, file.write)

            shutil.move(file_path, internal_network)
            logger.info('Moved: %s', file_name)
