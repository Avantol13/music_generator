#!/usr/bin/python2
'''
Created on Jan 21, 2016

@author: Alexander VanTol
'''

# Project Modules
import mgen
import sys
import argparse
from colorama import init
from colorama import Fore
from colorama import Style as ColoramaStyle
import traceback
import os

def main():
    # Initialize colorama colored command line output
    init()

    my_generator = None

    # Parse arguments into script. Note that 1st argument is script name
    args = parse_args(sys.argv[1:])

    # If we don't want output, ignore all print statements
    if args.silent:
        # Redirect print output to null device on operating system
        print_redirect = open(os.devnull, 'w')
        sys.stdout = print_redirect

    print_header()

    # Use provided StyleProbs or use default
    if args.style_file_path:
        try:
            my_style = mgen.StyleProbs(args.style_file_path)
        except IOError:
            print_error('Couldn\'t find ' + args.style_file_path)
    else:
        my_style = mgen.StyleProbs(mgen.DEFAULT_CFG_FILE)

    # Load MusicGenerator object is specified, otherwise create a new one
    if args.load_pickle:
        try:
            my_generator = mgen.MusicGenerator.from_pickle(args.load_pickle)
            # Force style if provided
            if args.style_file_path:
                my_generator.style = my_style
        except IOError:
            print_error('Couldn\'t find ' + args.load_pickle)
    else:
        my_generator = mgen.MusicGenerator(my_style, composition_title=args.composition_name)

    # Force musical key if provided
    if args.key:
        my_generator.set_key(args.key)

    if args.melody_track:
        if args.repeat_tracks:
            my_generator.add_melody_track(style=my_style,
                                          location_to_add=args.start_bar,
                                          num_bars=args.melody_track,
                                          times_to_repeat=args.repeat_tracks)
        else:
            my_generator.add_melody_track(style=my_style, location_to_add=args.start_bar,
                                          num_bars=args.melody_track)

    if args.chords_track:
        if args.repeat_tracks:
            my_generator.add_chords_track(style=my_style,
                                          location_to_add=args.start_bar,
                                          num_bars=args.melody_track,
                                          times_to_repeat=args.repeat_tracks,
                                          octave_adjust=-1)
        else:
            my_generator.add_chords_track(style=my_style, location_to_add=args.start_bar,
                                          num_bars=args.melody_track,
                                          octave_adjust=-1)

    # File exports
    if args.generate_pickle:
        export_location = my_generator.export_pickle(args.generate_pickle)
        print('Generated PKL file: ' + Fore.GREEN + export_location + Fore.RESET)
    if args.generate_pdf:
        export_location = my_generator.export_pdf(args.generate_pdf)
        print('Generated PDF file: ' + Fore.GREEN + export_location + Fore.RESET)
    if args.generate_midi:
        export_location = my_generator.export_midi(args.generate_midi, args.beats_per_minute)
        print('Generated MIDI file: ' + Fore.GREEN + export_location + Fore.RESET)

    print('\n' + str(my_generator))
    print_footer()

def parse_args(args):
    """
    Returns parsed and validated arguments that were passed into the script.

    :param args: The arguments passed into the script
    """
    # Parse arguments from command line
    # NOTE: nargs=? allows 0 or 1 argument. If unspecified, will use default
    parser = argparse.ArgumentParser(description='Music Generator: ' +
                                     'Generate randomized musical ' +
                                     'compositions based on probabilities.')
    parser.add_argument('-mt', '--melody_track', metavar='NUM_BARS_TO_GEN',
                        help='Adds a melody track to the composition.',
                        nargs='?', const=8, type=int, default=None)
    parser.add_argument('-ct', '--chords_track', metavar='NUM_BARS_TO_GEN',
                        help='Adds a chords track to the composition.',
                        nargs='?', const=8, type=int, default=None)
    parser.add_argument('-sb', '--start_bar', type=int,
                        help='Bar in the composition to add the tracks to. ' +
                        ' For example, --start_bar 9 will generate tracks ' +
                        'beginning at the 9th bar.',
                        nargs='?', default=0)
    parser.add_argument('-r', '--repeat_tracks', type=int,
                        help='Will repeat the specified tracks the amount ' +
                        'of times specified.',
                        nargs='?', const=1, default=None)

    parser.add_argument('-c', '--composition_name',
                        help='Name to associate with the generated composition.',
                        nargs='?', default='Untitled')
    parser.add_argument('-k', '--key',
                        help='Forces the musical key. Use lower case for ' +
                        'minor keys, b for flat, and # for sharp')

    parser.add_argument('-midi', '--generate_midi', metavar='MIDI_OUTPUT_PATH',
                        help='Generates the composition as a MIDI file',
                        nargs='?', const=mgen.config._PATH_TO_SCRIPT + '/../output/', default=None)

    parser.add_argument('-pdf', '--generate_pdf', metavar='PDF_OUTPUT_PATH',
                        help='Generates the musical score as a PDF file',
                        nargs='?', const=mgen.config._PATH_TO_SCRIPT + '/../output/', default=None)

    parser.add_argument('-pkl', '--generate_pickle', metavar='PKL_OUTPUT_PATH',
                        help='Generates the MusicGenerator object as a .pkl ' +
                        '(reimportable Python object) file',
                        nargs='?', const=mgen.config._PATH_TO_SCRIPT + '/../output/', default=None)

    parser.add_argument('-st', '--style_file_path', metavar='STYLE_FILE_PATH',
                        help='Path to musical probabilities configuration file,' +
                        ' if not provided, will use default style.')

    parser.add_argument('-l', '--load_pickle', metavar='PKL_FILE_PATH',
                        help='Load a MusicGenerator previously saved as' +
                        ' a .pkl file.')

    parser.add_argument('-bpm', '--beats_per_minute',
                        help='Beats per minute for midi output.',
                        nargs='?', default=90, type=int)

    parser.add_argument('-s', '--silent', help='Silence printing information to command window',
                        action='store_true')

    return parser.parse_args()

def print_header():
    """
    Print header of tool into command line.
    """
    print(ColoramaStyle.BRIGHT + '\n--------------------------------------------------' +
          '------------------------------')
    print('   MUSIC GENERATOR')
    print('-------------------------------------------------------------------' +
          '-------------\n' + ColoramaStyle.RESET_ALL)

def print_footer():
    """
    Print footer of tool into command line.
    """
    print(ColoramaStyle.BRIGHT + '\n--------------------------------------------------' +
          '------------------------------')
    print('   END')
    print('-------------------------------------------------------------------' +
          '-------------\n' + ColoramaStyle.RESET_ALL)

def print_error(error=None):
    """
    Print an error into command line with traceback.

    :param error: Optional string to print before traceback
    """
    print(Fore.RED + ColoramaStyle.BRIGHT + '!!!--------------------------------------' +
          '------------------------------------!!!\n')

    if error is not None:
        print(error + '\n')

    traceback.print_exc()

    print('\n!!!--------------------------------------------------------------' +
          '------------!!!' + ColoramaStyle.RESET_ALL + '\n')

if __name__ == '__main__':
    main()
