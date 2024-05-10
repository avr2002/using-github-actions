#!/usr/bin/bash

EXIT_STATUS=0

black --config .black.toml . || ((EXIT_STATUS++))
pylint --rcfile .pylintrc *.py ./type-hints/ || ((EXIT_STATUS++))
flake8 --config .flake8 . || ((EXIT_STATUS++))
mypy . --exclude .venv || ((EXIT_STATUS++))
ruff check . --config ruff.toml --fix || ((EXIT_STATUS++))
isort . --settings .isort.cfg || ((EXIT_STATUS++))

echo Exiting with status $EXIT_STATUS
exit $EXIT_STATUS
