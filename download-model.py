from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("68baff0203344dfebe89a6c73c6d6cfe", path="model")
print(f"Placed model in: {my_model}")



