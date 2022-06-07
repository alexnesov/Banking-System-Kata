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

## Goal of these principles

Increased clarity and testability resulting from the **separation of concerns**

 ## Running the app
 <code>python src/main.py</code>
 
 ## Testing command
 While being in <code>/src</code> type <code>python -m pytest src.tests</code>