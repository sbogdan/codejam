#!/usr/bin/env bash

CJ_TYPE="$1"
if [[ "$CJ_TYPE" != "dcj" && "$CJ_TYPE" != "cj" ]]; then
    echo $CJ_TYPE
    echo 1>&2 "usage: $(basename "$0") cj|dcj"
else
    ABS_PATH_CLI=$(dirname "$0")/abspath
    ENV_PATH=$($ABS_PATH_CLI $(dirname "$0"))
    RES_PATH="$ENV_PATH/res"
    function downloadInput {
        INPUT_NAME=${1?"downloadInput <INPUT_NAME>"}
        mv ~/Downloads/$INPUT_NAME.py $INPUT_NAME.py.1
        ln -sf $INPUT_NAME.py.1 $INPUT_NAME.py
        idx=2

        for f in ~/Downloads/${INPUT_NAME}*py; do
            mv $f $INPUT_NAME.py.$idx
            ((idx+=1))
        done
    }

    if [[ "$CJ_TYPE" == "cj" ]]; then
        echo "CodeJam environment:"
        echo "[*] initTaskDir <TASK_NAME_0>..."

    else
        alias dcj="$RES_PATH/dcj/dcj.sh"
        alias dcjt="dcj test --source"

        alias msgLib="less $RES_PATH/message.py"

        echo "DistributedCodeJam environment:"
        echo "[*] initTaskDir <TASK_NAME_0>..."
        echo "[*] dcj"
        echo "[*] dcjt <source.py> --nodes 10 # build & run"
        echo "[*] msgLib # less message.py"
        echo "[*] downloadInput <INPUT_NAME>"
    fi

    function initTaskDir {
        for TASK_NAME in "$@"
        do
            mkdir "$TASK_NAME"
            cp "$RES_PATH/${CJ_TYPE}Solver.py" "$TASK_NAME/$TASK_NAME.py"
            cp "$RES_PATH/${CJ_TYPE}GenerateInput.py" "$TASK_NAME/generateInput.py"
        done
    }
fi
