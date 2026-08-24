"""
Common utility scripts
"""

import os
import yaml

this_dir = os.path.realpath(os.path.dirname(__file__)) + "/"
config_path = os.path.join(this_dir, "config.yaml")


def load_config() -> dict:
    with open(config_path, "r", encoding="utf-8") as stream:
        loaded = yaml.load(stream, Loader=yaml.Loader)

    return dict(loaded or {})


def reload_config() -> dict:
    global config

    config = load_config()
    return config


config: dict = load_config()


def stringify_hour(hour: int) -> str:

    hour = int(hour)
    return f"H0{hour}" if hour<10 else f"H{hour}"


def stringify_day(day: int) -> str:

    day = int(day)
    return f"D00{day}" if day<10 else f"D0{day}" if day<100 else f"D{day}"


def destringify_day(day: str) -> str:

    return int(day[1:])


def index_to_season(idx: int):

    day = index_to_day(idx)

    if config['days_per_period'] == 1: return stringify_day(day)
    elif config['days_per_period'] > 1:
        day_2 = day + config['days_per_period'] - 1

        return f"{stringify_day(day)}-{stringify_day(day_2)}"


def index_to_day(idx: int):

    d = idx * config['days_per_period'] - config['day_to_index']
    return d