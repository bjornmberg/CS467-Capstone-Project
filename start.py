import os
# The following uses code adapted from:
# https://stackoverflow.com/questions/16941885/want-to-resize-terminal-windows-in-python-working-but-not-quite-right
print("\x1b[8;40;100t")
# Call main.py via system call to allow formatting to proceed correctly
os.system("python3 main.py")
