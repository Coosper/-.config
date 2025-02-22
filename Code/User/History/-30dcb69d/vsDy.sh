#!/bin/bash

# Get CPU temperature (replace with your preferred method)
cpu_temp=$(sensors | grep "Core 0" | awk '{print $3}' | tr -d '+°C')

# Get GPU temperature for AMD card
gpu_temp=$(sensors | grep "edge" | awk '{print $2}' | tr -d '+°C')

# Output in Waybar's JSON format
echo "{ \"text\": \"CPU: $cpu_temp°C GPU: $gpu_temp°C\" }"
