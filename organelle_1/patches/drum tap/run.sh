#!/bin/bash 
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH


killall pd
cd "$SCRIPTPATH"
cd ..
pd -rt   -audiobuf 8 -audiodev 9,9 -midiindev 1 "mother.pd" "$SCRIPTPATH/main.pd"
