import sys
from typing import Any
import logging
import ftplib
import socket


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
