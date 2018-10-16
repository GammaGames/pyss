#!/usr/bin/python3

import sass, sys, os

if len(sys.argv) < 2 or sys.argv[1] == "-h":
    print("Usage: pyss <source file/folder> [target file/folder] [output_style]")
    quit()

source = sys.argv[1]

if len(sys.argv) < 3:
    target = ""
else:
    target = sys.argv[2]

if len(sys.argv) < 4:
    style = "compressed"
else:
    style = sys.argv[3]


if os.path.isfile(source):
    if not target:
        target = os.path.splitext(os.path.basename(source))[0]

    css = sass.compile(filename=source, output_style=style)
    if not target.endswith(".css"):
        target = target + ".css"
    with open(target, 'w') as f:
        f.write(css)

elif os.path.isdir(source):
    if not target:
        target = "css"
    sass.compile(dirname=(source, target), output_style=style)

quit()
