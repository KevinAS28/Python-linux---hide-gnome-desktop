#!/usr/bin/python3

import os
import sys

#true false
if len(sys.argv) > 1:
  os.system("gsettings set org.gnome.desktop.background show-desktop-icons %s" %(sys.argv[1]))
