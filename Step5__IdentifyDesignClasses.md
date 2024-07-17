# The essence of the document
Design classes are usually added to a project in two ways: the designer uses his previous successful experience or 
ready-made architectural solutions (primarily classical design patterns) from the relevant literature.

The general principle remains the same: it is better to reuse already proven ready-made solutions than to invent them yourself.

Design classes are more correctly understood as "machines" (for example, state machines, "active" data structures with
rather complex internal logic and composition of other classes) or "factories" (generators of objects), rather than 
as simple entities.

# Highlighting the main design classes (Abstract Data Types) in the project
- FieldObserver - паттерн "наблюдатель", обеспечивает связывание между шардами на игровом поле
- FieldPhysicsStrategy - паттерн "стратегия", обеспечивает возможность взаимозаменять алгоритмы обработки физики игрового поля
- TurnsStack - стек в котором, ведется запись ходов пользователя, не позволяет вставлять ходы между существующими 
  ходами, только удалять или вставлять в конец
- MultiLangDict - синглтон датакласс, позволяющий динамично менять язык приложения в зависимости от настроек пользователя
