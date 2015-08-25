# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# FILENAME  main.py
# AUTHOR  Kristopher Chambers
# UPDATED 2015-05-03
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# PURPOSE This module handles the main game loop, user input, and the instructions.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import player
import things
import ghosts
from dirs import *

def main():
  """ shows the title, start the game, and then wave goodbye. """
  showTitle()
  showOpening()
  gameLoop()
  showGoodbye()

def showInstructions():
  """ prints a complete command list and basic help. """
  print """This is an old-skool adventure game. You interact with the game with "words" that you "type" at a "keyboard."

This game accepts only one-to-three word sentences using simple verbs. Here is a full list, with synonyms:
  GO, MOVE
  [GO] NORTH
  [GO] SOUTH
  [GO] EAST
  [GO] WEST
  EXAMINE, LOOK
  GET, TAKE
  DROP
  THROW
  TURN ON, TURN OFF
  [SHOW] INVENTORY
  WEAR, UNWEAR
  QUIT, EXIT, END

Commands are case insensitive. To see this list again, type HELP or INSTRUCTIONS at any time.
Knowledge of the Five Nights At Freddy's games is highly advisable.
Management is not responsible for pwned n00bs."""

  
def showTitle():
  """ prints some nice boilerplate for the player. """
  print "****************************************"
  print "*                                      *"
  print "*  FIVE NIGHTS AT FREDDY'S : BLACKOUT  *"
  print "*                                      *"
  print "****************************************"
  print "  A fan game by Kristopher Chambers"
  print "  Dedicated to Danielle Landry"
  print

def showOpening():
  """ prints the opening text for the game. """
  print """NIGHT 3
5 AM

The emergency doors slam closed. You take your sweating hand off the button as the power meter ticks to 4%. There is no way you'll survive another hour with power, and the power
doors are all that stand between you and horrible mutilation at the hands of Freddy and his band of animatronic nightmares.

As the meter ticks ever closer to your death, you idly try to decide which of Freddy's gang was most responsible.
Was it Bonnie? The homicidal rabbit had made three trips to the supply closet that night, passing dangerously close to the security office each time, and forcing you to close the door and use
up your precious power.
 
3% now.
 
It couldn't have been Freddy, he had only just left the stage a few minutes ago, and when you last saw him on the cameras, he had been lurking near the bathrooms.
 
2% and dropping.
 
It was all Foxy's fault, wasn't it? He just wouldn't stop running down the west hallway and banging over and over again. You don't know how knocking on a door could drain the power
but it's the sort of thing he'd do. Yes. It's all Foxy's fault.
  
1%
  
No, it was YOUR fault for coming back after the first night. You should have quit when you first heard the words "forcibly stuff you into a suit if they get into your office." Now you are almost certainly going to die,
and your last meal was cheap takeout.
 
0%

It's over. With a horrible finality, the emergency doors slam open again. The lights flicker off, plunging you into the dark as the buzzing fan dies, leaving you in total, dreadful silence.

Nothing moves. The open doorways on either side of you are gaping chasms of blackness.
  
If you stay here, they will find you.
"""

def showGoodEnding():
  """ prints the 'good' ending text, where the player narrowly escapes. """
  print """As you first crack open the large front doors at the front of the building, you can hear the heavy tread of footsteps behind you. With sudden panic you stumble, and are met with an
ear-splitting screech as someone hits you from behind, sending you sprawling to your hands and knees. A rough pair of animatronic claws grab your legs and pull you back into the darkness.
  
You scrabble at the pizzeria floor with your hands, but it does nothing. As the light of freedom recedes and the darkness surrounds you, you close your eyes and wait for the inevitable.
  
.
.
.
  
The claws let go. You open your eyes. The animatronics are shuffling away into the darkness, and your ears hear a faint sound in the distance.
 
...ding dong ding dong, ding dong ding dong...
  
dong.
  
dong.
  
dong.
  
dong.
  
dong.
  
dong.

As you lay on the ground, you reflect that you should either quit, or ask for a raise."""

def showBadEnding():
  """ prints the bad ending, where the player tries to escape, but fails. """
  print """As you first crack open the large front doors at the front of the building, you can hear the sound of Freddy's music box behind you. With sudden panic you stumble, and are met with an
ear-splitting screech as Freddy pounces, sending you sprawling to your hands and knees. Animatronic claws grab your legs and pull you back into the darkness.
 
You scrabble at the pizzeria floor with your hands, but it does nothing. As the light of freedom recedes and the darkness surrounds you, you close your eyes and wait for the inevitable...
 
At six AM, the day staff arrive to find a neatly packaged Freddy Fazbear costume, with surprisingly realistic eyes. """
  
def showGoodbye():
  """ prints 'the end' text. """
  print
  print "THE END."
  print
  
def getInputChoice(message, choices):
  """ prints a text message, and gets user input from a list of options. Returns the player's choice. """
  done = False
  
  while not done:
    choice = raw_input(message)
    if choice.lower() in choices:
      done = True
  return choice  
    
def gameLoop():
  """ the main game loop, where we get the whole feedback, input, and command parsing. """  
  
  done = False
  while not done:
    # first, make sure the game isn't over.
    if player.location == 'TRYING TO LEAVE':
      # the player is trying to leave the building. Is the flashlight in their hand, and is it turned on?
      if things.getById('flashlight').location == 'INVENTORY' and "on" in things.getById('flashlight').tags:
        showGoodEnding()
        done = True
        continue
      else:
        # woops. You haven't won yet.
        showBadEnding()
        done = True
        continue       

    # There's also the option you died last round.
    elif player.location == 'DEAD':
      done = True
      continue
    
    # Every once inawhile, spookiness happens.
    ghosts.playSpookyFlavorText()

    # Does anyone know you're here? If so, they get to act.
    for thing in things.getByLocation(player.location):
      if "alive" in thing.tags:
        thing.think()

    # ...did someone just kill you?
    if player.location == 'DEAD':
      done = True
      continue
    
    # Tell us where we are:
    player.look()

    
    # get input from the user
    userInput = raw_input("What do you do? ")
    
    # then strip the leading whitespace, convert everything to lowerspace, and split input into individual words we can parse:
    words = userInput.strip().lower().split()
    
    # did they actually say anything? If not, we don't need to go further.
    if len(words) < 1:
      continue
    
    # So, does the player want to ...
    
    # quit the game?
    if words[0] in ["quit", "exit", "end", "q"]:
      # Looks like we're done here.
      done = True
      
    # read instructions again?
    if words[0] in ['instructions', 'help', '?'] or (words[0] in ['show'] and words[1] in ['instructions', 'help']):
      showInstructions()

    # check inventory
    if words[0] in ['i', 'inv', 'inventory'] or (words[0] == 'show' and words[1] == 'inventory'):
      player.showInventory ()

    # move?
    if words[0] in ['n', 'north'] or (words[0] in ['go', 'move'] and words[1] == 'north'): player.go (NORTH)
    if words[0] in ['s', 'south'] or (words[0] in ['go', 'move'] and words[1] == 'south'): player.go (SOUTH)
    if words[0] in ['w', 'west'] or (words[0] in ['go', 'move'] and words[1] == 'east'): player.go (WEST)
    if words[0] in ['e', 'east'] or (words[0] in ['go', 'move'] and words[1] == 'west'): player.go (EAST)
    if words[0] in ['go', 'move'] and len(words) != 2:
      print ("Go where? Please specify a direction.")
      continue
   
    # all of these take a single argument.
    checkForTwoWordCommand (words, ["take", "get"], player.take)
    checkForTwoWordCommand (words, ["drop"], player.drop)
    checkForTwoWordCommand (words, ["throw"], player.throw)
    checkForTwoWordCommand (words, ["examine", "x"], player.examine)
    checkForTwoWordCommand (words, ["wear"], player.wear)
    checkForTwoWordCommand (words, ["unwear"], player.unwear)
    
    # flashlight verbs!
    if words[0] == 'turn':
      # turn something on?
      if words[1] == 'on':
        if len(words) == 3:
          player.turnOn (words[2])
        else:
          print "Turn on what? Please specify a single noun."
      
      # maybe turn it off?
      if words[1] == 'off':
        if len(words) == 3:
          player.turnOff (words[2])
        else:
          print "Turn on what? Please specify a single noun."

def checkForTwoWordCommand (words, commandNames, function):
  """ checks if a given command matches a verb noun pattern, and either executes a provided function if it is, or complains if it has too many objects """
  if words[0] in commandNames:
    if len(words) == 2:
      function (words[1])
    else:
      print commandNames[0] + " what? Please specify a single noun."
  
# And so it begins...
main()
