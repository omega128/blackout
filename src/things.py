# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# FILENAME	things.py
# AUTHOR	Kristopher Chambers
# UPDATED	2015-05-03
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# PURPOSE	This module handles the various things in the pizzeria.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import bots
import player

class Thing:
  """ stores information about a particular thing, whether it's a cupcake, a robot, a phantasm, etc. """
  def __init__ (self, title, short_description, long_description, location, tags):
    self.title = title
    self.short_description = short_description
    self.long_description = long_description
    self.location = location
    self.tags = tags

# And here's the list of every Thing in the game:
thingsById = {
  # now, some FAN service! geddit? *crickets chirp*
  "fan": Thing("fan", "A silent fan is here.", "Bereft of power, the fan is silent.", "OFFICE", ['moveable']),
  "uniform": Thing("uniform", "A purple security uniform is here.", "It's a purple uniform with 'security' on the back. It looks very snappy.", "WORN", ['moveable', 'wearable']),

  # these are the various items you'll need in-game
  "cupcake": Thing("cupcake", "A cupcake with eyes is here.",
  "The cupcake is large and bright magenta. It has a pair of large, expressive brown eyes that seem to follow you in the dim light.", "OFFICE", ['moveable']),

  "sauce": Thing("sauce", "A jar of pizza sauce is here.",
  "The jar is full of deep red marinara, with a happy italian chef on the label making a gesture that is endearing in America, and obscene in Arabia. The lid doesn't stay on very well.", "KITCHEN", ['moveable']),

  "flashlight": Thing("flashlight", "A flashlight is here.",
  "The flashlight is long and thin, with a rubber handle and a large, conspicuous switch on the side.", "CLOSET", ['moveable', 'off']),
      
  "mask": Thing("mask", "A freddy fazbear mask is here.",
  "The Freddy Fazbear mask smells of stale pizza and sweat. It's features are locked into a perpetual grin. Many employees have worn this mask over the years to entertain children.",
  "MAINTENANCE", ['moveable', 'wearable']),

  # Freddy and the gang are defined in bots.py
  "freddy1": bots.MusicalFreddy(),
  "freddy2": bots.ExitFreddy(),
  "bonnie":  bots.Bonnie(),
  "chica":   bots.Chica(),
  "foxy":    bots.Foxy(),
  }

# We also want to be able to retrieve data by name.
thingsByTitle = {}

# Since we've already defined everything by their id, we can reference that to make a dictionary.
for thingId in thingsById:
  thing = thingsById[thingId]
  thingsByTitle[thing.title] = thing

def getById (id):
  """ returns a Thing object with a given ID string """
  if id in thingsById:
    return thingsById[id]
  else:
    return None

def getByTitle (title):
  """ returns a Thing object with a given name """
  if title in thingsByTitle:
    return thingsByTitle[title]
  else:
    return None

def getByLocation (location):
  """ returns a list of Thing objects at a particular location """
  # this could be handled various ways, but the simplest way is just to query everything when we need to. If this was a larger game, I'd build a more complete database for faster lookup.
  out = []
  for key in thingsById:
    if thingsById[key].location == location:
      out.append (thingsById[key])
  return out
  