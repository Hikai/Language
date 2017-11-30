#!/bin/sh

hciconfig hci0 up
hciconfig hci0 class 0x50040c
hcitool scan
