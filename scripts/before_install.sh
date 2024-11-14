#!/bin/bash

# Update the package index
sudo yum update -y

# Install Python 3 and pip if not already installed
sudo yum install -y python3

# Ensure pip is up-to-date
sudo python3 -m ensurepip --upgrade
sudo python3 -m pip install --upgrade pip
