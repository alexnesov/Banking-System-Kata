![This package is currently under development.](https://img.shields.io/badge/under-development-orange.svg)


# Banking-System-Kata
<b>Applying the Hexagonal Architecture principles to a Banking System use case.</b><br>
Also known as "Ports and Adapters".

Adapters = DB, Cache, ... <br>
Ports = Website, Tests, App

*Is this ports and adapters? Or is it **hexagonal architecture**? Is that the same as onion architecture? What about the clean architecture? What's a port, and what's an adapter? Why do you people have so many words for the same thing?*
*Although some people like to nitpick over the differences, all these are pretty much names for the same thing, and thhey all boil down to the **dependency inversion principle: high-level modules (the domain) should not depend on low-level ones (the infrastructure).***

*Architecture Patterns with Python*, Harry J.W. Percival & Bob

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

Increased clarity and testability resulting from the **separation of concerns** and removal of **side effects**

 ## Running the app
 <code>python src/main.py</code>

 ## Testing command
 While being in <code>/src</code> type <code>python -m pytest tests</code>


# User Stories

## 1

In order to save money
As a bank client
I want to make a deposit in my account


## 2

In order to retrieve some or all of my savings
As a bank client
I want to make a withdrawal from my account

## 3

In order to check my operations
As a bank client
I want to see the history (operation, date, amount, balance) of my operations