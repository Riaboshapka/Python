#!/bin/bash

echo "Number of arguments: $#"

for i in "$@"
do
    echo "Вы написали: ${i}"
done
