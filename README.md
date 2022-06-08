![This package is currently under development.](https://img.shields.io/badge/under-development-orange.svg)


# Banking-System-Kata
<b>Applying the Hexagonal Architecture principles to a Banking System use case.</b><br>
Also known as "Ports and Adapters".

Adapters = DB, Cache, ... <br>
Ports = Website, Tests, App



## Guiding principles to build the hexagonal architecture

<ul>
<li> TDD mindset, start from the user story test 
<li> Separation of concerns 
<li> The domain layer is not imported from any other part of the system. Because the domain is the center, the business logic. The other system elements should gravitate around the domain, and not the other way around.
<li> The domain is stack agnostic, ca be changed without any impact on business logic
</ul>

## How these principles are linked to the actual code in this repo: 
These guiding principles are interesting as they show how Python's <b>Abstract Base Classes</b> (ABC) are useful to depict the pure business logic.
The **implementation** of ABC is outside the pure domain (where the ABCs were defined). The business logic can be sensed through these ABCs.
The implementation and other technical details depends on the business logic, and not the other way around.


Picture source: Https://beyondxscratch.com/2017/08/19/hexagonal-architecture-the-practical-guide-for-a-clean-architecture/

## Goal of these principles

Increased clarity and testability resulting from the **separation of concerns** and removal of **side effects*

 ## Running the app
 <code>python src/main.py</code>

 ## Testing command
<<<<<<< HEAD
 While being in <code>/src</code> type <code>python -m pytest tests</code>
=======
 While being in <code>/src</code> type <code>python -m pytest src.tests</code>
>>>>>>> ca774249c001fa809ad50b4d4459fb9a3451906e
