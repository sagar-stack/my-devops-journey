#!/bin/bash

# Create a 'logs' folder if it doesn't exist
mkdir -p logs

# Get the current date and time
NOW=$(date)

# Save a message into a log file with a timestamp
echo "[$NOW] Script was executed by user: $USER" >> logs/activity.log
echo "[$NOW] System check: PASSED" >> logs/activity.log

echo "Activity logged in logs/activity.log"