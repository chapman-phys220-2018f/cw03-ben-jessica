#!/bin/bash
if [ -f "./fibs.csv.bak" ]; then
    echo "fibs.csv.bak already exists"
    echo "exiting"
    exit 1
fi

if [ -f "./fibs.csv" ]; then
    mv fibs.csv fibs.csv.bak
    echo "fibs.csv already exists. creating backup"
fi

for i in $( seq 10000 ); do
    x=$(python fib.py $i)
    echo "$x" >> fibs.csv
done