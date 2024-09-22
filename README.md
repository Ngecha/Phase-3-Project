# Phase-3-Project

**Welcome to F1_Weekend**
This is a simulation of a Formula one weekend. The program has three models, a team, a circuit and an event.

**Relationships**
An event has one circuit and a team. A circuit has many events and the team has many events.

To run the program:

1. Clone the Repo to your machine.
2. Create an environment,run source phase3_project/bin/activate to activate the environment.
3. Run the app.py file that contains the CLI(Command Line Interface).

## The Program

**Overview**

This CLI application is built using Python with SQLAlchemy for ORM and SQLite as the database. It simulates management of Formula 1 weekend circuits, teams, and events. Users can create new records, delete existing records, view all records, or find records by their IDs.

## Features

- Create, view, and delete F1 circuits.
- Create, view, and delete F1 teams.
- Create, view, and delete F1 events.
- Manage relationships between events, circuits, and teams.
- Handle invalid inputs gracefully.

## Usage

The CLI gives the user the following options:

**Welcome to F1 Weekend**<br>
**Circuits**<br>

1. Create a Circuit
2. Delete a Circuit
3. See all Circuits
4. Find a Circuit<br>
   **Teams**<br>
5. Create Team
6. Delete Team
7. See all Teams
8. Find a Team<br>
   **Events**<br>
9. Create Event
10. Delete Event
11. See all Events
12. Find an Event
13. Quit

To continue, the user needs to select an option by entering the corresponding number and follow the prompts.

## Models Overview

**Event Class**
The Event class represents an F1 event that is associated with a circuit and a team. It includes methods to create, delete, retrieve, and search for events.

**Circuit Class**
The Circuit class represents an F1 circuit, including details like name, country, number of laps, and previous winner. The class allows users to create, delete, view, and find circuits.

**Team Class**
The Team class represents an F1 team with details such as the name, hometown, drivers, and engine manufacturer. Users can create, delete, view, and search for teams.

## Dependencies

- Python 3.x
- SQLAlchemy: A Python SQL toolkit and ORM.
- Alembic

## License

This project is licensed under the MIT License - see the LICENSE file for details.
