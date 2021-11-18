#!/bin/bash 
pip install pytest-cov # make sure pytest-cov is installed

pytest tests.py

pytest --cov=src tests.py --cov-report term-missing
