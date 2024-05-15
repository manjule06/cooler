#!/bin/bash

echo "Enter the array elements"
read -a arr
n=${#arr[*]}
echo $n
echo "Original array is: " ${arr[*]}

for (( i = 0; i < n - 1; i++ )); do
    for (( j = 0; j < n - i - 1; j++ )); do
        if [ ${arr[j]} -gt ${arr[j + 1]} ]; then
            temp=${arr[j]}
            arr[j]=${arr[j + 1]}
            arr[j + 1]=$temp
        fi
    done
done
echo "Sorted array is: " ${arr[*]}
