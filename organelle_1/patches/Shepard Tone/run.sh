#!/bin/bash 
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

killall pd
cd "$SCRIPTPATH"
cd ..
pd -rt   "mother.pd" "$SCRIPTPATH/shepard.tone.pd"
