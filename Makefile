init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run Practica/practica.py
	coverage report -m
