install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C predict-fake-news.py main.py local-cli-predict

all: install lint test