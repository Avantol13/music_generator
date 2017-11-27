[![Build Status](https://travis-ci.org/Avantol13/mgen.svg?branch=master)](https://travis-ci.org/Avantol13/mgen)
[![Coverage Status](https://coveralls.io/repos/github/Avantol13/mgen/badge.svg?branch=master)](https://coveralls.io/github/Avantol13/mgen?branch=master)

# Music Generator (mgen)
 > By: Alexander VanTol

Generate randomized musical compositions based on probabilities.

## Overview

1. /mingus (not my code, see [this](https://github.com/bspaans/python-mingus))
2. /mgen (my code)
    - choice.py *||||| Makes choices based on probabilities in a style*
    - convert.py *|||| Converts my stuff to mingus stuff and vice-versa*
    - create.py *||||| The magic happens here. Contains the MusicGenerator class*
    - style.py *|||||| Contains the Style class which defines probabilities*
    - time.py *||||||| Handles note and bar musical timing math stuff*
    - config.py *||||| Configuration for mgen*
3. /styles (holds cfg files for different styles)
4. lilypond-2.18.2-1.mingw.exe (program for PDF generation)
    - This one's for Windows (works with Windows 10)
    - See [here](http://lilypond.org/download.html) for alternate downloads
5. MidiPlayW7.exe (a free midi player, see [here](http://www.chrishills.org.uk/midiplay/))

## Quickstart
There are a few scripts included to show how this can be used at the moment.

### Windows Users
Just run the .bat files in the root directory.
I've included the executables necessary in the root dir of this repo.

### Linux Users
You need a **midi player** if you want to play the resulting .mid files.
I recommend `[timidity]`(https://wiki.archlinux.org/index.php/timidity).

You can install `timidity` with:
`sudo apt-get install timidity`

Also, you'll need **[Lilypond](http://lilypond.org)** (a program for creating music notation in PDF's).
Follow the directions [here](http://lilypond.org/unix.html) to install.

## Official Documentation

> TODO: Add link to documentation

See documentation [here]().
