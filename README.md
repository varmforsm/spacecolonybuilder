spacecolonybuilder
==================

A basic simulation of a space colony, with the ability to extend and control the colony. Designed by my younger son.

Short-term plan - six months
----------------------------
The gameplan is as follows;
- create a controlling framework that can be responsible for;
  - receiving and distributing events (MQ?) between game objects
  - creating and destroying objects
  - sending out a heartbeat (a timed event) to all objects at configurable times (default: five seconds realtime, 1 minute gametime) to automatically increase and decrease levels of oxygen, waster and water, for example
  - keeping the world up to date, i.e creating random events, risks and so on
- give the simulation load/save capabilities

Long-term plan - years...
-------------------------
Adding graphics

Objects involved
----------------
Building - needs Water (Material), Energy (Material) and Oxygen (Material)
Factory - producing Material from Materials
Powerplant - a factory producing Energy from sunlight or via fission or using waste
Oxygenplant - a factory producing Oxygen (Material) from Water (Material) using Energy (Material)
Mine - a factory producing Materials from Surface elements
Crewmember - a human with Skills, Job and a Mission
Crew - a collection of Crewmember
Vehicle - an object that can carry a load of Materials and/or a Crew between two Positions, at a given Velocity
Materials - iron, copper, oxygen, water and whatever else that can be defined as a "raw material"
Surface - a square of land, containing upto 100 of Materials
World - a collection of Surface elements
Event - to be sent or received by the game objects
Mission - an assignment with a start and end goal possible to set up and define using game objects
