---
layout: post
title: "Cronjob Creation to Auto-Start Docker Images"
date: 2024-07-05
categories: [multi-server]
---

How to create a cronjob to check if the Kasm Docker images are running and auto-start them if not.

1. **Create a Script to Check the Docker Container and Manage Port 443:**

   Create a script, say `check_and_restart_docker.sh`, with the following content:

   ```bash
   #!/bin/bash

   # Docker container ID to check
   CONTAINER_ID="875ca0bef633"

   # Check if the Docker container is running
   if ! docker ps | grep -q "$CONTAINER_ID"; then
     echo "Docker container $CONTAINER_ID is not running."

     # Find the process using port 443
     PID=$(sudo lsof -t -i:443)

     if [ -n "$PID" ]; then
       echo "Killing process $PID using port 443."
       sudo kill -9 $PID
     fi

     # Start the Docker container
     echo "Starting Docker container $CONTAINER_ID."
     docker start $CONTAINER_ID
   else
     echo "Docker container $CONTAINER_ID is running."
   fi
   ```

2. **Make the Script Executable:**

   ```bash
   sudo chmod +x /path/to/check_and_restart_docker.sh
   ```

3. **Create a Cron Job to Run the Script Periodically:**

   Open the cron job editor:

   ```bash
   sudo crontab -e
   ```

   Add the following line to run the script every 5 minutes (adjust the interval as needed):

   ```bash
   */5 * * * * /path/to/check_and_restart_docker.sh >> /var/log/check_and_restart_docker.log 2>&1
   ```

   This will run the script every 5 minutes and log the output to `/var/log/check_and_restart_docker.log`.

4. **Save and Exit the Cron Job Editor:**

   Save the file and exit the editor (for `nano`, press `Ctrl+X`, then `Y`, and `Enter`).

This setup will ensure that the specified Docker container is checked every 5 minutes. If it is not running, it will kill any process using port 443 and restart the Docker container.