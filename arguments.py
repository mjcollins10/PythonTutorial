#!/usr/bin/env python
#
# Argument Parsing
#
import argparse, sys

parser = argparse.ArgumentParser(description='Demo for Jlab Python Course')

#boolean flag
parser.add_argument('--verbose',
    action='store_true',
    help='verbose flag' )

#value
parser.add_argument('--id',  type=int)#required=True

#no flag
parser.add_argument('filename')

args = parser.parse_args()

print('args.id ==', args.id)
print('args.verbose ==', args.verbose)
print('args.filename ==', args.filename)
print('sys.argv ==', sys.argv)
