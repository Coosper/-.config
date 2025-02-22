#!/bin/bash

# Get battery info
battery_info=$(dualsensectl-git battery 2>&1)

# Check if controller is connected
if echo "$battery_info" | grep -q "No device found"; then
  echo '{ "text": " Off" }'  # Controller off
elif echo "$battery_info" | grep -q "Connection timed out"; then
  echo '{ "text": " Disconnected" }'  # Controller disconnected
else
  # Extract battery level
  level=$(echo "$battery_info" | awk '{print $3}')
  echo '{ "text": " '"$level"'" }'  # Controller connected with battery level
fi