from models import Event, Circuit, Team

def app():
    # Infinite loop to keep the CLI running until user chooses to exit
    while True:
        # Menu for user choices
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
        
        # Using try-except to handle invalid input when converting input to integer
        try:
            choice = int(input("Enter your choice to continue: "))
        except ValueError:
            # If user enters a non-integer, prompt them with an error message and restart loop
            print("Invalid choice, please enter a number between 1 and 12.")
            continue

        # Process user input based on their choice
        if choice == 1:
            # Create a new Circuit
            print("*Creating Circuit*")
            name = input("Enter name: ")
            country = input("Enter country: ")
            try:
                laps = int(input("Enter number of laps: "))  # Validate laps input as integer
            except ValueError:
                print("Laps must be a valid number.")
                continue
            previous_winner = input("Enter previous winner: ")
            
            # Call the Circuit class method to create a circuit
            Circuit.create_circuit(name, country, laps, previous_winner)
            print(f"Circuit '{name}' created.")
        
        elif choice == 2:
            # Delete a Circuit by name
            print("Deleting Circuit") 
            name = input("Enter Circuit name: ")
            try:
                Circuit.delete_circuit(name)
                print(f"Circuit '{name}' has been deleted.")
            except ValueError as e:
                print(e)  
                 
        elif choice == 3:
            # Display all Circuits
            print("Listing all Circuits...")
            Circuit.get_all_circuits()
        
        elif choice == 4:
            # Find a Circuit by its ID
            print("Find Circuit")
            try:
                circuit_id = int(input("Enter the Circuit id: "))  # Validate circuit ID as integer
                Circuit.find_by_id(circuit_id)
            except ValueError as e:
                print(e)
                
            
        
        elif choice == 5:
            # Create a new Team
            print("*Creating Team*")
            name = input("Enter team name: ")
            hometown = input("Enter hometown: ")
            drivers = input("Enter the drivers: ")
            engine_manufacturer = input("Enter engine manufacturer: ")
            Team.create_team(name, hometown, drivers, engine_manufacturer)
            print(f"Team '{name}' created.")
        
        elif choice == 6:
            # Delete a Team by name
            print("Deleting Team")
            name = input("Enter Team name: ")
            try:
              Team.delete_team(name)
              print(f"Team '{name}' has been deleted.")
            except ValueError as e:
                print(e)
        
        elif choice == 7:
            # Display all Teams
            print("Listing all Teams...")
            Team.get_all_teams()
        
        elif choice == 8:
            # Find a Team by its ID
            print("Find Team")
            try:
                team_id = int(input("Enter the Team id: "))  # Validate team ID as integer
                Team.find_by_id(team_id)
            except ValueError as e:
                print(e)
            
        
        elif choice == 9:
            # Create a new Event
            print("*Creating Event*")
            name = input("Enter event name: ")
            try:
                circuit_id = int(input("Enter Circuit id: "))  # Validate circuit ID as integer
                team_id = int(input("Enter Team id: "))  # Validate team ID as integer
            except ValueError:
                print("Invalid Circuit or Team ID")
                continue
            Event.create_event(name, circuit_id, team_id)
            print(f"Event '{name}' created.")
        
        elif choice == 10:
            # Delete an Event by name
            print("Deleting Event")
            name = input("Enter Event name: ")
            try:
              Event.delete_event(name)
              print(f"Event '{name}' has been deleted.")
            except ValueError as e:
                print(e)
                
        elif choice == 11:
            # Display all Events
            print("Listing all Events...")
            Event.get_all_events()
        
        elif choice == 12:
            # Find an Event by its ID
            print("Find Event")
            try:
                event_id = int(input("Enter the Event id: "))  # Validate event ID as integer
            except ValueError:
                print("Invalid Event ID")
                continue
            Event.find_by_id(event_id)
        
        elif choice == 0:
            # Quit the application
            print("Exiting the application...")
            break  # Break the loop to exit the program
        
        else:
            # Handle invalid choices outside the expected range
            print("Invalid choice, please try again.")

# Start the CLI app
app()
