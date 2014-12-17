# -*- coding: utf-8 -*-

def getArrays():

  across_answers = [
    [ 1, "Astrolabio" ],
    [ 6, "Alud" ],
    [ 10, "Cinta" ],
    [ 11, "Cofradias" ],
    [ 12, "Toston" ],
    [ 13, "Amansado" ],
    [ 15, "Tabaco" ],
    [ 16, "Ase" ],
    [ 20, "Rap" ],
    [ 22, "Oscura" ],
    [ 27, "Evaporar" ],
    [ 28, "Caribe" ],
    [ 30, "Recondito" ],
    [ 31, "Libia" ],
    [ 32, "Soez" ],
    [ 33, "Intrinseca" ]
  ]

  down_answers = [
    [ 1, "Asceta" ],
    [ 2, "Tenistas" ],
    [ 3, "Oradora" ],
    [ 4, "Asco" ],
    [ 5, "Infame" ],
    [ 7, "Loinas" ],
    [ 8, "Discolos" ],
    [ 9, "Faunos" ],
    [ 14, "Col" ],
    [ 17, "Orfebres" ],
    [ 18, "Sor" ],
    [ 19, "Urdimbre" ],
    [ 21, "Adorno" ],
    [ 23, "Charlan" ],
    [ 24, "Parche" ],
    [ 25, "Camion" ],
    [ 26, "Semana" ],
    [ 29, "Loor" ]
  ]

  answers = [across_answers, down_answers]

  #position, startx, starty
  coords = [
    [ 1, 1  ],
    [ 3, 1 ],
    [ 5, 1 ],
    [ 7, 1 ],
    [ 9, 1 ],
    [ 12, 1 ],
    [ 13, 1 ],
    [ 15, 1 ],
    [ 11, 2 ],
    [ 1, 3 ],
    [ 7, 3 ],
    [ 1, 5 ],
    [ 8, 5 ],
    [ 7, 6 ],
    [ 2, 7 ],
    [ 10, 7 ],
    [ 1, 8 ],
    [ 9, 8 ],
    [ 13, 8 ],
    [ 4, 9 ],
    [ 5, 9 ],
    [ 9, 9 ],
    [ 11, 9 ],
    [ 3, 10 ],
    [ 7, 10 ],
    [ 15, 10 ],
    [ 1, 11 ],
    [ 10, 11 ],
    [ 9, 12 ],
    [ 1, 13 ],
    [ 11, 13 ],
    [ 1, 15 ],
    [ 6, 15 ]
  ]

  across_clues = [
    [ 1, "Sextante revela estrella con morro (10)" ],
    [ 6, "Derrumbe de bienestar al perder la cabeza (4)" ],
    [ 10, "Compromiso con Polo resulta en cordón (5)" ],
    [ 11, "Hermandades de tocados circumnavegan bahía interminable (9)" ],
    [ 12, "Esconde sus cantos, tonadas – qué fastidio! (6)" ],
    [ 13, "Hombre inglés en barbacoa queda domesticado (8)" ],
    [ 15, "Se fuma palo que incluye a las primeras (6)" ],
    [ 16, "Aquella volvió y la cociné (3)" ],
    [ 20, "Dos regresan con música moderna (3)" ],
    [ 22, "Negra se alivia después de aplicar puntos (6)" ],
    [ 27, "Vaporizar a la primera mujer con fósforo y rezar (8)" ],
    [ 28, "En ese mar hay espacio para incluir a la mitad de Bari! (6)" ],
    [ 30, "Lejano cerdito no revienta (9)" ],
    [ 31, "Bebe con uno en país africano (5)" ],
    [ 32, "Grosero suena a seso magullado (4)" ],
    [ 33, "Esencial y de moda esa tonada interminable y marchita (10)" ]
  ]

  down_clues = [
    [ 1, "Mástil con carbón y punto para ermitaño (6)" ],
    [ 2, "Deportistas con las cabezas llenas de nitrógeno singular (8)" ],
    [ 3, "Reza, mujer! Qué charlatana! (7)" ],
    [ 4, "Esa cosa podrida me lo produce! (4)" ],
    [ 5, "Ni me enloquezca alrededor de esa nota, depravado! (6)" ],
    [ 7, "Con telas atrapa uno de esos peces de río (6)" ],
    [ 8, "Astro se remonta bajo anillo de rebeldes (8)" ],
    [ 9, "Nota ciertos personajes mitológicos (6)" ],
    [ 14, "Casi demente sube con la de bruselas (3)" ],
    [ 17, "Joyeros de febreros fragorosos (8)" ],
    [ 18, "Monja devuelve flor interminable (3)" ],
    [ 19, "Tejido de ciudad sumeria, cuéntame, con bromo? (8)" ],
    [ 21, "Arreglo de amo rondando el norte (6)" ],
    [ 23, "Conversan sobre gases que circundan alar derruido (7)" ],
    [ 24, "Remiendo de duo revolucionario (6)" ],
    [ 25, "A mí, con estrellar ese furgón (6)" ],
    [ 26, "Surge bajo punto a los 7 días (6)" ],
    [ 29, "Elogio de olor nauseabundo (4)" ]
  ]

  clues = [across_clues, down_clues]

  return answers, coords, clues
