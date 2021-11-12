set -e
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
py.test SCRIPT_DIR/../tests/ --cov-report xml:SCRIPT_DIR/../cov.xml --cov package
