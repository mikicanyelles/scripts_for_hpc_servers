#!/bin/bash

echo "CPU information by node:"
echo ""
echo " NODE  - USED/FREE/Other/TOTAL of CORES "
sinfo -No"%n -      %.12C"  | grep -v '.bat\|.ext' | sed '1d'
echo ""
