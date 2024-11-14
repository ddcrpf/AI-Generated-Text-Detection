#!/bin/bash
# Start the application, e.g., a Flask server
cd /home/ec2-user/myapp
nohup python app.py > /dev/null 2>&1 &
