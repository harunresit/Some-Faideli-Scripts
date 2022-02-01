#!/bin/bash
#author: Harun Resit Kirbiyik

pwd
sudo apt update
echo Started to build vera++
sudo apt install vera++
wget https://github.com/verateam/vera/archive/refs/tags/v1.3.0.zip
unzip v1.3.0.zip
cd vera-1.3.0
sudo apt-get install lua5.2 liblua5.2-dev libluabind-dev
sudo apt-get install libboost-all-dev
sudo apt-get install tcl
mkdir build
cd build
cmake ..
sudo sed -i 's/VERA_USE_SYSTEM_LUA:BOOL=ON/VERA_USE_SYSTEM_LUA:BOOL=OFF/g' CMakeCache.txt
sudo sed -i 's/VERA_LUA:BOOL=ON/VERA_LUA:BOOL=OFF/g' CMakeCache.txt
cmake ..
sudo make -j8
sudo make install

