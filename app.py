from models import Event, Circuit, Team

def app():
 while True:
     print(f"**Welcome to F1 Weekend")
     print("     **Circuits**")
     print("1. Create a circuit")
     print("2. Delete a circuit")
     print("3. see all circuits")
     print("4. Find a circuit")
     print("      **Teams**")
     print("5. Create team")
     print("6. Delete team")
     print("7. See all teams")
     print("8. Find a team")
        
     # Using try-except to handle invalid input
     try:
            choice = int(input("Enter your choice to continue: "))
     except ValueError:
            print("Invalid choice, please enter a number between 1 and 8.")
            continue

        # Handle different options
     if choice == 1:
            print("*Creating circuit*")
            name = input("Enter name:  ")
            country = input("Enter country: ")
            try:
                laps = int(input("Enter number of laps: ")) 
            except ValueError:
                print("Laps must be a valid number.")
                continue
            previous_winner = input("Enter previous winner: ")
            
            Circuit.create_circuit(name, country, laps, previous_winner)
            print(f"Circuit '{name}' created.")
     elif choice==2:
        print("Deleting circuit") 
        name=input("Enter Name:  ")
        Circuit.delete_circuit(name)
        print(f"Circuit {name} has been deleted")
     elif choice ==3:
        print("circuits")
        Circuit.get_all_circuits()
     elif choice==4:
        print("Circuit")
        id=int(input("Enter the Circuit id:  "))
        print (id)
        Circuit.find_by_id(id)
      
     elif choice == 5:
            print("*Creating Team*")
            name = input("Enter name:  ")
            hometown = input("Enter Hometown: ")
            drivers =input("Enter the drivers: ") 
            engine_manufacturer= input("Enter the engine manufacturer: ")
            Team.create_team(name, hometown, drivers,engine_manufacturer)
            print(f"Team** '{name}' **created.")
     elif choice==6:
         print("Deleting team") 
         name=input("Enter Name:  ")
         Team.delete_team(name)
         print(f"Team **{name}** has been deleted")
     elif choice ==7:
         print("Team")
         Team.get_all_teams()
     elif choice==8:
         print("Teams")
         id=int(input("Enter the Team id:  "))
         Team.find_by_id(id)
        
  
  

        
app()