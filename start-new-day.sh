#!/bin/bash

# Get day number as input
read -p "Enter day number: " dayNum

# Create folder 
mkdir "Day-$dayNum"

# Change to folder
cd "Day-$dayNum"

# Create files
touch "prompt-day-$dayNum.txt"
touch "input-day-$dayNum.txt" 
touch "example.txt"
touch "answer-day-$dayNum.py"

# Stage files
git add.

# Commit files
git commit -m "Initialize Day $dayNum"

# Sync with remote
git push origin master
