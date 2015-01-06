#!/bin/bash 
# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
echo $SCRIPTPATH

cd "$SCRIPTPATH"

killall wpa_supplicant
killall udhcpc
cp wpa /etc/wpa_supplicant.conf
wpa_supplicant -d -Dnl80211 -c/etc/wpa_supplicant.conf -iwlan0 -B
udhcpc -R -b -p /var/run/udhcpc.wlan0.pid -i wlan0



