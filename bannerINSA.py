#!/usr/bin/python3
# -*- coding: utf-8 -*-
# file: bannerINSA.py
# author: Nathan PERIER
# created: 2021/03/24
# last modified: 2021/05/06
# github page: https://github.com/NathanPERIER/BannerINSA

import sys
import re
import random


colour_codes = {
	'black': 0, 
	'red': 1, 
	'green': 2, 
	'yellow': 3, 
	'blue': 4, 
	'magenta': 5, 
	'cyan': 6, 
	'white': 7,
	'dafault': 9
}
reg_8bit = re.compile(r'8bit-(\d{1,3})')
reg_truecolor = re.compile(r'#([0-9a-fA-F]{6})')
def translateCol(c) :
	if c == 'random' :
		c = random.choice(list(colour_codes.keys()))
	if c in colour_codes :
		col_code = colour_codes[c]
		return f"\033[1;3{col_code}m"
	if c.startswith('8bit-') :
		if c == '8bit-random' :
			col_code = random.randint(0, 255)
		else : 
			m = reg_8bit.fullmatch(c)
			if m is None or int(m.group(1)) >= 256 :
				return None
			col_code = m.group(1)
		return f"\033[38;5;{col_code}m"
	if c == 'truecolor-random' :
		col_code = [
			random.randint(0, 255),
			random.randint(0, 255),
			random.randint(0, 255)
		]
	else : 
		m = reg_truecolor.fullmatch(c)
		if m is None :
			return None
		col_code = m.group(1)
		col_code = [
			int(col_code[0:2], 16),
			int(col_code[2:4], 16),
			int(col_code[4:6], 16)
		]
	return f"\033[38;2;{col_code[0]};{col_code[1]};{col_code[2]}m"


if len(sys.argv) > 1 :
	if sys.argv[1] in ['-h', '--help'] :
		print(f"usage : {sys.argv[0]} [--<insa>] [-t text] [-s subtitle] [--center | --left | --right] [-c colour] [--fill | --corner] [--bar | --sep] [--compatibility]")
		sys.exit(0)


i = 1

names = {
	'--rennes': 'RENNES', 
	'--lyon': 'LYON', 
	'--toulouse': 'TOULOUSE', 
	'--rouen': 'ROUEN', 
	'--strasbourg': 'STRASBOURG', 
	'--cvl': 'CENTRE VAL DE LOIRE', 
	'--hdf': 'HAUTS-DE-FRANCE', 
	'--euromed': 'EURO-MÉDITERRANNÉE'
}
if i < len(sys.argv) and sys.argv[i] in names :
	insa = names[sys.argv[i]]
	i += 1
else :
	insa = names['--rennes']


if i+1 < len(sys.argv) and sys.argv[i] == '-t' : 
	text = sys.argv[i+1]
	i += 2
else : 
	text = ''


maxlen = max(17, len(insa), len(text))
logo_len = maxlen + 48


if i+1 < len(sys.argv) and sys.argv[i] == '-s' :
	subtitle = sys.argv[i+1]
	if len(subtitle) > logo_len - 2 : 
		subtitle = ''
	i += 2
else :
	subtitle=''


align = 'c'
if i < len(sys.argv) : 
	if sys.argv[i] in ['--center', '--left', '--right'] :
		align = sys.argv[i][2]
		i += 1


text_col = None
if i+1 < len(sys.argv) and sys.argv[i] == '-c' :
	text_col = translateCol(sys.argv[i+1])
	i += 2
if text_col is None :
	text_col = translateCol('red')


corner_col = ''
bars_col = None
if i < len(sys.argv) :
	if sys.argv[i] == '--fill' :
		splitted = list(text_col)
		if text_col[1:5] == '[1;3' :
			splitted[2] = '0'
			bars_col = ''.join(splitted)
			splitted[2] = '1'
			splitted[4] = '4'
			text_col = ''.join(splitted)
			if splitted[5] == '7' :
				text_col = text_col[:-1] + ";30m"
		else : 
			bars_col = text_col
			splitted[2] = '1;4'
			text_col = ''.join(splitted)
		i += 1
	elif sys.argv[i] == '--corner' :
		corner_col = '\033[1;30m'
		i += 1


bar = False
char_sep = ' '
if i < len(sys.argv) :
	if sys.argv[i] == '--bar' : 
		bar = True
		i += 1
	elif sys.argv[i] == '--sep' :
		char_sep = '='
		i += 1


compatibility_mode = (i < len(sys.argv) and sys.argv[i] == '--compatibility')
if compatibility_mode :
	chars = ['|', '|', '|', '-', '-', '-', ' ', ' ']
	if bars_col is not None :
		bars_col = text_col
		text_col += ' '			# Add a coloured space before
		maxlen += 1				# Add a coloured space after
		logo_len += 2
	i += 1
else :
	chars = ['╻', '┃', '╹', '╶', '─', '╴', '▄', '▀']


tab_a = [''] * 8
nb_a = 0
if i < len(sys.argv) and re.fullmatch(r'--aaa+', sys.argv[i]) != None :
	import shutil
	nb_cols = shutil.get_terminal_size().columns
	if nb_cols > logo_len : 
		nb_a = (nb_cols - logo_len) // 13
		tab_a[0] = '8888b        ' * nb_a
		tab_a[1] = '88888b       ' * nb_a
		tab_a[2] = '888Y88b      ' * nb_a
		tab_a[3] = '888 Y88b     ' * nb_a
		tab_a[4] = '888  Y88b    ' * nb_a
		tab_a[5] = '888   Y88b   ' * nb_a
		tab_a[6] = '8888888888b  ' * nb_a
		tab_a[7] = '888     Y88b ' * nb_a
		logo_len += 13 * nb_a



reset = '\033[0m'
fixed_padding = ' ' * (maxlen - 16) + reset
insa_padding = ' ' * (maxlen - len(insa) + 1) + reset
text_padding = ' ' * (maxlen - len(text) + 1) + reset

logo = [
	f"{text_col} 8888888 888b    888  .d8888b.  {tab_a[0]}8888b {corner_col} Y8888 {chars[0]}                  {fixed_padding}",
	f"{text_col}   888   8888b   888 d88P  Y88b {tab_a[1]}88888b {corner_col} Y888 {chars[1]} INSTITUT NATIONAL{fixed_padding}",
	f"{text_col}   888   88888b  888 Y88b.      {tab_a[2]}888Y88b {corner_col} Y88 {chars[1]} DES SCIENCES     {fixed_padding}",
	f"{text_col}   888   888Y88b 888  \"Y888b.   {tab_a[3]}888 Y88b {corner_col} Y8 {chars[1]} APPLIQUÉES       {fixed_padding}",
	f"{text_col}   888   888 Y88b888     \"Y88b. {tab_a[4]}888  Y88b {corner_col} Y {chars[1]} {insa}{insa_padding}",
	f"{text_col}   888   888  Y88888       \"888 {tab_a[5]}888   Y88b {corner_col}  {chars[1]} {char_sep * maxlen} {reset}",
	f"{text_col}   888   888   Y8888 Y88b  d88P {tab_a[6]}8888888888b {corner_col} {chars[1]} {text}{text_padding}",
	f"{text_col} 8888888 888    Y888  \"Y8888P\"  {tab_a[7]}888     Y88b {corner_col}{chars[2]}                  {fixed_padding}"
]

if len(subtitle) > 0 :
	if bar :
		padding = chars[3] + chars[4] * (logo_len - 4) + chars[5]
	else :
		padding = ' ' * (logo_len - 2)
	logo.append(f"{text_col} {padding} {reset}")
	if align == 'r' : 
		logo.append(f"{text_col} {subtitle.rjust(logo_len - 3)} {reset}")
	elif align == 'l' :
		logo.append(f"{text_col} {subtitle.ljust(logo_len - 3)} {reset}")
	else :
		left = (logo_len - 2 - len(subtitle)) // 2
		right = logo_len - 2 - len(subtitle) - left
		logo.append(f"{text_col} {' ' * left + subtitle + ' ' * right} {reset}")

if bars_col is not None :
	logo.insert(0, f"{bars_col}{chars[6] * logo_len}{reset}")
	logo.append(f"{bars_col}{chars[7] * logo_len}{reset}")

if compatibility_mode and bars_col is not None :
	print(logo_len)
	print('')
	for line in logo :
		print('  ' + line)
	print('')
else : 
	for line in logo :
		print(' ' + line)

