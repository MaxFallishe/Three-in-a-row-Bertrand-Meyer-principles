# The essence of the document
In this document, we will define the boundaries of the system being developed:

- what will be included in the system, and what exactly should not be included in it;
- main subsystems;
- user metaphors (what exactly does the user/customer understand by what, within the framework of the project, he calls, for example, "Car" or "Product" or "Customer");
- functionality;
- reuse libraries.

# Boundaries description
1. **System components** \
The system being developed should include the implementation of the internal logic of the game, a mechanism for displaying the gameplay in
consoles. The system under development should not include the implementation of mechanisms for the correct display of characters in the console,
this point remains on the shoulders of the operating system.

2. **Main subsystems**
   - subsystem for generating the playing field
   - subsystem for field physics
   - subsystem for calculating moves 
   - subsystem for displaying the interface in the console 
   - subsystem for saving user actions

3. **User metaphors**
   - Playing field — 2D matrix, measuring 8 by 8 identical squares in the shape of a square 
   - Game element (shard) — various types of objects that can take a place in the matrix cell (in each cell 
     there can be only one game element)
   - Game event — successful user interaction with elements inside the game field  
   - Game move (turn) — a period of time (in conjunction with the game events that occurred during this period) between any 
     the next two successful clicks of the "next move"/"start the game" button by the user

4. **Functionality** \
The user has the ability to move elements inside the matrix (1 cell up, down, left or right), while
the element that stands at the new position of the element becomes the previous position of the element. 
In addition to the gameplay, the user can also start the game, restart the game and finish it ahead of schedule.

5. **Reuse libraries**
   - _not defined_
