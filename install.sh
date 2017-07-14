#!/bin/bash

CHANGER_PATH="$PWD/changer.py";
echo "Using: $CHANGER_PATH";

echo "Your current crontab: ";
crontab -l;
echo;
echo "----------------------";
echo;

crontab -l > /tmp/mycron;
echo "0 * * * * /usr/bin/python3 $CHANGER_PATH" >> /tmp/mycron;
crontab /tmp/mycron;
echo "Your updated crontab: ";
crontab -l;
rm /tmp/mycron;
