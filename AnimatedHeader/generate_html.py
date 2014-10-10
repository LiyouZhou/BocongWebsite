#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import codecs

menu = []
with codecs.open('Structure.txt', 'r', encoding='utf-8') as fd:
	for line in fd:
		if line.strip() != '':
			if line.startswith('\t') or line.startswith(' '):
				menu[-1][1].append( line.strip() )
			else: menu.append( (line.strip(), []) )

env = Environment(loader=FileSystemLoader('./templates'))
main = env.get_template("main.html", parent="./templates")
s = main.render(menu=menu)

with codecs.open('index.html', 'w', encoding='utf-8') as fd:
	fd.write(s)