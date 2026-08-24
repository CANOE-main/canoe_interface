"""
Handles logging globally
"""

import os
import sys
import logging

from datetime import datetime
from logging.handlers import RotatingFileHandler

from directories import LOG_DIR


def setup_logging(name: str = "canoe_app") -> logging.Logger:
    """
    Creates or returns a logger with consistent configuration.

    Args:
        name: The logger name (defaults to "canoe_app")

    Returns:
        A configured logger instance
    """

    logger = logging.getLogger(name)

    # Only add handlers if none exist
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Build logfile name with current datetime
        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        log_file = os.path.join(
            LOG_DIR,
            f"canoe_app_{timestamp}.log"
        )

        # File handler
        fh = RotatingFileHandler(
            log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=3,
            encoding="utf-8",
        )

        fh.setLevel(logging.DEBUG)

        fh_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(name)s "
            "%(module)s:%(lineno)d - %(message)s"
        )

        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)

        # Console handler
        #
        # PyInstaller console=False sets sys.stderr to None
        # on Windows, so only create this handler when a
        # console stream actually exists.
        if sys.stderr is not None:
            ch = logging.StreamHandler(sys.stderr)
            ch.setLevel(logging.INFO)

            ch_formatter = logging.Formatter(
                "%(asctime)s %(levelname)s - %(message)s",
                "%H:%M:%S",
            )

            ch.setFormatter(ch_formatter)
            logger.addHandler(ch)

        # Avoid duplicate logs
        logger.propagate = False

    return logger