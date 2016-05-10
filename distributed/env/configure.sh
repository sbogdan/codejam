#!/usr/bin/env bash

ENV_PATH=$(readlink -f $(dirname "$0"))
RES_PATH="$ENV_PATH/res"

alias dcj="$RES_PATH/dcj/dcj.sh"
alias dcjt="dcj test --source"

alias msgLib="less $RES_PATH/message.py"

function initTaskDir {
    for TASK_NAME in "$@"
    do
        mkdir "$TASK_NAME"
        cp "$RES_PATH/taskSolver.py" "$TASK_NAME/$TASK_NAME.py"
    done
}

cat << EOF
DistributedCodeJam environment:
    [*] initTaskDir <TASK_NAME_0>...
    [*] dcj
    [*] dcjt <source.py> --nodes 10 # build & run
    [*] msgLib # less message.py
EOF
