#!/usr/bin/python3
#
####################################
#
# Magic Damage Calculation Tool
#
####################################
#
import argparse
import math
import csv
#
#
def main():
    input_file = csv.DictReader(open("test"))
        for row in input_file:
                print(row)
                #
                #
                if __name__ == "__main__":
                    main()
                    
