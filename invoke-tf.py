import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import mlflow
import mlflow.keras
import mlflow.tensorflow
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from mlflow.models.signature import infer_signature

cal_housing = fetch_california_housing()
# grab a bit of data to test with
X_train, X_test, y_train, y_test = train_test_split(cal_housing.data,
                                                    cal_housing.target,
                                                    test_size=0.0005)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X_test)
print(f"Shape of test set: {X_test.shape}")

## Predict by loading model from disk
keras_model = mlflow.keras.load_model(f"tf-model")
keras_pred = keras_model.predict(X_test)
print(keras_pred)

#describe signature
signature = infer_signature(X_test, keras_pred)
print(signature)



