from models import Event, Circuit, Team

def app():
    while True:
        print(f"**Welcome to F1 Weekend**")
        print("     **Circuits**")
        print("1. Create a Circuit")
        print("2. Delete a Circuit")
        print("3. See all Circuits")
        print("4. Find a Circuit")
        print("      **Teams**")
        print("5. Create Team")
        print("6. Delete Team")
        print("7. See all Teams")
        print("8. Find a Team")
        print("      **Events**")
        print("9. Create Event")
        print("10. Delete Event")
        print("11. See all Events")
        print("12. Find an Event")
        print("0. Quit")
        
        # Using try-except to handle invalid input
        try:
            choice = int(input("Enter your choice to continue: "))
        except ValueError:
            print("Invalid choice, please enter a number between 1 and 12.")
            continue

        # Handle different options
        if choice == 1:
            print("*Creating Circuit*")
            name = input("Enter name: ")
            country = input("Enter country: ")
            try:
                laps = int(input("Enter number of laps: ")) 
            except ValueError:
                print("Laps must be a valid number.")
                continue
            previous_winner = input("Enter previous winner: ")
            
            Circuit.create_circuit(name, country, laps, previous_winner)
            print(f"Circuit '{name}' created.")
        
        elif choice == 2:
            print("Deleting Circuit") 
            name = input("Enter Circuit name: ")
            Circuit.delete_circuit(name)
            print(f"Circuit '{name}' has been deleted.")
        
        elif choice == 3:
            print("Listing all Circuits...")
            Circuit.get_all_circuits()
        
        elif choice == 4:
            print("Find Circuit")
            try:
                circuit_id = int(input("Enter the Circuit id: "))
            except ValueError:
                print("Invalid Circuit ID")
                continue
            Circuit.find_by_id(circuit_id)
        
        elif choice == 5:
            print("*Creating Team*")
            name = input("Enter team name: ")
            hometown = input("Enter hometown: ")
            drivers = input("Enter the drivers: ")
            engine_manufacturer = input("Enter engine manufacturer: ")
            Team.create_team(name, hometown, drivers, engine_manufacturer)
            print(f"Team '{name}' created.")
        
        elif choice == 6:
            print("Deleting Team")
            name = input("Enter Team name: ")
            Team.delete_team(name)
            print(f"Team '{name}' has been deleted.")
        
        elif choice == 7:
            print("Listing all Teams...")
            Team.get_all_teams()
        
        elif choice == 8:
            print("Find Team")
            try:
                team_id = int(input("Enter the Team id: "))
            except ValueError:
                print("Invalid Team ID")
                continue
            Team.find_by_id(team_id)
        elif choice == 9:
            print("*Creating Event*")
            name = input("Enter event name: ")
            try:
                circuit_id = int(input("Enter Circuit id: "))
                team_id = int(input("Enter Team id: "))
            except ValueError:
                print("Invalid Circuit or Team ID")
                continue
            Event.create_event(name, circuit_id, team_id)
            print(f"Event '{name}' created.")
        
        elif choice == 10:
            print("Deleting Event")
            name = input("Enter Event name: ")
            Event.delete_event(name)
            print(f"Event '{name}' has been deleted.")
        
        elif choice == 11:
            print("Listing all Events...")
            Event.get_all_events()
        
        elif choice == 12:
            print("Find Event")
            try:
                event_id = int(input("Enter the Event id: "))
            except ValueError:
                print("Invalid Event ID")
                continue
            Event.find_by_id(event_id)
        
        elif choice == 0:
            print("Exiting the application...")
            break
        
        else:
            print("Invalid choice, please try again.")
  

app()
