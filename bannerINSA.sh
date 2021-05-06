#!/bin/bash
# encoding: UTF-8
# file: bannerINSA.sh
# author: Nathan PERIER
# created: 2021/03/12
# last modified: 2021/05/05
# github page: https://github.com/NathanPERIER/BannerINSA

rep () {
	if [ $2 -ge 1 ]
	then
		printf "$1%.0s" $(eval "echo {1..$(($2))}")
	fi
}


if [ $# -ge 1 ] 
then
	if [ $1 = '-h' ] || [ $1 = '--help' ]
	then
		echo "usage : $0 [--<insa>] [-t text] [-s subtitle] [--center | --left | --right] [-c colour] [--fill | --corner] [--bar | --sep]"
		exit 0
	fi
fi


insa='RENNES'
if [ $# -ge 1 ]
then
	case "$1" in
		'--rennes') shift ;;
		'--lyon') insa='LYON' ; shift ;;
		'--toulouse') insa='TOULOUSE' ; shift ;;
		'--rouen') insa='ROUEN' ; shift ;;
		'--strasbourg') insa='STRASBOURG' ; shift ;;
		'--cvl') insa='CENTRE VAL DE LOIRE' ; shift ;;
		'--hdf') insa='HAUTS-DE-FRANCE' ; shift ;;
		'--euromed') insa='EURO-MÉDITERRANNÉE' ; shift ;;
	esac
fi 

insa_len=${#insa}
maxlen=$( (( $insa_len > 17 )) && echo "$insa_len" || echo '17' )

if [ $# -ge 2 ] && [ $1 = '-t' ]
then 
	text="$2"
	textlen=${#text}
	shift 2
else 
	text=""
	textlen=0
fi

maxlen=$( (( $textlen > $maxlen )) && echo "$textlen" || echo "$maxlen" )

if [ $# -ge 2 ] && [ $1 = '-s' ]
then 
	subtitle="$2"
	subtitlelen=${#2}
	align='c'
	if [ $subtitlelen -gt $((maxlen + 46)) ]
	then
		subtitlelen=0
	fi
	shift 2
else 
	subtitlelen=0
fi

if [ $# -ge 1 ]
then
	if [ $1 = '--center' ] || [ $1 = '--left' ] || [ $1 = '--right' ]
	then
		align=$(echo "$1" | head -c 3 | tail -c 1)
		shift
	fi
fi

if [ $# -ge 2 ] && [ $1 = '-c' ]
then
	palette=2
	case $2 in 
		'black') col_code=0 ;;
		'green') col_code=2 ;;
		'yellow') col_code=3 ;;
		'blue') col_code=4 ;;
		'magenta') col_code=5 ;;
		'cyan') col_code=6 ;;
		'white') col_code=7 ;;
		'8bit-'*) col_code=${2#*-}; if [[ "$col_code" =~ [0-9]{1,3} ]] && [[ $col_code -lt 256 ]]; then palette=8; else col_code=1; fi;;
		*) col_code=1 ;;		# Red is default
	esac
	shift 2
else
	col_code=1
fi

if [[ $palette -eq 2 ]]; then
	text_col="[1;3${col_code}m"
else 
	text_col="[38;5;${col_code}m"
fi
reset='[0m'
corner_col=''

fill='false'
if [ $# -ge 1 ]
then 
	if [ $1 = '--fill' ]
	then
		fill='true'
		if [[ $palette -eq 2 ]]; then
			bars_col="[0;3${col_code}m"
			text_col="[1;4${col_code}m"
			if [ "$col_code" = '7' ]
			then
				text_col="${text_col}[1;30m"
			fi
		else
			bars_col="$text_col"
			text_col="[48;5;${col_code}m"
		fi
		shift
	elif [ $1 = '--corner' ]
	then 
		corner_col='[1;30m'
		shift
	fi	
fi

bar='false'
sep='false'
if [ $# -ge 1 ]
then
	if [ $1 = '--bar' ]
	then
		bar='true'
		shift
	elif [ $1 = '--sep' ]
	then
		sep='true'
		shift
	fi
fi



if [ $fill = 'true' ]
then
	padding=$(rep '▄' $((maxlen - 16)))"$reset"
	echo " ${bars_col}▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄$padding"
fi
padding=$(rep ' ' $((maxlen - 16)))"$reset"
echo " $text_col 8888888 888b    888  .d8888b.  8888b $corner_col Y8888 ╻                  $padding"
echo " $text_col   888   8888b   888 d88P  Y88b 88888b $corner_col Y888 ┃ INSTITUT NATIONAL$padding"
echo " $text_col   888   88888b  888 Y88b.      888Y88b $corner_col Y88 ┃ DES SCIENCES     $padding"
echo " $text_col   888   888Y88b 888  \"Y888b.   888 Y88b $corner_col Y8 ┃ APPLIQUÉES       $padding"
temp="$padding"
padding=$(rep ' ' $((maxlen - insa_len + 1)))"$reset"
echo " $text_col   888   888 Y88b888     \"Y88b. 888  Y88b $corner_col Y ┃ ${insa}${padding}"
padding="$temp"
if [ $sep = 'true' ] 
then 
	echo " $text_col   888   888  Y88888       \"888 888   Y88b $corner_col  ┃ $(rep '=' $maxlen) $reset"
else
	echo " $text_col   888   888  Y88888       \"888 888   Y88b $corner_col  ┃                  $padding"
fi
temp=$padding
padding=$(rep ' ' $((maxlen - textlen + 1)))"$reset"
echo " $text_col   888   888   Y8888 Y88b  d88P 8888888888b $corner_col ┃ ${text}${padding}"
padding=$temp
echo " $text_col 8888888 888    Y888  \"Y8888P\"  888     Y88b $corner_col╹                  $padding"
if [ $subtitlelen -gt 0 ]
then
	if [ $bar = 'true' ] ; then 
		padding='╶'$(rep '─' $((maxlen + 44)))'╴'
	else 
		padding=$(rep ' ' $((maxlen + 46)))
	fi
	echo " $text_col $padding $reset"
	if [ $align = 'r' ] ; then
		left=$(( maxlen + 46 - subtitlelen ))
		right=0
	elif [ $align = 'l' ] ; then
		left=0
		right=$(( maxlen + 46 - subtitlelen ))
	else
		left=$(( (maxlen + 46 - subtitlelen) / 2 ))
		right=$(( maxlen + 46 - subtitlelen - left ))
	fi
	echo " $text_col $(rep ' ' $left)${subtitle}$(rep ' ' $right) $reset"
fi
if [ $fill = 'true' ]
then
	padding=$(rep '▀' $((maxlen - 16)))"$reset"
	echo " ${bars_col}▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀$padding"
fi



#' [0;31m▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄[0m'
#' [1;41m 8888888 888b    888  .d8888b.  8888b  Y8888 ╻                   [0m'
#' [1;41m   888   8888b   888 d88P  Y88b 88888b  Y888 ┃ INSTITUT NATIONAL [0m'
#' [1;41m   888   88888b  888 Y88b.      888Y88b  Y88 ┃ DES SCIENCES      [0m'
#' [1;41m   888   888Y88b 888  "Y888b.   888 Y88b  Y8 ┃ APPLIQUÉES        [0m'
#' [1;41m   888   888 Y88b888     "Y88b. 888  Y88b  Y ┃ RENNES            [0m'
#' [1;41m   888   888  Y88888       "888 888   Y88b   ┃                   [0m'
#' [1;41m   888   888   Y8888 Y88b  d88P 8888888888b  ┃ Nathan PERIER     [0m'
#' [1;41m 8888888 888    Y888  "Y8888P"  888     Y88b ╹                   [0m'
#' [1;41m ╶─────────────────────────────────────────────────────────────╴ [0m'
#' [1;41m                           Bottom text                           [0m'
#' [0;31m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀[0m'
