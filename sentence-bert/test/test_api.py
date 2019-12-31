# -*- coding: utf-8 -*-

import json
import requests
import logging
import csv

url = "http://localhost:10000/predict"


def get_result(text_list):

    response = None

    data = {"text_list": text_list}

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.warning("Service %s requests exception: %s", url, e)

    if response is None:
        logging.warning("Failed to call service")
        return None
    elif response.status_code != 200:
        logging.warning("Invalid response code %d from service", response.status_code)
        return None
    else:
        return response.json()


def test_basic():

    result = get_result(["hello world!", "thank you"] * 1024)

    assert len(result) == 2048 and len(result[0]) == 1024 and len(result[1]) == 1024
