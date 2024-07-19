# The essence of the document
We select the final set of classes, removing unnecessary ones (analysis) and form clusters from them: we combine classes
as modules into logical groups (transition to design).


Clusters often depend on each other. However, even if dependent clusters are not completed, development can be carried out 
taking into account the formal specifications of the necessary administrative divisions 
(in fact, public class interfaces), or using their abstract or partially implemented versions. 
The development of different clusters can be carried out in parallel and independently.

# A list of rejected classes with an explanation of the reason

- Cluster №1
  - GameTurn  
  - GameSession
- Cluster №2
  - TwoDimensionalArray
  - GameField
  - FieldPhysicsStrategy
  - FieldObserver
  - FieldEffect
- Cluster №3
  - Shard
