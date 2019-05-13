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
sets = []
#
#
def main():
    stats_import()
#
#
def stats_import():
    input_file = csv.DictReader(open("test"))
    for row in input_file:
        sets.append(row)
    print(*sets, sep = "\n")
#
#
def D_calc():
    '''
    D: INT-adjusted Base Damage

    Definition of Variables

    * V: Every individual damage-dealing magic spell has a base damage value denoted as V.
    * dINT: dINT represents the difference between caster and target INT: (Caster's INT - Target's INT).
    * M: Every individual damage-dealing magic spell has several INT multiplier values denoted as M for different dINT ranges.
        Note: For offensive white magic, substitute dMND for dINT (Caster's MND - Target's MND)
    * mDMG: mDMG represents the "Magic Damage" statistic obtained from equipped weapons and armor.
    * D: INT and "Magic Damage" adjusted base spell damage calculated from the terms above.

    Calculating D
    D = mDMG + V + (dINT * M)
    
    The calculation of D is a piecewise function with the multiplier M changing at the following INT levels:
    dINT = 0 ~ 49
    dINT = 50 ~ 99
    dINT = 100 ~ 199
    dINT > 200
    When determining D, the appropriate V and M values must be applied depending on the INT difference. For example,
    with dINT = 134, V100 should be chosen for the base damage, and the M which corresponds to dINT = 100 ~ 199 should
    be chosen as the multiplier. When choosing a V value, reduce the dINT by the amount factored into the V value to
    come up with the correct result (for example, at 134 INT, when using V100 in the calculation, use dINT = 134-100 = 34)
    dINT = 134: D = mDMG + V100 + (34 * M100-199)

    Reference:  https://www.bg-wiki.com/bg/Magic_Damage#Calculating_D
    
    '''
    print()

#
#
if __name__ == "__main__":
    main()
                    
