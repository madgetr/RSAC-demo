#!/bin/bash
echo "Scanning good_pickle.pkl"
python -m picklescan -p good_pickle.pkl
read -p "" -n1 -s
echo "Scanning bad_pickle.pkl"
python -m picklescan -p bad_pickle.pkl
read -p "" -n1 -s
echo "Scanning worse_pickle.pkl"
python -m picklescan -p worse_pickle.pkl
