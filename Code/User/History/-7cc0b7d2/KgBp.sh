#!/bin/bash

notify_id=-1
icon="/usr/share/icons/breeze-dark/devices/64/input-gamepad.svg"
dev=$(echo $DS_DEV | tr '[:lower:]' '[:upper:]')

send_notification() {
    notify_id=$(notify-desktop -r $notify_id -i $icon "$dev" "$1")
}

monitor_battery() {
    while true; do
        battery=$(dualsensectl battery 2> /dev/null)
        perc=$(echo $battery | cut -d' ' -f1)
        state=$(echo $battery | cut -d' ' -f2)
        
        if [ -n "$perc" ] && [ -n "$state" ]; then
            [ $perc -lt 15 ] && [ "$state" != "charging" ] && send_notification "Low battery ${perc}%"
            echo "{\"class\": \"\", \"text\": \" ${perc}%\"}"
        fi
        
        sleep 5m
    done
}

case "$1" in
    add)
        send_notification "Controller connected"
        monitor_battery
        ;;
    remove)
        send_notification "Controller disconnected"
        echo "{\"text\": \"\"}"
        ;;
    *)
        echo "{\"text\": \"\"}"
        exec dualsensectl monitor add "${BASH_SOURCE[0]} add" remove "${BASH_SOURCE[0]} remove"
        ;;
esac