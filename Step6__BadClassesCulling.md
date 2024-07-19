# The essence of the document
Class identification is a dual process. It implies both the nomination of candidates for being an Abstract Data Type 
and their later selection, as well as the screening out of unsuitable ones.
1. the candidate is not suitable if he encapsulates some action, function
2. the candidate is not suitable if he answers the question "this class does ..."
3. the candidate is most often not suitable if he continues (or begins) the hierarchy of classes when the analysis phase is not over yet
4. the candidate is not suitable if it is a class without methods.
5. the candidate is not suitable if it is a class without its own fields, or with a small number of them, but inheriting the attributes of its parents.
6. a candidate, as a rule, is not suitable if he does not contain commands, but only requests.
7. the candidate is not suitable if two or more different abstractions are mixed in it.

# A list of rejected classes with an explanation of the reason
The Abstract data types that were highlighted in the previous steps are listed below. Next to each Abstract Data Type, 
there are REJECTED or SAVED marks — the result of whether it has passed the correctness check or not. Emojis tick off 
the items that the Abstract Data type corresponds to, and emojis with a cross indicate the items that do not correspond 
(numbering in accordance with the section "The essence of the document").

- Analysis Classes
  - Shard - _SAVED_ 
    - ✅ ✅ ✅ ✅ ✅ ✅ ✅ 
  - GameField - _SAVED_,
    - ✅ ✅ ✅ ✅ ✅ ✅ ✅  
  - GameTurn - _SAVED_,
    -  ✅ ✅ ✅ ✅ ✅ ✅ ✅  
  - FieldEffect - _SAVED_,
    -  ✅ ✅ ✅ ✅ ✅ ✅ ✅  
  - GameSession -_SAVED_,
    -  ✅ ✅ ✅ ✅ ✅ ✅ ✅  

- Realization Classes
  - TwoDimensionalArray - _SAVED_, 
    -  ✅ ✅ ✅ ✅ ✅ ✅ ✅  

- Design Classes
  - FieldObserver - _SAVED_,
    - ✅ ✅ ✅ ✅ ✅ ✅ ✅
  - FieldPhysicsStrategy - _SAVED_,
    - ✅ ✅ ✅ ✅ ✅ ✅ ✅
  - TurnsStack - _SAVED_,
    - ✅ ✅ ✅ ✅ ✅ ✅ ❌
  - MultiLangDict - _SAVED_,
    - ✅ ✅ ✅ ❌ ✅ ❌ ✅
