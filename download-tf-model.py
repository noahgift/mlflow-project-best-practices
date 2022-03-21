from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("86e829a82162463a8300a301864df036", path="model")
print(f"Placed model in: {my_model}")
