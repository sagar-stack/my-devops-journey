#!/bin/bash

#1. Setting a variable
APP_NAME="MegaApp"
DEPLOY_DATE=$(date)

#2. Using the variable(Note the $ sign!)
echo "Deploying $APP_NAME..."
echo "Deployement started at: $DEPLOY_DATE"

#3. Doing a fake deployement
mkdir -p deployments/$APP_NAME
touch deployments/$APP_NAME/version_1.txt

echo "Success! Check the deployements folder."

