#!/bin/bash

# Get battery level, handle potential errors
battery_info=$(dualsensectl-git battery 2>/dev/null)

# Check if the controller is connected
if [[ -z "$battery_info" ]]; then
    echo '{ "text": "" }'  # Display a "disconnected" icon (power plug off)
else
    # Extract the battery percentage
    level=$(echo "$battery_info" | awk '{print $3}')
    echo '{ "text": " '"$level"'" }'
fi 