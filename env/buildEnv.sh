#!/usr/bin/env bash

ENV_PATH='/home/saca/workplace/algo/py/codejam/env'
TEMPLATE_PATH="$ENV_PATH/templates"

function initTaskDir {
    TASK_NAME=${1:?buildTaskDir <TASK_NAME>}

    mkdir "$TASK_NAME"
    cd "$TASK_NAME"
    cp "$TEMPLATE_PATH/taskSolver.py" "$TASK_NAME.py"
    chmod u+x "$TASK_NAME.py"
}

cat << EOF
CodeJam environment:
    [*] initTaskDir <TASK_NAME>
EOF
