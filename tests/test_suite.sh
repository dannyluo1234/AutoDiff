#!/bin/bash 
pip install pytest-cov # make sure pytest-cov is installed
pip install ../. #make sure that creative name is installed

pytest cs107_creativename_tests/tests.py


pytest --cov=cs107_creativename cs107_creativename_tests/tests.py --cov-report term-missing
