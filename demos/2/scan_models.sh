#!/bin/bash
echo "Scanning models simple_model.pth"
python -m picklescan -p simple_model.pth
read -p "" -n1 -s
echo "Scanning models infected_model.pth"
python -m picklescan -p infected_model.pth
