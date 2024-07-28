# The essence of the document
We form the architecture, set the principles of system behavior: schemes for creating objects, event processing, 
linking with selected frameworks and technologies, and tests for typical scenarios (design).


# Principles of system behavior
1. Schemes for creating objects:
   * The playing field can only be created by the object of the game session
   * A game move can only be created from a game session object
   * Shards can only be created by heirs of the abstract game effect class
2. Schemes for event processing:
   * Each user move is a separate independent area with its own input and output data
   * After completing the user's actions on the move, the final state of the playing field is calculated
3. Linking with frameworks and technologies:
   * External frameworks will not be used in the application, one of the elements that would potentially 
     be optimal to do with the help of an external dependency — the UI interface of the game in the console will be 
     mplemented using the standard built-in Python library curses.
4. Tests for typical scenarios:
   * Testing the correct display of the game UI in the terminal
   * Testing the correct calculation of the physics of the field
   * Testing the correctness of the algorithm for filling the playing field with shards
   * Testing the movement in the game history of moves
   * Testing each of the created game effects on the playing field

