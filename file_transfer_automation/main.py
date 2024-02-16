import functools
import datetime
import logging
import pathlib
import os

from .task_scheduler import schedule_daily_task
from .logging_config import configure_logging
from .import_config import import_config
from .ftp import download_directory


logger = logging.getLogger(__name__)


def main() -> None:
    configure_logging()
    config = import_config()

    internal_network = pathlib.Path('network')
    os.makedirs(internal_network, exist_ok=True)

    task = functools.partial(download_directory, config['FTP'], internal_network)
    schedule_time: datetime.time = config["schedule_time"]
    schedule_daily_task(task, schedule_time.hour, schedule_time.minute)
