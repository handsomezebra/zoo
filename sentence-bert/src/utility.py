# -*- coding: utf-8 -*-

import yaml
import os
import logging
import logging.config

config = None


def override_string(config_obj, name):
    value = os.getenv(name.upper(), None)
    if value is not None:
        config_obj[name] = value


def override_int(config_obj, name):
    value = os.getenv(name.upper(), None)
    if value is not None:
        config_obj[name] = int(value)


def override_float(config_obj, name):
    value = os.getenv(name.upper(), None)
    if value is not None:
        config_obj[name] = float(value)


def load_config(config_file_path='src/config.yml'):
    global config
    if config is None:
        value = os.getenv('CONFIG', None)
        if value:
            config_file_path = value

        with open(config_file_path, 'rt') as f:
            config = yaml.safe_load(f)

        # define configs that can be overridden by the environment variables
        # note that config names are lower case but corresponding environment variables are all in uppercase
        for k, v in config.items():
            if type(v) is str:
                override_string(config, k)
            elif type(v) is int:
                override_int(config, k)
            elif type(v) is float:
                override_float(config, k)

    return config


def setup_logging(log_config_file_path=None):
    if log_config_file_path is None:
        log_config_file_path = "src/logging.yml"

    with open(log_config_file_path, 'rt') as f:
        log_config = yaml.load(f)

    log_file = os.getenv('LOG_FILE', None)
    if log_file:
        log_config['handlers']['file_handler']['filename'] = log_file

    console_log_level = os.getenv('CONSOLE_LOG_LEVEL', None)
    if console_log_level:
        log_config['handlers']['console']['level'] = console_log_level

    file_log_level = os.getenv('FILE_LOG_LEVEL', None)
    if file_log_level:
        log_config['handlers']['file_handler']['level'] = file_log_level

    logging.config.dictConfig(log_config)
