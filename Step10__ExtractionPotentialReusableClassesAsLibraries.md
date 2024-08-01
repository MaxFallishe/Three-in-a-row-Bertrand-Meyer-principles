# The essence of the document

Creating standard libraries is an important methodological design technique. In particular, at the end of the project,
it is useful to perform an additional generalization step: allocate the most suitable classes to the standard library
for reuse in future projects. In particular, factorization and abstraction, which were considered at the end of the
previous course, are used here.

It is necessary to allocate to libraries all suitable data structures and algorithms and support for the graphical
interface, as well as all possible secondary functions represented as classes of formal properties (-able) through
structural inheritance.

# Exctracted classes

* ConsoleGUI — they are a useful implementation of abstraction that allows you to implement step-by-step logic, it is
  clear that their abstract versions will be used as libraries, but it is easy to imagine how, if desired, they can be
  used in the future for any programs, not only games, whose work is tied to step-by-step interaction with the outside
  world
* GameTurn and GameSession — they are a useful implementation of abstraction that allows you to implement step-by-step
  logic, it is clear that their abstract versions will be used as libraries, but it is easy to imagine how, if desired,
  they can be used in the future for any programs, not only games, whose work is tied to step-by-step interaction with
  the outside world
* TwoDimensionalArray — the concept of a two-dimensional array itself is quite simple due to this, it can easily be
  designed into a full-fledged class, which is a good idea since it is quite universal in itself, despite the fact that
  it does not have a direct implementation in the python standard library, but it is not always reasonable to drag numpy
  into the project.
* Software Patterns — any design patterns implemented during the project process should be allocated to the library of
  potential reusable modules, because each time implementing a pattern from scratch is not always a pleasant experience
