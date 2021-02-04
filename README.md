# BackOffice_SolEng
Projeto do processo seletivo para as vagas de Back Office e de Solution Engineer na Raccoon Marketing Digital

## Requirements:
> import json

> import operator

> import re

> import requests

> from requests.exceptions import HTTPError, RequestException, Timeout

> from xml.etree.ElementTree import fromstring

## How to run script:
> python main.py

Observation: If you want to test the POST request locally, implement a separate simple Flask server, like this one:
>from flask import Flask, request
app = Flask(\_\_name\_\_)
@app.route('/', methods=\['POST'])
def result():
    content = request.get_json()
    print(content)
    return "success"
