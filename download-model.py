from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("51c0348482e042ea8e4b7983ab6bff99", path="model")
print(f"Placed model in: {my_model}")


#ModelsArtifactRepository(model_uri).download_artifacts(artifact_path="model")
