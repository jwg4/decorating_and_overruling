#!/bin/bash -e

mkdir stripped

for i in [0-9][0-9]_*.md; do
    d=`echo $i | sed 's/md$/py/'`
    python tools/strip_code.py $i stripped/$d
done

flake8 --ignore=E302,E302,E305,W391,E402 stripped/
rm -rf stripped/
