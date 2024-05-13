#!/bin/bash

prime_number() {
     num=$1
     if [ $num -lt 2 ]; then
        echo "The given number is not prime"
     else
        for ((i=2; i<num; i++)); do
            if [ $((num % i)) -eq 0 ]; then
               echo "Given number is not Prime number"
               return
            fi
       done
       echo "Given number is Prime Number"
    fi
}

echo -n "Enter a number : "
read n

if [[ $n =~ ^[1-9][0-9]*$ ]]; then
   prime_number "$n"
else
   echo "invalid choice"
fi
