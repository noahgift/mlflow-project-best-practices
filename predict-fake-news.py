#!/usr/bin/env python

import os
import requests
import pandas as pd

my_data = {
    "text": {"aliens are coming to invade earth"},
}
df = pd.DataFrame(data=my_data)

def create_tf_serving_json(data):
    return {
        "inputs": {name: data[name].tolist() for name in data.keys()}
        if isinstance(data, dict)
        else data.tolist()
    }

def score_model(dataset):
    url = "https://adb-2951765055089996.16.azuredatabricks.net/model/Fake-News/1/invocations"
    headers = {"Authorization": f'Bearer {os.environ.get("DATABRICKS_TOKEN")}'}
    data_json = (
        dataset.to_dict(orient="split")
        if isinstance(dataset, pd.DataFrame)
        else create_tf_serving_json(dataset)
    )
    response = requests.request(method="POST", headers=headers, url=url, json=data_json)
    if response.status_code != 200:
        raise Exception(
            f"Request failed with status {response.status_code}, {response.text}"
        )
    return response.json()


if __name__ == "__main__":
    print(score_model(df))
