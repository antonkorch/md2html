#!/usr/bin/env python3

import markdown
import os

def md2html(mdfile, htmlfile):
    with open(mdfile, "r") as mdfile:
        text = mdfile.read()
        html = markdown.markdown(text, extensions=['tables'])
        with open(htmlfile, "w") as htmlfile:
            htmlfile.write('<head><meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1"></head>\n')
            htmlfile.write('<link rel="stylesheet" href="https://stackedit.io/style.css" />\n')
            htmlfile.write('<body class="stackedit"><div class="stackedit__html">')
            htmlfile.write(html)

for filename in os.listdir("."):
    if filename.endswith(".md"):
        md2html(filename, filename[:-3] + ".html")
        print("Converted " + filename + " to " + filename[:-3] + ".html")
    else:
        continue