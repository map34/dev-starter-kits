#!/usr/bin/env bash
set -e

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
pushd $SCRIPT_DIR/../
    mvn jacoco:prepare-agent test jacoco:report
    mv target/site/jacoco/jacoco.xml cov.xml
popd
