#!/bin/bash

mkdir -p ~/.local/share/kservices5/
cp plasma-runner-KRunnerAlias.desktop ~/.local/share/kservices5/
kquitapp5 krunner
pkill python3
python3 src/KRunnerAlias.py