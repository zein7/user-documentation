build:
	sphinx-build -aE -b html docs/ _build/html/

serve:
	sphinx-autobuild -aE -b html docs/ docs/_build/html/ -H 0.0.0.0 -p 8080