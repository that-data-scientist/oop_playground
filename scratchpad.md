## Notes

## Architectural Decisions

## Design Decisions

1. Choice for Enum  <br>
   1. "weekday" should not be local to the function Sol option: define at instance, class, or
   global level  
   2. Problem: local will overshadow Mutable. Should be immutable but its definition can
change   
   3. if Cardinality = 1 then can use typing's final If mutually exclusive, then use Enum

3. Ways to implement types
   1. typing.NamedTuple
   2. dataclass
   3. pydentic.BaseModel
   4. box dict

## Data Types

