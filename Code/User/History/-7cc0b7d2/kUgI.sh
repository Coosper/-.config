#!/bin/bash

# Get battery info, suppress error messages
battery_info=$(dualsensectl battery 2>/dev/null)

# Check for specific "No device found" message
if echo "$battery_info" | grep -q "No device found"; then
    echo '{ "text": " Off" }'  # Controller off
else
    # Check for "Connection timed out" which also indicates disconnection
    if echo "$battery_info" | grep -q "Connection timed out"; then
        echo '{ "text": " Disconnected" }'  # Controller disconnected
    else
        # Extract battery level
        level=$(echo "$battery_info" | awk '{print $3}')
        echo '{ "text": " '"$level"'" }'  # Controller connected with battery level
    fi
fi