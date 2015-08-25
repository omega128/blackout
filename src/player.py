# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# FILENAME	player.py
# AUTHOR	Kristopher Chambers
# UPDATED	2015-05-01
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# PURPOSE	This module handles the player, as well as each action the player can take
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from dirs import *

import places
import things

# the player always starts in the security office.
location = "OFFICE"

def look ():
  """ makes the player look at the current room """
  global location
  here = places.getById(location)
  
  # Where are we? Show this place's title and description:
  print " - " + here.title + " -"
  print here.description
  print
  
  # display any Things in the area, unless they're hidden.
  thingsHere = [thing for thing in things.getByLocation(location) if "hidden" not in thing.tags] # <-- list comprehension! one of many ways python is awesome
  if len(thingsHere) > 0:
    for thing in thingsHere:
        print "  " + thing.short_description
    print

def go (direction):
  """ makes the player move in a given direction. """
  global location
  here = places.getById(location)
  
  # complain if we can't go that way.
  if direction not in here.exits:
    print "You cannot go that way!"
    print
    return
    
  # Foxy only comes out if the player visits the closet.
  if location == 'CLOSET':
    things.getById('foxy').location = 'WEST HALLWAY'
      
  # if foxy is sprinting at you but there isn't any sauce, you cannot move fast enough to leave.
  if location == things.getById('foxy').location and 'mangled' not in things.getById('foxy').tags:
    print "You cannot move fast enough."
    print
    return
  
  # move us over that-a-ways!
  print "You go " + direction + "."
  print
  location = here.exits[direction]
  
def take (chosenThing):
  """ makes the player pick up something nearby. """
  global location
  
  # does this thing exist?
  thing = things.getByTitle (chosenThing)
  if not thing:
    print "You cannot do that."
    print
    return

  # is it both here, AND moveable?
  if thing.location == location and "moveable" in thing.tags:
    thing.location = "INVENTORY"
    print "You take the", chosenThing
    print
    return
  else:
    print "You cannot do that."
    print
    return
  
  
def showInventory ():
  """ lists everything the player is carrying, and everything they are wearing. """
  global location
  
  # show a list of everything you have
  print "You have: "
  for thing in things.getByLocation("INVENTORY"):
    print thing.title,
    
    # We want to let the player know if the flashlight is on
    if "on" in thing.tags:
      print "(on)"
    else:
      print
      
  print

  # show anything you're wearing
  print "You are wearing: "
  for thing in things.getByLocation("WORN"):
    print thing.title
    
  print
  
def examine (chosenThing):
  """ makes the player examine something nearby. """
  global location
  
  # does this thing exist?
  thing = things.getByTitle (chosenThing)
  if not thing:
    print "You cannot do that."
    print
    return
    
  # to examine a thing it must either be in the room, in your inventory, or worn, and it must not be hidden
  if thing.location in [location, 'INVENTORY', 'WORN'] and "hidden" not in thing.tags:
    print thing.long_description
    print
  else:
    print "You cannot do that."
    print
    return   

def drop (chosenThing):
  """ makes the player drop something they are carrying. """
  global location
  
  # does this thing exist?
  thing = things.getByTitle (chosenThing)
  if not thing:
    print "You cannot do that."
    print
    return
  
  # we can only drop an item that is in our inventory, or that is currently worn.
  if thing.location in ['INVENTORY', 'WORN']:
    thing.location = location
    print "You drop the", thing.title
    print
  else:
    print "You cannot do that."
    print
    return   

def wear (chosenThing):
  """ makes the player wear something. """
  global location
  
  # does this thing exist?
  thing = things.getByTitle (chosenThing)
  if not thing:
    print "You cannot do that."
    print
    return

  # we can only wear an item that is in the current room, or in the inventory, and it has to be wearable
  if thing.location in [location, 'INVENTORY'] and "wearable" in thing.tags:
    thing.location = "WORN"
    print "You wear the", thing.title
    print
  
  # wait, are you already wearing it?
  elif thing.location == 'WORN':
    print "You are already wearing the", thing.title
    print  
  else:
    print "You cannot do that."
    print
  
  
def unwear (chosenThing):
  """ makes the player remove something they are wearing. """
  global location
  
  # does this thing exist?
  thing = things.getByTitle (chosenThing)
  if not thing:
    print "You cannot do that."
    return

  # we can only unwear an item that we are wearing.
  if thing.location == 'WORN':
    thing.location = "INVENTORY"
    print "You remove the", thing.title
    print
  else:
    print "You cannot do that."
    
def turnOn (chosenThing):
  """ makes the player turn something on. """
  global location
  
  # does this thing exist?
  thing = things.getByTitle (chosenThing)
  if not thing:
    print "You cannot do that."
    return
    
  # we can only turn on a thing that we are carrying.
  if thing.location in [location, 'INVENTORY'] and "off" in thing.tags:
    thing.tags.remove ("off")
    thing.tags.append ("on")
    print "You turn on the", thing.title
    print
  else:
    print "You cannot do that."
    print

def turnOff (chosenThing):
  """ makes the player turn something off. """
  global location
  
  # does this thing exist?
  thing = things.getByTitle (chosenThing)
  if not thing:
    print "You cannot do that."
    return
    
  # we can only turn off an item that is nearby.
  if thing.location in [location, 'INVENTORY'] and "on" in thing.tags:
    thing.tags.remove ("on")
    thing.tags.append ("off")
    print "You turn off the", thing.title
    print
    return
  
  else:
    # The thing wasn't here.
    print "You cannot do that."
    print

def throw (chosenThing):
  """ makes the player throw something. """
  global location
   
  # verify the thing exists
  thing = things.getByTitle (chosenThing)
  if not thing:
    print "You cannot do that."
    print
    return
  
  if thing.location in [location, 'INVENTORY'] and "moveable" in thing.tags:
    
    # The only objects that have special rules for throwing is the sauce. Everything else is treated as though you dropped it.
    if chosenThing == 'sauce':
      print "You throw the jar of sauce. It breaks open, spattering thick, dark red liquid everywhere."
      
      # Now, the sauce is out of your inventory, no longer moveable, and has new descriptive text.
      thing.location = location
      thing.tags.remove ('moveable')
      thing.tags.append ('broken')
      thing.short_description = "Slick, dark red tomato sauce is seeping across the floor."
      thing.long_description = "The tomato sauce looks horribly like blood as it seeps across the pizzeria floor."      
      return
      
    elif chosenThing != 'sauce':
      thing.location = location
      print "You throw the", thing.title
      print
      return
    
