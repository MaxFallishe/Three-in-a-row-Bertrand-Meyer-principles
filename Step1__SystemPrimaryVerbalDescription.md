# The essence of the document
This document provides a verbal description of the system that we want to make. 
Within the framework of this document, we adhere to the principles of modularity. 
Approximately 5–7 of the most common entities (potential abstract data types) should be described in this document, 
they can be described briefly and informally. The main part of this document will indicate what each of the initially 
proposed entities does. It is important that from this set of formulations "who does what" the general idea of the 
system as a whole would be well understood.

# System primary description
> Important note! The technical specification for this project represents the well-known concept of the three-in-a-row game.

The system should be a console application that implements the game three in a row. The game should have a playing
field in the form of a matrix, elements (of different types) that will be placed inside the playing field and will disappear under
certain conditions, bonus effects from certain combinations. There should also be certain statistics regarding the player's actions with
the possibility of further use. 

As part of the formulation of the main administrative divisions (Abstract data types), it turned out to identify the following and define
What they are doing:
1. The element (shard)\
   Represents an element that can be located inside the playing field, the main object that the player can manipulate.

2. The playing field \
   Restricts the logic of placing elements during the game.

3. The game move \
   Contains information about the player's specific move, including completed actions, etc.

4. Effect (on the playing field) \
   It has any effect on the playing field, for example, it mixes all the elements on the playing field.

5. The interface in the console \
   Displays the graphical interface of the game to the user and allows the player to make the next move.

6. Game session \
   Accumulates information about the course of the game session.

7. The field generator \
   Determines the pattern and fills the playing field according to it.

