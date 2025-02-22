#!/bin/bash

icon=""  # Nerd Font gamepad icon

# Get battery info, suppress errors
battery_info=$(dualsensectl battery 2>/dev/null)

# Check for "No device found" 
if echo "$battery_info" | grep -q "No device found"; then
  echo '{ "text": "'"$icon Off"'" }'
elif echo "$battery_info" | grep -q "Connection timed out"; then
  echo '{ "text": "'"$icon Disconnected"'" }'
else
  # Extract battery level and state
  level=$(echo "$battery_info" | awk '{print $3}')
  state=$(echo "$battery_info" | awk '{print $4}')

  # Output with icon and level
  echo '{ "text": "'"$icon $level"'" }' 
fi