#!/bin/bash -e

mkdir stripped

for i in [0-9]{2}_*.py
do
    d=`echo $i | sed 's/md$/py/'`
    python tools/strip_code.py $i stripped/$d
done

flake8 stripped/
rm -rf stripped/
