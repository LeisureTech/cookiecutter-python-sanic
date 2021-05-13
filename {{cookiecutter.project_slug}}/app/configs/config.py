import configparser
import os
import logging


def get_config() -> configparser.ConfigParser:
    logger = logging.getLogger(__name__)
    environment = os.getenv("ENV", "dev")
    logger.info(f"We are running in the {environment} environment")

    read_file = __config_filename(environment)
    config = configparser.ConfigParser()
    config.read(read_file)
    logger.info(f"Reading config from file {read_file}")

    print(config)
    return config


def __config_filename(env: str) -> str:
    return f"config_{env}"
