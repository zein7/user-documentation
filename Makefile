all:
	./scripts/prepare_server.sh
	./scripts/start_server.sh
	# - SELENIUM_DRIVER="selenium.webdriver.Chrome" tox -e docs-strict
	tox -e docs-strict
	tox -e docs-text-index
	cp -r docs/_build/text/* docs/_build/html/_sources
