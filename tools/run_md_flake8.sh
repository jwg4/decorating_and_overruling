#!/bin/bash

mkdir stripped

for i in [0-9]{2}_*.py
    d=`echo $i | sed 's/md$/py/'`
    python tools/strip_code $i stripped/$d

flake8 stripped/
rm -rf stripped/
