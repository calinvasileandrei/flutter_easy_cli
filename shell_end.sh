#!/bin/sh
echo 'Flutter updating packages'
cd $1
flutter pub get
flutter pub upgrade
echo "Flutter upgraded!"
