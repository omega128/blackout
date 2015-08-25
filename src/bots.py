# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# FILENAME	bots.py
# AUTHOR	Kristopher Chambers
# UPDATED	2015-05-01
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# PURPOSE	This module handles freddy and the gang.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
import player
import things

class MusicalFreddy:
  """ Freddy ambushes the player if they linger in the office. """
  def __init__ (self):
    self.title = ""
    self.short_description = ""
    self.long_description = ""
    self.location = "OFFICE"
    self.tags = ['alive', 'hidden']
    self.t = 0

  def think (self):
    """ called each turn you stay in the office. """
    
    # Freddy gives you a few turns before he starts playing the music. Then you have another turn to RUN.
    self.t += 1
    
    if self.t == 2:
      print "You hear heavy footsteps."
      print
    elif self.t == 3:
      print "You can hear an off-key rendition of 'The Toreador March' coming"
      print "from the darkness."
      print
    elif self.t == 4:
      print "Freddy Fazbear's eyes glow in time to his music."
      print
    elif self.t == 5:
      print "It is silent."
      print
    elif self.t == 6:
      print "With a shriek, Freddy Fazbear lunges at you, his frame taking up"
      print "your whole vision before everything mercifully goes black."
      player.location = "DEAD"

class ExitFreddy:
  """ Freddy lurks near the bathrooms, and prevents you from leaving the pizzeria """
  def __init__ (self):
    self.title = "eyes"
    self.short_description = "A pair of glowing white eyes are watching you from the darkness near the bathrooms."
    self.long_description = "Freddy Fazbear's white eyes glow from within, illuminating the faint impression of a bloody handprint on his head."
    self.location = "NE CORNER"
    self.tags = ['alive']
    self.t = 0

  def think (self):
    """ called each turn near the exit. """
    # Freddy won't let you get close to the bathrooms and the exit.
    self.t += 1
    
    # Freddy doesn't like light, and will hide and wait until you turn it off before attacking.
    if things.getById('flashlight').location == 'INVENTORY' and "on" in things.getById('flashlight').tags:
      # Freddy will stay away while you have the light on
      self.t = 0
      
      # hide or unhide freddy.
      if "hidden" not in self.tags:
        self.tags.append ("hidden")
      else:
        if "hidden" in self.tags:
          self.tags.remove ("hidden")

    # Freddy will wait before lunging.
    if self.t == 2:
      print "Freddy's slow laughter echoes in the restaurant."
      print
    if self.t == 4:
      print "Without warning, Freddy Fazbear lunges at you, taking up your entire vision before everything mercifully goes black."
      player.location = "DEAD"

class Bonnie:
  """ Bonnie walks in on you when you visit the closet. """
  def __init__ (self):
    self.title = "bonnie"
    self.short_description = "Bonnie the bunny is here, staring at you with empty eyes."
    self.long_description = "Bonnie the bunny is a sickly blue in the dim light. His eyes are large, unblinking and empty. Bonnie stands motionless except for his head, which slowly rotates to track your movement."
    self.location = "CLOSET"
    self.tags = ['alive', 'hidden']
    self.t = 0

  def think (self):
    """ called each turn in the closet. """
    
    # Bonnie enters the room when you have already been there, and will kill you UNLESS you are wearing the mask.
    self.t += 1
    
    if self.t == 2:
      print "With heavy footfalls, Bonnie enters the room."
      print
      self.tags.remove ('hidden')
    
    if things.getById('mask').location != 'WORN' and self.t > 3:
      print "With a shriek, Bonnie lunges at you, taking up your whole view before everything mercifully goes black."
      print
      player.location = "DEAD"
    else:
      self.t == 3

class Chica:
  """ Chica wants her cupcake, and is looking in the kitchen for it. """
  def __init__ (self):
    self.title = "chica"
    self.short_description = "Chica the chicken is here."
    self.long_description = "Despite her resemblance to a duck, Chica is a chicken. You can tell because she has disturbingly sharp talons. Her bib says 'let's eat,' and her eyes point in different directions."
    self.location = "KITCHEN"
    self.tags = ['alive', 'hidden']
    self.t = 0

  def think (self):
    """ called each turn in the kitchen. """
    
    self.t += 1
    
    # You get one turn before Chica enters the room.
    
    if self.t == 2:
      print "You hear a rattling groan as Chica enters the room."
      print
      self.tags.remove ("hidden")

    elif self.t == 3:
      # have you dropped the cupcake?
      if things.getById('cupcake').location == self.location:
        print "With a shriek, Chica dives for the cupcake, knocking over several ladles and a saucepan that land on the ground with a deafening crash. She thrashes and scrabbles as she tries to get her claws on the cupcake."
        print
        things.getById('cupcake').tags.append ('hidden')
        
      else:
        print "With a shriek, Bonnie lunges at you. The last thing you see is the words 'let's eat,' and her oversized chicken jaws gaping open."
        print
        player.location = "DEAD"
    elif self.t == 4:
      print "Chica is holding the cupcake up. She is completely still, her eyes pointing in different directions. You swear the cupcake blinks."
      print
    elif self.t == 5:
        print "With a shriek, Bonnie lunges at you. The last thing you see is the cupcake, and her oversized chicken jaws gaping open."
        print
        player.location = "DEAD"

class Foxy:
  """ Foxy runs down the western hallway. He does that alot. """
  def __init__ (self):
    self.title = "foxy"
    self.short_description = "Foxy is in a mangled heap on the floor."
    self.long_description = "Foxy the Pirate lives up to both his names."
    self.location = "NOWHERE" # Foxy only moves to the hallway when you've been in the closet.
    self.tags = ['alive', 'hidden']
    self.t = 0

  def think (self):
    """ called each turn in the northwest hallway. """
    self.t += 1
      
    if self.t == 1:
      print "Foxy is sprinting down the hallway directly at you."
      print
      
    elif self.t == 2:
      # have you used... THE SAUCE?
      sauce = things.getById('sauce')
      if sauce.location == self.location and "broken" in sauce.tags:
        print "As Foxy sprints towards you, his mechanical feet lose their traction and slip in the spilled pizza sauce. With a shriek, he crashes into the wall and lands in a mangled heap."
        print
        self.tags.append ('mangled')
        self.tags.remove ('hidden')
      else:
        print "With a shriek, Foxy lunges at you. The last thing you see are his sharp teeth and wicked hook."
        print
        player.location = "DEAD"
        
    elif self.t == 3: 
       print "As Foxy twitches and spasmically sorts out his tattered limbs, his head turns in your direction."
       print
       self.tags.remove ('mangled')
      
    elif self.t == 4:
        print "With a shriek, Foxy lunges at you. The last thing you see are his sharp teeth and wicked hook."
        print
        player.location = "DEAD"
