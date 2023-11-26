#!/usr/bin/env python3

import markdown
import os

def md2html(mdfile, htmlfile):
    with open(mdfile, "r") as mdfile:
        text = mdfile.read()
        html = markdown.markdown(text)
        with open(htmlfile, "w") as htmlfile:
            htmlfile.write('<head><meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1"></head>\n')
            htmlfile.write('<style> body {font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";font-size: 18px;line-height: 1.5;margin-left: 64px;color: #24292e;background-color:#fff}</style>\n')
            htmlfile.write(html)

for filename in os.listdir("."):
    if filename.endswith(".md"):
        md2html(filename, filename[:-3] + ".html")
        print("Converted " + filename + " to " + filename[:-3] + ".html")
    else:
        continue