#!/bin/bash
echo "Scanning models diffusion_pytorch_model.bin"
python -m picklescan -p diffusion_pytorch_model.bin
read -p "" -n1 -s
echo "Scanning models infected_model.bin"
python -m picklescan -p infected_model.bin
