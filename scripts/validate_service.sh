#!/bin/bash
# Simple health check
curl -f http://localhost:5000 || exit 1
