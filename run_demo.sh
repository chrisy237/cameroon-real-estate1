#!/bin/bash

# Build and run Docker containers in detached mode
docker-compose up --build -d

# Print a message with the app URL
echo "Cameroon Real Estate app is running at http://<EC2-IP>:8000"
