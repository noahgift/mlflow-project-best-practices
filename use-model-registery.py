import mlflow
import pandas as pd

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model('model')

#create payload
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
data = pd.DataFrame(data=my_data)
result = loaded_model.predict(pd.DataFrame(data))
print(result)