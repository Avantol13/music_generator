#!/bin/bash
################################################################################
#  ___  ___          _        _____                           _                #
#  |  \/  |         (_)      |  __ \                         | |               #
#  | .  . |_   _ ___ _  ___  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __    #
#  | |\/| | | | / __| |/ __| | | __ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|   #
#  | |  | | |_| \__ \ | (__  | |_\ \  __/ | | |  __/ | | (_| | || (_) | |      #
#  \_|  |_/\__,_|___/_|\___|  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|      #
################################################################################
# Generate midi, pdf, and Python pkl file by using a probability (style) file,
# output path, composition name, key, and number of bars to generate for a
# melody and chord track.

################################ CONFIGURATION #################################
# Path to Python installation
PYTHON_PATH=python

# The name for your composition (included in some of the generated files)
COMPOSITION_NAME="EXAMPLE"

# Force the musical key. Can use # and b for sharp and flat. Use lowercase
# for minor keys and UPPERCASE for major keys
FORCE_KEY="G"

# Number of bars for different tracks. If not specified, will default to 8
MELODY_TRACK_BARS=4
CHORDS_TRACK_BARS=4

# Amount of times to repeat the above generated tracks
REPEAT_TRACKS=1

# Which bar to start generating at
START_BAR=1

# Path to the "Style", you can create your own following the same format as
# those in the "styles" folder
STYLE_FILE_PATH="styles/default.json"

# Path to the main script
MUSIC_GENERATOR_CLI="mgen_cli.py"

# -- Different options for file output paths below -- #
# Default directory and name (if no argument specified)
PKL_OUTPUT_PATH=
# Default name, specific directory
# NOTE: Don't use relative paths, put / at end
MIDI_OUTPUT_PATH="/var/tmp/music_generator/"
# Specific directory and filename
# NOTE: Don't use relative paths
PDF_OUTPUT_PATH="/var/tmp/music_generator/example"

################################## EXECUTION ###################################
$PYTHON_PATH $MUSIC_GENERATOR_CLI --style_file_path $STYLE_FILE_PATH \
 --melody_track $MELODY_TRACK_BARS --chords_track $CHORDS_TRACK_BARS \
 --repeat_tracks $REPEAT_TRACKS --start_bar $START_BAR               \
 --composition_name $COMPOSITION_NAME --key $FORCE_KEY               \
 --generate_midi $MIDI_OUTPUT_PATH --generate_pdf $PDF_OUTPUT_PATH   \
 --generate_pickle $PKL_OUTPUT_PATH