#!/bin/bash

# Exit if something fails
set -e

rm ~/.local/share/kservices5/plasma-runner-KRunnerAlias.desktop
rm ~/.local/share/dbus-1/services/org.kde.KRunnerAlias.service

kquitapp5 krunner