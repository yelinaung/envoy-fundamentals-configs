#!/bin/env bash
PORT=$1
echo "Starting web server at ${PORT}"
python -m http.server "$PORT"
