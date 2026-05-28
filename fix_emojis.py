import re

with open('latexGame.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    # Emojis in python 3 can be caught using a regex for high unicode blocks.
    # Alternatively, we can just replace anything not ascii, minus specific punctuation like em-dash and bullet point
    if line.startswith(r'\sceneicon{'):
        # replace whatever is inside with an asterisk or question mark
        line = re.sub(r'\\sceneicon\{.*?\}', r'\\sceneicon{$\\star$}', line)
    elif r'\textbf{' in line and r'\quad' in line:
        # Many hyperlinks use \textbf{emoji}\quad
        # We can strip emojis from within \textbf{...}
        line = re.sub(r'\\textbf\{[^\}]+\}\\quad', r'\\textbf{$\\rightarrow$}\\quad', line)
    new_lines.append(line)

with open('latexGame.tex', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
