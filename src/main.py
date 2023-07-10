import os
import sys
from threading import Event
from rclone_python import rclone
from scheduler import TimeScheduler, DailyTask
from dotenv import load_dotenv
import logging
from rich.logging import RichHandler


def upload():
    rclone.sync("data", REMOTE_EXPORT_PATH)


if __name__ == "__main__":
    # setup logger
    log = logging.getLogger("rich")
    FORMAT = "%(message)s"
    logging.basicConfig(
        level="INFO",
        format=FORMAT,
        datefmt="[%X]",
        handlers=[
            RichHandler(
                rich_tracebacks=True,
            )
        ],
    )

    # load ENV-variables
    load_dotenv()
    BACKUP_ON_START = os.getenv("BACKUP_ON_START") or False
    REMOTE_EXPORT_PATH = os.getenv("REMOTE_EXPORT_PATH")
    if REMOTE_EXPORT_PATH is None:
        log.error("The env variable REMOTE_EXPORT_PATH is not set.")
        sys.exit()
    UPLOAD_TIMES = os.getenv("UPLOAD_SCHEDULE") or "00:00"
    UPLOAD_TIMES = UPLOAD_TIMES.split()

    # setup the scheduler
    ts = TimeScheduler()
    for schedule in UPLOAD_TIMES:
        ts.add(DailyTask(schedule, upload))
        log.info(f"Scheduling daily uploads @ {schedule}")

    if BACKUP_ON_START:
        log.info('Starting backup right away as "BACKUP_ON_START" is set.')
        upload()

    # start the scheduler
    ts.start()

    # wait until manually stopped
    Event().wait()
