puzzleData generator for jweisbeck/Crossword script.js
======================================================

Put proper data in data_arrays.py
(Take a look at data_arrays.py file)

Then, run

    python input-gen.py > <path>/<filename>.txt

e.g.

    python input-gen.py > data/elcriptico/crucigrama8/crucigrama8-input.txt

File contents look like the following:

    {
      clue: "Sextante revela estrella con morro (10)",
      answer: "Astrolabio",
      position: 1,
      orientation: "across",
      startx: 1,
      starty: 1,
    },
    {
      clue: "Derrumbe de bienestar al perder la cabeza (4)",
      answer: "Alud",
      position: 6,
      orientation: "across",
      startx: 12,
      starty: 1,
    },
    ....

You can directly include this in script.js of jweisbeck/Crossword
