def generate(answers, coords, clues) :

  across_answers = answers[0]
  down_answers = answers[1]

  across_clues = clues[0]
  down_clues = clues[1]

  across_count = len(across_answers)
  down_count = len(down_answers)

  for i in xrange(across_count) :
    print('{')
    clue = across_clues[i][1]
    print("  clue: \"%s\"," % (clue))
    answer = across_answers[i][1]
    print("  answer: \"%s\"," % (answer))
    position = across_clues[i][0]
    print("  position: %d," % (position))
    print('  orientation: "across",')
    print("  startx: %d," % (coords[position-1][0]))
    print("  starty: %d," % (coords[position-1][1]))
    print('},')
  for i in xrange(down_count) :
    print('{')
    clue = down_clues[i][1]
    print("  clue: \"%s\"," % (clue))
    answer = down_answers[i][1]
    print("  answer: \"%s\"," % (answer))
    position = down_clues[i][0]
    print("  position: %d," % (position))
    print('  orientation: "down",')
    print("  startx: %d," % (coords[position-1][0]))
    print("  starty: %d," % (coords[position-1][1]))
    print('},')