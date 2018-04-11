#!/bin/bash

LEVEL=level01
# TODO: we need a solution that doesn't require us to put password in the source code
PASSWORD=f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2

# Boiler Plate

cd "$(dirname "$0")"
useradd -m $LEVEL -s /bin/bash
passwd $LEVEL <<< "$PASSWORD"$'\n'"$PASSWORD"
echo $PASSWORD > /home/$LEVEL/password
