# -*- coding: utf-8 -*-

import json
import requests
import logging
import csv

url = "http://localhost:10000/parse"


def get_result(text, lang, dims, latent=None, reftime=None, tz=None):
    data = {
        "text": text,
        "lang": lang,
        "dims": json.dumps(dims)
    }

    if reftime is not None:
        data["reftime"] = reftime

    if tz is not None:
        data["tz"] = tz

    if latent is not None:
        data["latent"] = latent

    response = None

    try:
        response = requests.post(url, data=data)
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


def test_time_en():

    reftime = "1559920354000"  # 6/7/2019 8:12:34 AM
    time_zone = "America/Los_Angeles"

    result = get_result("tomorrow at eight", "en", ["time"], reftime=reftime)

    assert result is not None and result[0]["value"]["value"] == "2019-06-08T08:00:00.000-07:00"
