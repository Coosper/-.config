#!/bin/bash

icon="󰊴"  # Nerd Font gamepad icon
iconoff="󰊵"

# Get battery info
battery_info=$(dualsensectl battery 2>&1)

# Check if device is found and extract battery level
if echo "$battery_info" | grep -q "No device found"; then
    echo '{ "text": "'"$iconoff  Off"'" }'
else
    level=$(echo "$battery_info" | grep -oP '^\d{1,2}')
    # Output based on level or checking status, appending '%' if level is found
    if [[ -n "$level" ]]; then
        echo '{ "text": "'"$icon  ${level}%"' }'
    else
        echo '{ "text": "'"$icon  Checking"'" }'
    fi
fi
