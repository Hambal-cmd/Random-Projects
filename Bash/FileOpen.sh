#!/bin/bash

FILES=("/home/hamlab/Documents/BMSCE /I-sem/Chemistry" "/home/hamlab/Documents/BMSCE /I-sem/Mathematics" "/home/hamlab/Documents/BMSCE /I-sem/Python")

echo "Please select a file to open:"

for i in "${!FILES[@]}"; 
do
    echo "  $((i+1))) $(basename "${FILES[$i]}")"
done

read -p "Enter the number of the file you want to open: " choice

if ! [[ "$choice" =~ ^[0-9]+$ ]]
then
    echo "Error: Invalid input. Please enter a number."
    exit 1
fi

if [ "$choice" -lt 1 ] || [ "$choice" -gt "${#FILES[@]}" ]
then
    echo "Error: Invalid selection. Please enter a number between 1 and ${#FILES[@]}."
    exit 1
fi

SELECTED_FILE="${FILES[$((choice-1))]}"

if [ -e "$SELECTED_FILE" ]
then
    echo "Opening $SELECTED_FILE..."
    xdg-open "$SELECTED_FILE"
else
    echo "Error: File not found at $SELECTED_FILE"
    exit 1
fi
    
exit 0




