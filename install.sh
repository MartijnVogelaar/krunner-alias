#!/bin/bash

# Exit if something fails
set -e

mkdir -p ~/.local/share/krunner/dbusplugins/
mkdir -p ~/.local/share/dbus-1/services/

cp plasma-runner-KRunnerAlias.desktop ~/.local/share/krunner/dbusplugins
sed "s|%{PROJECTDIR}/KRunnerAlias.py|${PWD}/src/KRunnerAlias.py|" "org.kde.KRunnerAlias.service" > ~/.local/share/dbus-1/services/org.kde.KRunnerAlias.service

kquitapp6 krunner
