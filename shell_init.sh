#!/bin/sh
echo 'Script Started'
echo "App Name: $1 "
very_good create $1

git clone https://github.com/calinvasileandrei/flutter_starter

cd $1
rm -rf lib
rm -rf test
rm -rf pubspec.yaml
rm -rf analysis_options.yaml

cd ..

mv flutter_starter/lib $1
mv flutter_starter/test $1
mv flutter_starter/assets $1
mv flutter_starter/pubspec.yaml $1
mv flutter_starter/analysis_options.yaml $1

rm -rf flutter_starter
