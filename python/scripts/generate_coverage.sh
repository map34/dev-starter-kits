set -e
SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"
py.test $SCRIPT_DIR/../tests/ --cov-report xml:$SCRIPT_DIR/../cov.xml --cov package
