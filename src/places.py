# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# FILENAME	places.py
# AUTHOR	Kristopher Chambers
# UPDATED	2015-05-01
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#
# PURPOSE	This module handles the various locations in the pizzeria.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from dirs import *

class Place:
  """ stores information about a particular place in the pizzeria """
  def __init__ (self, title, description, exits):
    self.title = title
    self.description = description
    self.exits = exits

# This is the master list of every Place in the game.
placesByID = {
  # These three rooms are special, and exist to make bookkeeping easier.
  'TRYING TO LEAVE': Place('', '', {}), # The end of the game. If the player goes here, and the flashlight is on, they win
  'DEAD': Place('', '', {}),            # The less fun alternative
  'INVENTORY': Place('', '', {}),       # What's in your pockets
  'WORN': Place('', '', {}),            # What's on your body
  
  # These are the actual rooms of the pizzeria
  # Each "place" has a key, a title, a description, and a list of exits, organized by direction 
  'MAINTENANCE' : Place("Maintenance",
"""Your eyes dart from strange shape to strange shape in the darkness, looking for any sign of movement, but you don't see anything. Deactivated animatronic body parts are strewn around, while
rows of disembodied heads line the walls.
The door out lies to the east.""",
{EAST: 'OUTSIDE MAINTENANCE'}),
  
  'OUTSIDE MAINTENANCE' : Place("Outside Maintenance",
"""The large door to Maintenance is ajar to the west. Pirate's Cove lies to the south, and the front row of tables is to the east.""",
{WEST: 'MAINTENANCE', SOUTH: 'OUTSIDE THE COVE', EAST: 'FRONT TABLES'}), 
  
  'FRONT TABLES' : Place("The Front Tables",
"""There are more tables here, all set up with party hats. At the front of the room, the raised stage where Freddy and the Gang perform is empty.
The maintanence door is to the west. More tables lie to the south, while the bathrooms and building exit lie to the east.""",
{WEST: 'OUTSIDE MAINTENANCE', SOUTH: 'REAR TABLES', EAST: 'NE CORNER'}), 
  
  'NE CORNER' : Place("Northeast Corner",
"""The bathrooms are to the east, more of the restaurant lies to the south, while the large front doors of the restaurant are to the north.""",
{NORTH: 'TRYING TO LEAVE', SOUTH: 'SE CORNER', WEST: 'FRONT TABLES', EAST: 'BATHROOMS'}), 
  
  'BATHROOMS' : Place("Bathrooms",
"""The bathrooms are divided into the standard MENS and WOMENS. There is nothing in them.
The main restaurant is to the west.""",
{WEST: 'NE CORNER'}),
  
  'OUTSIDE THE COVE' : Place("Outside The Cove",
"""The curtain of Pirate's Cove sway gently in unseen air currents behind the big sign reading 'SORRY, OUT OF ORDER.'
To the north is the entrance to Maintenance. Rows of tables sprawl to the east, while the west hallway is to the south.""",
{NORTH: 'OUTSIDE MAINTENANCE', SOUTH: 'WEST HALLWAY', EAST: 'REAR TABLES'}), 
  
  'REAR TABLES' : Place("The Rear Tables",
"""The tables here are arrayed with party hats, ready for hordes of young children to arrive.
To the north are more tables. To the south is the east hallway. You can make out the shape of the kitchen entrance to the east, and Pirate's Cove to the west.""",
{NORTH: 'FRONT TABLES', SOUTH: 'EAST HALLWAY', EAST: 'SE CORNER', WEST: 'OUTSIDE THE COVE'}),
  
  'SE CORNER' : Place("Southeast Corner",
"""the heavy door of the kitchen is open to the south, while the rear-most tables are to the west.
To the north you can see the outline of the bathrooms, and the large double doors of the entrance.""",
{NORTH: 'NE CORNER', SOUTH: 'KITCHEN', WEST: 'REAR TABLES'}),
  
  'CLOSET' : Place("Supply Closet",
"""The supply closet is mostly filled with bottles of cleaning supplies.
The door out is open to the east.""",
{EAST: 'WEST HALLWAY'}),
  
  'WEST HALLWAY' : Place("West Hallway",
"""The hallway's walls are papered with naive children's drawings of friendly animals.
To the north you can barely see the edge of Pirates Cove in the gloom. The permanently open door of the security off lies east, while the door of the supply closet is open to the west""",
{NORTH: 'OUTSIDE THE COVE', EAST: 'OFFICE', WEST: 'CLOSET'}), 
  
  'EAST HALLWAY' : Place("East Hallway",
"""The string of fairy lights along the ceiling has fallen askew across the hallway, waiting to garotte the unwary. A list of rules hangs on the wall here, informing children to behave.
To the north is the restaurant itself, while the door to the office lies to the west.""",
{NORTH: 'REAR TABLES', WEST: 'OFFICE'}),
  
  'KITCHEN' : Place("The Kitchen",
"""For all the times you've wondered what it looked like, the perfectly ordinary kitchen just seems underwhelming.
The door out is to the north.""",
{NORTH: 'SE CORNER'}), 
  
  'OFFICE' : Place("Security Office",
"""You can just make out the dim outlines of the desk, the monitor, and the tacky posters on the walls. There is a sense of deep forboding in the still air.
The power doors lay open to the east and west.""",
{WEST: 'WEST HALLWAY', EAST: 'EAST HALLWAY'}),    
  }

def getById ( id ):
  """ returns a Place object with a given ID string """
  if id in placesByID:
    return placesByID[id]    
  else:
    return None
