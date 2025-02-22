#!/bin/bash

# Get battery status from dualsensectl
battery_status=$(dualsensectl battery 2>&1)

# Check if dualsensectl command was successful
if [ $? -ne 0 ]; then
  if echo "$battery_status" | grep -q "No controllers found"; then
    echo "{\"text\": \"Controller Off\", \"class\": \"error\"}"
  else
    echo "{\"text\": \"Error\", \"class\": \"error\"}"
  fi
  exit 1
fi

# Extract the battery percentage
battery_percentage=$(echo $battery_status | grep -oP '\d+%')

# Check if the battery percentage was extracted successfully
if [ -z "$battery_percentage" ]; then
  echo "{\"text\": \"N/A\", \"class\": \"error\"}"
  exit 1
fi

# Shorten the battery percentage to the first two digits
short_battery_percentage=$(echo $battery_percentage | grep -oP '^\d{1,2}')

# Output the result in JSON format for Waybar
echo "{\"text\": \"$short_battery_percentage%\", \"class\": \"battery\"}"