import os
# The following uses code adapted from:
# https://stackoverflow.com/questions/16941885/want-to-resize-terminal-windows-in-python-working-but-not-quite-right
print("\x1b[8;40;100t")
os.system("python3 main.py")
