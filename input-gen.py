# -*- coding: utf-8 -*-

# Input generator for jweisbeck/Crossword

import data_arrays as DA

answers, coords, clues = DA.getArrays()

import generator as GEN

GEN.generate(answers, coords, clues)
