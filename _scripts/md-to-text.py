# This script converts a markdown file to plain text 
# for later use it in text to speech functionality

import re
import os
import sys
import emoji
import pyperclip
import frontmatter
from pathlib import Path
from markdown import markdown
from bs4 import BeautifulSoup

def remove_emojis(text):
    text = text.replace(" :)", ".").replace(" :P", ".").replace(" :p", ".")
    return emoji.get_emoji_regexp().sub(r'', text)

def sanitize_markdown(md):
    # split at ``` as we don't want to extract code blocks`
    content = md.split("```")
    
    # join alternating blocks, this removes the code blocks
    noCodeBlocks = "".join(content[::2])

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(noCodeBlocks, extensions=['tables'])

    # extract text
    soup = BeautifulSoup(html, "html.parser")

    # don't include tables
    for tag in soup.select('table'):
        tag.decompose()

    text = ''.join(soup.findAll(text=True))

    # remove emojis from text
    text = remove_emojis(text)
    
    # remove extra parenthesis and jekyll stuff from text
    text = text.replace("()", "")
    text = re.sub('{.*?}', '', text)

    return text

file = Path(os.getcwd() + "/" + sys.argv[1])

with open(file) as f:
    content = frontmatter.load(file).content
    
    text = sanitize_markdown(content)

    pyperclip.copy(text)
    print(text)
