#!/bin/bash

# UUID: e2 c5 6d b5 df fb 48 d2 b0 60 d0 f5 a7 10 96 e1
# Major: 00 01 
# Minor: 00 02

sudo hcitool -i hci0 cmd 0x08 0x000a 00
sudo hcitool -i hci0 cmd 0x08 0x0008 1e 02 01 1a 1a ff 4c 00 02 15 e2 c5 6d b5 df fb 48 d2 b0 60 d0 f5 a7 10 96 e1 00 01 00 02 c8 00
sudo hcitool -i hci0 cmd 0x08 0x000a 01 