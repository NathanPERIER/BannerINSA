#!/usr/bin/python3
# -*- coding: utf-8 -*-
# file: bannerINSA.py
# author: Nathan PERIER
# created: 2021/03/24
# last modified: 2021/05/06
# github page: https://github.com/NathanPERIER/BannerINSA

import sys
import re


if len(sys.argv) > 1 :
	if sys.argv[1] in ['-h', '--help'] :
		print(f"usage : {sys.argv[0]} [--<insa>] [-t text] [-s subtitle] [--center | --left | --right] [-c colour] [--fill | --corner] [--bar | --sep]")
		exit(0)

i = 1


names = {'--rennes':'RENNES', '--lyon':'LYON', '--toulouse':'TOULOUSE', '--rouen':'ROUEN', '--strasbourg':'STRASBOURG', '--cvl':'CENTRE VAL DE LOIRE', '--hdf':'HAUTS-DE-FRANCE', '--euromed':'EURO-MÉDITERRANNÉE'}
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
logo_len = maxlen + 49


if i+1 < len(sys.argv) and sys.argv[i] == '-s' :
	subtitle = sys.argv[i+1]
	if len(subtitle) > logo_len - 3 : 
		subtitle = ''
	i += 2
else :
	subtitle=''


align = 'c'
if i < len(sys.argv) : 
	if sys.argv[i] in ['--center', '--left', '--right'] :
		align = sys.argv[i][2]
		i += 1


colour_codes = {'black':0, 'red':1, 'green':2, 'yellow':3, 'blue':4, 'magenta':5, 'cyan':6, 'white':7}
col_code = colour_codes['red']
palette = 2
if i+1 < len(sys.argv) and sys.argv[i] == '-c' :
	if sys.argv[i+1] in colour_codes : 
		col_code = colour_codes[sys.argv[i+1]]
	else : 
		res = re.fullmatch(r'8bit-(\d{1,3})', sys.argv[i+1])
		temp_col = int(res.group(1)) if res != None else 0
		if temp_col > 0 and temp_col < 256 :
			col_code = temp_col
			palette = 8
	i += 2

text_col = f"[1;3{col_code}m" if palette == 2 else f"[38;5;{col_code}m"
corner_col = ''
reset = '[0m'


fill = False
if i < len(sys.argv) :
	if sys.argv[i] == '--fill' :
		fill = True
		if palette == 2 : 
			bars_col = f"[0;3{col_code}m"
			text_col = f"[1;4{col_code}m"
			if col_code == 7 :
				text_col += '[1;30m'
		else : 
			bars_col = text_col
			text_col = f"[48;5;{col_code}m"
		i += 1
	elif sys.argv[i] == '--corner' :
		corner_col = '[1;30m'
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



if fill :
	padding = '▄' * (maxlen - 16 + nb_a * 13) + reset
	print(f" {bars_col}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{padding}")
padding = ' ' * (maxlen - 16) + reset
print(f" {text_col} 8888888 888b    888  .d8888b.  {tab_a[0]}8888b {corner_col} Y8888 ╻                  {padding}")
print(f" {text_col}   888   8888b   888 d88P  Y88b {tab_a[1]}88888b {corner_col} Y888 ┃ INSTITUT NATIONAL{padding}")
print(f" {text_col}   888   88888b  888 Y88b.      {tab_a[2]}888Y88b {corner_col} Y88 ┃ DES SCIENCES     {padding}")
print(f" {text_col}   888   888Y88b 888  \"Y888b.   {tab_a[3]}888 Y88b {corner_col} Y8 ┃ APPLIQUÉES       {padding}")
temp = padding
padding = ' ' * (maxlen - len(insa) + 1) + reset
print(f" {text_col}   888   888 Y88b888     \"Y88b. {tab_a[4]}888  Y88b {corner_col} Y ┃ {insa}{padding}")
print(f" {text_col}   888   888  Y88888       \"888 {tab_a[5]}888   Y88b {corner_col}  ┃ {char_sep * maxlen} {reset}")
padding = ' ' * (maxlen - len(text) + 1) + reset
print(f" {text_col}   888   888   Y8888 Y88b  d88P {tab_a[6]}8888888888b {corner_col} ┃ {text}{padding}")
padding = temp
print(f" {text_col} 8888888 888    Y888  \"Y8888P\"  {tab_a[7]}888     Y88b {corner_col}╹                  {padding}")
if len(subtitle) > 0 :
	if bar :
		padding = '╶' + '─' * (logo_len - 5) + '╴'
	else :
		padding = ' ' * (logo_len - 3)
	print(f" {text_col} {padding} {reset}")
	if align == 'r' : 
		print(f" {text_col} {subtitle.rjust(logo_len - 3)} {reset}")
	elif align == 'l' :
		print(f" {text_col} {subtitle.ljust(logo_len - 3)} {reset}")
	else :
		left = (logo_len - 3 - len(subtitle)) // 2
		right = logo_len - 3 - len(subtitle) - left
		print(f" {text_col} {' ' * left + subtitle + ' ' * right} {reset}")
if fill :
	padding = '▀' * (maxlen - 16 + nb_a * 13) + reset
	print(f" {bars_col}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{padding}")



