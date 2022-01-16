## Notes

## Architectural Decisions

## Design Decisions

1. Choice for Enum  <br>
   1. "weekday" should not be local to the function Sol option: define at instance, class, or
   global level  
   2. Problem: local will overshadow Mutable. Should be immutable but its definition can
change   
   3. if Cardinality = 1 then can use typing's final If mutually exclusive, then use Enum

2. Ways to implement types
   1. typing.NamedTuple
   2. dataclass
   3. pydentic.BaseModel
   4. box dict

3. We are outsourcing our type checking to the static type checker, mypy in this case.

## Data Types

## Next Steps
Way forward options - 
1. Move above hotel, have multiple hotels and choose based on input
2. Implement customer type - reward vs regular customer
3. 

## Open Items
1. Compare and contrast - linter, formatter and static type checker