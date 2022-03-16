# mlflow-project-best-practices
An example MLFlow project

[![Python application test with Github Actions](https://github.com/noahgift/mlflow-project-best-practices/actions/workflows/main.yml/badge.svg)](https://github.com/noahgift/mlflow-project-best-practices/actions/workflows/main.yml)

You can Notebook see the Databricks code here:  https://github.com/FourthBrain/databricks-zero-to-mlops/blob/main/src/week2-mlflow/AutoML/XGBoost-fake-news-automl.py

## Example in Azure CloudShell
![Screen Shot 2022-03-12 at 6 40 00 PM](https://user-images.githubusercontent.com/58792/158038852-4bd3c5c0-5a41-491d-9cdb-a19587766b75.png)

## Example in Github Codespaces
![Screen Shot 2022-03-12 at 7 11 31 PM](https://user-images.githubusercontent.com/58792/158039417-e6510971-240c-45d2-984f-cd8ab88a1569.png)

### Curl Example
```
curl \
  -u token:$DATABRICKS_TOKEN \
  -X POST \
  -H "Content-Type: application/json; format=pandas-records" \
  -d@data.json \
  https://adb-2951765055089996.16.azuredatabricks.net/model/Fake-News/1/invocations
```


## Deploy Architecture

![IMG_0217](https://user-images.githubusercontent.com/58792/158256886-a0ae8edb-9c69-4ada-b4ca-17a796af6ed7.jpg)

## Query registered model

* [Azure Databricks Model Serving Architecture](https://docs.microsoft.com/en-us/azure/databricks/applications/mlflow/model-serving)

## Query with Databricks CLI

* [Databricks CLI](https://docs.databricks.com/dev-tools/cli/index.html)

1. Create a databricks config:
`touch ~/.databrickscfg`
2.  Put in host and token
3.  Query jobs

`databricks jobs list --output JSON | jq`
4.  List clusters

`databricks clusters list --output JSON | jq `

5.  List contents of DBFS

`databricks fs ls dbfs:/`

