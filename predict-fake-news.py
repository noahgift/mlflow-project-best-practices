#!/usr/bin/env python

import os
import requests
import pandas as pd

my_data = {
    "author": {0: "bigjim.com"},
    "published": {0: "2016-10-27T18:05:26.351+03:00"},
    "title": {0: "aliens are coming to invade earth"},
    "text": {0: "aliens are coming to invade earth"},
    "language": {0: "english"},
    "site_url": {0: "cnn.com"},
    "main_img_url": {
        0: "https://2.bp.blogspot.com/-0mdp0nZiwMI/UYwYvexmW2I/AAAAAAAAVQM/7C_X5WRE_mQ/w1200-h630-p-nu/Edison-Stock-Ticker.jpg"
    },
    "type": {0: "bs"},
    "title_without_stopwords": {0: "aliens are coming to invade earth"},
    "text_without_stopwords": {0: "aliens are coming to invade earth"},
    "hasImage": {0: 1.0},
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