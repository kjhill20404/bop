#! /usr/bin/bash

echo 'installing python'
sudo apt install python3 

echo 'installing plysound'
sudo pip3 install playsound

echo 'installing gtts'
sudo pip3 install gTTS

echo 'changing dir'
cd ~
echo 'installing wget'
apt-get install wget

echo 'installing main bop file'
wget https://github.com/kjhill20404/bop/archive/refs/heads/main.zip

echo 'unziping files'
unzip main.zip
echo 'changing dir name'
mv /home/kevin/bop-main /home/kevin/bop

rm main.zip

