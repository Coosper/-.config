#!/bin/bash

icon=""  # Nerd Font gamepad icon

# Get battery info, suppress errors
battery_info=$(dualsensectl battery)

# Check for "No device found" 
if echo "$battery_info" | grep -q "No device found"; then
    echo '{ "text": "'"$icon Off"'" }'
elif echo "$battery_info" | grep -q "Connection timed out"; then
    echo '{ "text": "'"$icon Disconnected"'" }'
else
    # Extract battery level and state
    level=$(echo "$battery_info" | grep -oP 'Battery: \K\d+')
    state=$(echo "$battery_info" | grep -oP 'State: \K\w+')

    # Output with icon and level
    if [ -n "$level" ] && [ -n "$state" ]; then
        echo '{ "text": "'"$icon $level% ($state)"'" }'
    else
        echo '{ "text": "'"$icon Unknown"'" }'
    fi
fi