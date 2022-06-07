# Banking-System-Kata
<b>Applying the Hexagonal Architecture principles to a Banking System use case.</b><br>
Also known as "Ports and Adapters".

Adapters = DB, Cache, ... <br>
Ports = Website, Tests, App



## Guiding principles

<ul>
<li> Separation of concerns &rarr; Removal of <b>side effects</b>
<li> The domain layer is not imported form any other part of the system. Because the domain is the center, the business logic. The other system elements should gravitate around the domain, and not the other way around.
<li> The domain is stack agnostic, ca be chaged without any impact on business logic
</ul>

## How these principles are linked to the actual code in this repo: 
These guiding principles are interesting as they show how Python's <b>Abstract Base Classes</b> (ABC) are useful to depict the pure business logic.
The **implementation** of ABC is outside the pure domain, where ABCs were defined. The business logic can be sensed through these ABCs.
The implementation and other technical details depends on the business logic, and not the other way around.

## Goal of these principles

Increased clarity and testability resulting from the **separation of concerns**

 ## Running the app
 <code>python src/main.py</code>

 ## Testing command
 While being in <code>/src</code> type <code>python -m pytest src.tests</code>