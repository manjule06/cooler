#!/bin/bash

factorial() {
     if [ $1 -eq 0 ] || [ $1 -eq 1 ]; then
        echo 1
     else
        echo $(( $1 * $(factorial $(( $1 - 1))) ))
     fi
}

echo -n "Enter the number to calculate the factorial: "
read num

if [[ $num =~ ^[0-9]+$ ]]; then
   result=$(factorial $num)
   echo "Factorial of $num is : $result"
else
   echo "Enter valid input"
fi

