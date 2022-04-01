# mlflow-project-best-practices
An example MLFlow project

[![Python application test with Github Actions](https://github.com/noahgift/mlflow-project-best-practices/actions/workflows/main.yml/badge.svg)](https://github.com/noahgift/mlflow-project-best-practices/actions/workflows/main.yml)


## High Level Architecture

![end-to-end-mlops](https://user-images.githubusercontent.com/58792/158695115-a4f8fd97-fbb5-4f9f-b548-ca424636e0ae.png)

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

## Query for Models with API

* [Refer to Quikstart Python](https://docs.databricks.com/applications/mlflow/quick-start-python.html)
* [Refer to Create or Register Model](https://docs.microsoft.com/en-us/azure/databricks/applications/machine-learning/manage-model-lifecycle/#create-or-register-a-model)
* [Access tracking server external](https://docs.databricks.com/applications/mlflow/access-hosted-tracking-server.html)

You need to set the tracking URI.

```bash
export MLFLOW_TRACKING_URI=databricks
```

```python
from pprint import pprint
from mlflow.tracking import MlflowClient
client = MlflowClient()
for rm in client.list_registered_models():
  pprint(dict(rm), indent=4)
```


## Download Model

* [Download model artifacts](https://docs.databricks.com/applications/mlflow/models.html#download-model-artifacts)

CLI version

```
mlflow artifacts download --artifact-uri models:/<name>/<version|stage>
````

To use Python do the following:

```python
from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository

model_uri = MlflowClient.get_model_version_download_uri(model_name, model_version)
ModelsArtifactRepository(model_uri).download_artifacts(artifact_path="")
```


## Register model for AWS Sagemaker

* [Register model for AWS Sagemaker](https://docs.databricks.com/applications/mlflow/scikit-learn-model-deployment-on-sagemaker.html)


![Screen Shot 2022-03-16 at 1 53 31 PM](https://user-images.githubusercontent.com/58792/158655796-06994cd3-c34f-4cbb-aa2b-34dbcb83d9fc.png)

## Goal for today

* Databricks Tensorflow run
* Feature Store
* Model Serving

### Model Serving
https://docs.databricks.com/applications/mlflow/model-serving.html

Run it with `mlserve`

```
 mlflow models serve --model-uri  /workspaces/mlflow-project-best-practices/tf-model
 ```
 
 ## References
 
 * [Watch Youtube Walkthrough](https://studio.youtube.com/video/PUXhWZQW8BI/edit?c=UCNDfiL0D1LUeKWAkRE1xO5Q)
 * [Watch Walkthrough on O'Reilly](https://learning.oreilly.com/videos/mlops-platforms-from/032232022VIDEOPAIML/)
 
 
