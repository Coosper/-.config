#!/bin/bash

icon="󰊴"  # Nerd Font gamepad icon
iconoff="󰊵"

# Get battery info
battery_info=$(dualsensectl battery 2>&1)

# Check if device is found and extract battery level
if echo "$battery_info" | grep -q "No device found"; then
    echo '{ "text": "'"$iconoff  Off"'" }'
else
    level=$(echo "$battery_info" | grep -oP '\d+(?=%)' || echo "Checking")
    echo '{ "text": "'"$icon  $level"'" }'
fi
