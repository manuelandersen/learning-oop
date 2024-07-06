# Understanding OOP 

This is a repo for the code in this [video](https://www.youtube.com/watch?v=cM_ocyOrs_k), thanks to him i finally understand OOP, chek it out and give it some like's.

# Classes Basics

Classes are "blueprints" for a specific object

We will implement three classes:

1) Characters
2) Weapons
3) Health bars 

# Characters Class 

We need to answer:
- What is it like? --> Attributes
    - Name
    - Health
    - Damage
- What can it do? --> Method's
    - Attack

- The __init__() method is where we pass the attributes that we want to give to our new object. -->(Class level variables)
If we set variables before the init method they will be shared across all instances of a class. -->
(Object-level variables)

# Weapons Class 

Objects can hold another objects.

We need to answer:
- What is it like? --> Attributes
    - Name
    - Type
    - Damage
    - Value

# Class Inheritance: Hero & Enemy

What if we want the Hero to change it's weapon by equiping or dropping one? And the enemy to have the same weapon all the time? --> How to crontrol this when creating the object?

So we want the Hero and the Enemy to behave differently --> Class Inheritance:

Because we have a complete class, we can create as many subclasses out of it.