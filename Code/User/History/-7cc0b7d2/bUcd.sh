#!/bin/bash

icon=""  # Nerd Font gamepad icon

# Get battery info, suppress errors
battery_info=$(dualsensectl battery 2>&1)

# Check for "No device found"
if echo "$battery_info" | grep -q "No device found"; then
    echo '{ "text": "'"$icon Off"'" }'
else
    # Extract battery level
    level=$(echo "$battery_info" | grep -oP '^\d{1,2}')

    # Output with icon and level
    if [ -n "$level" ]; then
        echo '{ "text": "'"$icon $level%"'" }'
    else
        echo '{ "text": "'"$icon Unknown"'" }'
    fi
fi