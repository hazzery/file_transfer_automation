from typing import Any
import logging
import ftplib
import socket
import shutil
import sys
import os


logger = logging.getLogger(__name__)


def authenticate(ftp: ftplib.FTP, config: dict[str, Any]):
    try:
        ftp.connect(config['hostname'], config['port_number'])
        ftp.login(config['username'], config['password'])
        ftp.cwd(config['working_directory'])
    except (socket.gaierror, ConnectionRefusedError) as error:
        logger.error(error)
        sys.exit('Failure to connect to FTP server')
    except ftplib.error_perm as error:
        logger.error(error)
        sys.exit(f'Failed to cd into {config["working_directory"]}')


def file_names(ftp: ftplib.FTP):
    return (
        file_name
        for file_name, file_info in ftp.mlsd(facts=['type'])
        if file_info['type'] != 'dir'
    )


def download_directory(
        config: dict[str, Any],
        destination: os.PathLike
) -> None:
    temp_directory = 'temp'
    os.makedirs(temp_directory, exist_ok=True)

    with ftplib.FTP() as ftp:
        authenticate(ftp, config)
        for file_name in file_names(ftp):
            file_path = f'{temp_directory}/file_name'
            logger.info('Downloading: %s', file_name)
            with open(file_path, 'wb') as file:
                ftp.retrbinary('RETR ' + file_name, file.write)

            shutil.move(file_path, destination)
            logger.info('Moved: %s', file_name)

    os.rmdir(temp_directory)

