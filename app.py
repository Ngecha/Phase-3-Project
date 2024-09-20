from models import Event, Circuit, Team

def app():
 while True:
     print(f"**Welcome to F1 Weekend")
     print("     **Circuits**")
     print("1. Create a circuit")
     print("2. Delete a circuit")
     print("3. see all circuits")
     print("4. Find a circuit")
        
# Using try-except to handle invalid input
     try:
            choice = int(input("Enter your choice to continue: "))
     except ValueError:
            print("Invalid choice, please enter a number between 1 and 5.")
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
        Circuit.get_all_circuits
        print("hahaha")
     elif choice==4:
        print("Circuit")
        id=int(input("Enter the Circuit id:  "))
        print (id)
        Circuit.find_by_id(id)
     else:
         choice >=5 
         print ("Choose a number below 5 ")       
        
  
  

        
app()