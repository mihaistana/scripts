#!/usr/bin/env python
#   cat movistar.txt | python3 cidr_merge.py

import sys
from netaddr import *


data = sys.stdin.readlines()

if len(data) == 1:
    data = data[0].split()

nets = IPSet(data)

# sort and merge cidrs
dat_merged_ips = cidr_merge(nets)

for cidr in dat_merged_ips:
    print (cidr)