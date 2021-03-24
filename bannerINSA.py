#!/usr/bin/python3
import sys


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


if i+1 < len(sys.argv) and sys.argv[i] == '-s' :
	subtitle = sys.argv[i+1]
	if len(subtitle) > maxlen + 46 : 
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
if i+1 < len(sys.argv) and sys.argv[i] == '-c' :
	if sys.argv[i+1] in colour_codes : 
		col_code = colour_codes[sys.argv[i+1]]
	i += 2

text_col = f"[1;3{col_code}m"
corner_col = ''
reset = '[0m'


fill = False
if i < len(sys.argv) :
	if sys.argv[i] == '--fill' :
		fill = True
		bars_col = f"[0;3{col_code}m"
		text_col = f"[1;4{col_code}m"
		if col_code == 7 :
			text_col += '[1;30m'
		i += 1
	elif sys.argv[i] == '--corner' :
		corner_col = '[1;30m'
		i += 1


bar=False
sep=False
if i < len(sys.argv) :
	if sys.argv[i] == '--bar' : 
		bar=True
		i += 1
	elif sys.argv[i] == '--sep' :
		sep=True
		i += 1



if fill :
	padding = '▄' * (maxlen - 16) + reset
	print(f" {bars_col}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄{padding}")
padding = ' ' * (maxlen - 16) + reset
print(f" {text_col} 8888888 888b    888  .d8888b.  8888b {corner_col} Y8888 ╻                  {padding}")
print(f" {text_col}   888   8888b   888 d88P  Y88b 88888b {corner_col} Y888 ┃ INSTITUT NATIONAL{padding}")
print(f" {text_col}   888   88888b  888 Y88b.      888Y88b {corner_col} Y88 ┃ DES SCIENCES     {padding}")
print(f" {text_col}   888   888Y88b 888  \"Y888b.   888 Y88b {corner_col} Y8 ┃ APPLIQUÉES       {padding}")
temp = padding
padding = ' ' * (maxlen - len(insa) + 1) + reset
print(f" {text_col}   888   888 Y88b888     \"Y88b. 888  Y88b {corner_col} Y ┃ {insa}{padding}")
padding = temp
if sep :
	print(f" {text_col}   888   888  Y88888       \"888 888   Y88b {corner_col}  ┃ {'=' * maxlen} {reset}")
else : 
	print(f" {text_col}   888   888  Y88888       \"888 888   Y88b {corner_col}  ┃                  {padding}")
temp = padding
padding = ' ' * (maxlen - len(text) + 1) + reset
print(f" {text_col}   888   888   Y8888 Y88b  d88P 8888888888b {corner_col} ┃ {text}{padding}")
padding = temp
print(f" {text_col} 8888888 888    Y888  \"Y8888P\"  888     Y88b {corner_col}╹                  {padding}")
if len(subtitle) > 0 :
	if bar :
		padding = '╶' + '─' * (maxlen + 44) + '╴'
	else :
		padding = ' ' * (maxlen + 46)
	print(f" {text_col} {padding} {reset}")
	if align == 'r' : 
		print(f" {text_col} {subtitle.rjust(maxlen + 46)} {reset}")
	elif align == 'l' :
		print(f" {text_col} {subtitle.ljust(maxlen + 46)} {reset}")
	else :
		left = (maxlen + 46 - len(subtitle)) // 2
		right = maxlen + 46 - len(subtitle) - left
		print(f" {text_col} {' ' * left + subtitle + ' ' * right} {reset}")
if fill :
	padding = '▀' * (maxlen - 16) + reset
	print(f" {bars_col}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀{padding}")



