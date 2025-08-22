#!/usr/bin/env bash

if [ -f .env ]; then
    set -o allexport
    source .env
    set +o allexport
fi

python3 -m build && python3 -m twine check dist/* && python3 -m twine upload -u __token__ -p "$PYPI_TOKEN" dist/*