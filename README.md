# Banking-System-Kata
<b>Applying the Hexagonal Architecture principles to a Banking System use case.</b><br>
Following the hexagonal architecture design principles. Also known as "Ports and Adapters".

Adapters = DB, Cache, ... <br>
Ports = Website, Tests, App



## Guiding principles

<ul>
<li> Separation of concerns --> Removal of side effects
<li> Domain layer not imported form any other part of the application. Because it's the center, the business logic. The other element should gravitate around, and not the other way around.
</ul>

## Goal

Increased clarity and testability resulting from the "separation of concerns"

 
 ## Testing command
 In /src type <code>python -m pytest src.tests</code>