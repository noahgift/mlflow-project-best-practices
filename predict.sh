#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "story":"Aliens have landed on earth"
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict/