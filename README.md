# Banking-System-Kata
<b>Applying the Hexagonal Architecture principles to a Banking System use case.</b><br>
Also known as "Ports and Adapters".

Adapters = DB, Cache, ... <br>
Ports = Website, Tests, App



## Guiding principles

<ul>
<li> Separation of concerns &rarr; Removal of <b>side effects</b>
<li> Domain layer not imported form any other part of the application. Because it's the center, the business logic. The other element should gravitate around, and not the other way around.
<li> Domain is stack agnostic, ca be chaged without any impact on business logic
</ul>

These guiding principles are interesting as they show how Python <b>Abstract Base Classes</b> are useful to depict the pure business logic.
The implementation of ABC is outside the pure domain that dicates the business logic.
Again, it follows the Hexagonal philosophy, the implementation and other technical details depends on the business logic, and not the other way around.

## Goal of these principles

Increased clarity and testability resulting from the **separation of concerns**

 ## Running the app
 <code>python src/main.py</code>

 ## Testing command
 While being in <code>/src</code> type <code>python -m pytest src.tests</code>