# Shell to use with Make
SHELL := /bin/bash

# Set important Paths
PROJECT := commis
LOCALPATH := $(CURDIR)/$(PROJECT)
PYTHONPATH := $(LOCALPATH)/

# Export targets not associated with files
.PHONY: test coverage pip clean build deploy

# Clean build files
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	find . -name "__pycache__" -print0 | xargs -0 rm -rf
	-rm -rf htmlcov
	-rm -rf .coverage
	-rm -rf build
	-rm -rf dist
	-rm -rf $(PROJECT).egg-info

# Targets for commis testing
test:
	nosetests -v --with-coverage --cover-package=$(PROJECT) --cover-inclusive --cover-erase tests

# Build the universal wheel and source distribution
build:
	python setup.py sdist bdist_wheel

# Deploy to PyPI
deploy:
	python setup.py register
	twine upload dist/*
