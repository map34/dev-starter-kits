#!/usr/bin/env bash
set -e

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
pushd $SCRIPT_DIR/../
    py.test $PYTHON_PKG_TEST_FOLDER_NAME --cov-report xml:cov.xml --cov $PYTHON_PKG_FOLDER_NAME
popd
