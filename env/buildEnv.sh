#!/usr/bin/env bash

ENV_PATH=$(readlink -f $(dirname "$0"))
TEMPLATE_PATH="$ENV_PATH/templates"

function initTaskDir {
    for TASK_NAME in "$@"
    do
        mkdir "$TASK_NAME"
        cp "$TEMPLATE_PATH/taskSolver.py" "$TASK_NAME/$TASK_NAME.py"
    done
}

cat << EOF
CodeJam environment:
    [*] initTaskDir <TASK_NAME_0>...
EOF
