# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# FILENAME	ghosts.py
# AUTHOR	Kristopher Chambers
# UPDATED	2015-05-01
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# PURPOSE	This module handles the various spooky atmospheric effects.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import random

flavorText = ["You swear you hear a little boy laughing somewhere."
              "You hear distant carnival music.",
              "You think you see movement in the corner of your eye.",
              "You feel like you are being watched.",
              "You feel a chill.",
              "You think you see something... golden, but then it's gone.",
]

def playSpookyFlavorText():
  """ randomly add spooky noises """

  # Each turn you have a 10% of encountering a spooky noise
  if random.randint(0, 100) < 35:
    # randomly choose spooky flavor text
    print random.choice(flavorText)
    print