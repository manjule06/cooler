#!/bin/bash

palindrome() {
     original="$1"
     reversed=$(echo "$original" | rev)

     if [ "$original" = "$reversed" ]; then
        echo "The Given String is Palindrome"
     else
        echo "The Given string Not a Palindrome"
     fi
}

echo -n "Enter a String to check if it is palindrome or not :"
read input_string

result=$(echo "$input_string" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')
palindrome "$result"
