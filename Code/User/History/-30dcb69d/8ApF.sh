#!/bin/bash

# Get CPU temperature (replace with your preferred method)
cpu_temp=$(sensors | grep "Core 0" | awk '{print $3}' | cut -c2-3)

# Get GPU temperature (replace with your preferred method)
gpu_temp=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)

# Output in Waybar's JSON format
echo "{ \"text\": \"CPU: $cpu_temp°C GPU: $gpu_temp°C\" }"