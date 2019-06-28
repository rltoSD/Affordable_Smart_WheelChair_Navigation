#!/bin/bash
echo Running Ubuntu Kernal Installation
sudo add-apt-repository ppa:ubilinux/up
sudo apt update
sudo apt-get autoremove --purge 'linux-.*generic'
sudo apt-get install linux-image-generic-hwe-18.04-upboard
sudo apt dist-upgrade -y
echo finished running ubuntu kernal installation
echo Running Ampak Firmware for WiFi and Bluetooth
sudo apt install firmware-ampak
sudo apt install upboard-extras
sudo usermod -a -G gpio ${USER}
sudo usermod -a -G leds ${USER}
sudo usermod -a -G spi ${USER}
sudo usermod -a -G i2c ${USER}
sudo usermod -a -G dialout ${USER}
echo Finished running Ampak Firmware for WiFi and Bluetooth
echo Ending Ubuntu Installation
sudo reboot
