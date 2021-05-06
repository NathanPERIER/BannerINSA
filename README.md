# BannerINSA

This script allows the users to display the INSA logo in a console (e.g. when you launch a new terminal).

![Example of what the script can display](preview/banner.png)

This script was originally written in Bash but I also translated it in Python for those who use other shells (like [fish](https://github.com/fish-shell/fish-shell)). It is intended as a best-effort script, therefore it will (~~should~~) never print an error message in the console. If a parameter is invalid, the default value will be used instead. 


# Motivations

I was bored lol


# How to use the script

```Bash
not@pancake:~$ ./bannerINSA.sh -h
bannerINSA.sh [--<insa>] [-t text] [-s subtitle] [--center | --left | --right] [-c colour] [--fill | --corner] [--bar | --sep]
```

* `--<insa>` : replace `<insa>` with the name of the desired school. Options are `lyon`, `rennes`,`rouen`, `toulouse`, `strasbourg`, `cvl`, `hdf` and `euromed`, default is `rennes`.

![banner with the name of the INSA Lyon](preview/banner-school.png)

* `-t text` : displays a given text at the right of the logo, under the name of the school. This is not meant for displaying big texts or mutiline text.

![banner with the text "Hello"](preview/banner-text.png)

* `-s subtitle` : displays the subtitle under the INSA logo. The subtitle has to be shorter than the length of the logo and should not contain any line return (may be changed in the future).

![banner with the subtitle "Subtitle"](preview/banner-subtitle-center.png)

* `--center | --left | --right` : determines the alignement of the subtitle with regards to the INSA logo, default is `--center`

![left-aligned subtitle](preview/banner-subtitle-left.png)
![right-aligned subtitle](preview/banner-subtitle-right.png)

* `-c colour` : determines the colour of the logo, options are `white`, `red`, `yellow`, `green`, `blue`, `magenta`, `cyan`, `black` and `8bit-<col>` where `<col>` is a number between 0 and 255 representing a colour in the [256-colour palette](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit) of your terminal. The default value is `red`. Note that rendering of the the colour may depend on the colour theme of your terminal, hence you may obtain a colour that doesn't match the name of the option. For example, if you use a light theme the `black` colour probably be light grey and the `white` colour will most likely be black. This should not affect 8-bit colours greater than or equal to 16.

![magenta-coloured logo](preview/banner-colour.png)

* `--fill` : with this option, the colour is applied to the background and the logo is displayed in white. The effect is nice because it uses [special characters](https://en.wikipedia.org/wiki/Box-drawing_character) that may not be rendered as intended on certain terminals (like Alacritty for example).

![filled banner](preview/banner-fill.png)

* `--corner` : displays the corner of the logo in gray. This option is mutually exclusive with `--fill`.

![banner with a corner](preview/banner-corner.png)

* `--bar` : displays a thin bar between the logo and the subtitle if there is one.

![banner with a bar](preview/banner-bar.png)

* `--sep` : displays a separator between the name of the school and the text. This option is mutually exclusive with `--bar`.

![banner with a separator](preview/banner-sep.png)


# Requirements

The main thing you'll need is a terminal that is able to display 8/16-colour palettes (which is the case most of the time). If you use a `8bit-sth` colour, you'll need a terminal that handles [256-colour palettes](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit).

For the Python script, you will need Python 3.6 or above because I just love f-strings and tend to put them everywhere.

For the Bash script, any recent version of Bash will do the trick but older versions should work as well (tested with bash 5.0.3 and 5.0.17).


# Assets

The terminal I use in the screenshots is gnome-terminal (the default terminal in Ubuntu). My colour profile is [Blood Moon](https://github.com/dguo/blood-moon), this theme has a pink-ish red which is why screenshots with the `--fill` option may look like they are pink/magenta.

The ASCII art text was generated using the font Colossal in a generator like [this one](https://patorjk.com/software/taag/#p=display&f=Colossal&t=INSA) (which is basically an interface running [FIGlet](http://www.figlet.org/)), I then modified the 'A' just a bit to mimic the INSA logo.


:pancakes:

