
# Check out the docs for this input: 
# https://docs.databricks.com/applications/mlflow/model-serving.html 

curl http://127.0.0.1:5000/invocations -H 'Content-Type: application/json' -d '{
          "inputs": [[ 0.0575371, 0.50570342, -0.09188722, -0.07555557, 0.03215254, 0.15547057, -0.74992243,0.80336201]]
     }'
