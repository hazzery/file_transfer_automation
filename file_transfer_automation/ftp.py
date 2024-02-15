from typing import Any
import ftplib


def authenticate(ftp: ftplib.FTP, config: dict[str, Any]):
    ftp.connect(config['hostname'], config['port_number'])
    ftp.login(config['username'], config['password'])
    ftp.cwd(config['working_directory'])


def file_names(ftp: ftplib.FTP):
    return (
        file_name
        for file_name, file_info in ftp.mlsd(facts=['type'])
        if file_info['type'] != 'dir'
    )
