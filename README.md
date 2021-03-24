# BannerINSA

This is a script that serves the only purpose of displaying the INSA logo (e.g. when you launch a new terminal). 

The script is best effort, therefore it will (~~should~~) never print an error message in the console. If a parameter is invalid, the default value will be used instead. 

![Example of what the script can display](preview/banner.png)


# How to use the script

```Bash
bannerINSA.sh [--<insa>] [-t text] [-s subtitle] [--center | --left | --right] 
		[-c colour] [--fill | --corner] [--bar | --sep]
```

* `--<insa>` : replace `<insa>` with the name of the desired school. Options are `lyon`, `rennes`,`rouen`, `toulouse`, `strasbourg`, `cvl`, `hdf` and `euromed`, default is `rennes`.

![Script with the name of the INSA Lyon](preview/banner-school.png)

* `-t text` : displays the text at the right of the logo, under the name of the school. This is not meant for displaying big texts or mutiline text.

![Script with the text "Hello"](preview/banner-text.png)

* `-s subtitle` : displays the subtitle under the INSA logo. The subtitle has to be shorter than the length of the logo and should not contain any line return (this may be changed in the future).

![Script with the subtitle "Subtitle"](preview/banner-subtitle-center.png)

* `--center | --left | --right` : determines the alignement of the subtitle with regards to the INSA logo, default is `--center`

![left-aligned subtitle](preview/banner-subtitle-left.png)
![right-aligned subtitle](preview/banner-subtitle-right.png)

* `-c colour` : determines the colour of the logo, options are `white`, `red`, `yellow`, `green`, `blue`, `magenta`, `cyan` and `black`, default is `red`. Note that the colour provided represents one of the 8 colours supported by basically any terminal, hence you may obtain a colour that doesn't match the option in the command depending on your terminal's theme, specifically if you use a light theme (which has not been tested).

![magenta-coloured logo](preview/banner-colour.png)

* `--fill` : with this option, the colour is applied to the background and the logo is displayed in white. This is achieved by using [special characters](https://en.wikipedia.org/wiki/Box-drawing_character) that may not be rendered as intended depending on the terminal you use.

![filled banner](preview/banner-fill.png)

* `--corner` : displays the corner of the logo in gray like in the original logo. This option is mutually exclusive with `--fill`.

![banner with a corner](preview/banner-corner.png)

* `--bar` : displays a thin bar between the logo and the subtitle if there is one.

![banner with a bar](preview/banner-bar.png)

* `--sep` : displays a separator between the name of the school and the text. This option is mutually exclusive with `--bar` because they look horrendous together.

![banner with a separator](preview/banner-sep.png)


# Assets


***TODO***

:pancakes:

