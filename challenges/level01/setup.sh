#!/bin/bash

LEVEL=level01
PASSWORD=f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2 # SHA256

# Boiler Plate

cd "$(dirname "$0")"
useradd -m $LEVEL
echo $PASSWORD > /home/$LEVEL/password




