from sqlalchemy import create_engine, CheckConstraint, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create SQLite database engine
engine = create_engine('sqlite:///F1_Weekend.db')

# Base class for models
Base = declarative_base()

# Create tables from all defined models
Base.metadata.create_all(engine)

# Event Model
class Event(Base):
    __tablename__ = 'events'
    
    # Table Columns
    id = Column(Integer, primary_key=True)
    name = Column(String(15), unique=True)
    circuit_id = Column(String, ForeignKey('circuits.id'))
    team_id = Column(String, ForeignKey('teams.id'))
    
    # Relationships
    circuit = relationship('Circuit', back_populates='events')  # Link to Circuit
    team = relationship('Team', back_populates='events')        # Link to Team
    
    # Representation method for debugging
    def __repr__(self):
        return f"Event number: {self.id}"\
               + f"  Circuit Name: {self.name}"\
               + f"  Circuit id: {self.circuit_id}"\
               + f"  Team id: {self.team_id}"
    
    # Class method to create a new event
    @classmethod
    def create_event(cls, name, circuit_id, team_id):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Create a new event object
        new_event = cls(name=name, circuit_id=circuit_id, team_id=team_id)
        
        # Add and commit new event to database
        session.add(new_event)
        session.commit()    
    
    # Class method to delete an event by name
    @classmethod
    def delete_event(cls, name):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Query for the event by name
        query = session.query(Event).filter_by(name=name).first()
        # Delete the queried event
        if not query:
        # Handle the case where the circuit does not exist
         raise ValueError(f"Circuit '{name}' does not exist.")
        else:
        # Delete the queried circuit
         session.delete(query)
         session.commit()
       

    
    # Class method to get and display all events
    @classmethod
    def get_all_events(cls):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Query to get all event names
        all_events = session.query(cls.name).all()
        print(all_events) 
    
    # Class method to find an event by its ID
    @classmethod
    def find_by_id(cls, id):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Query to find the event by ID
        event = session.query(cls).filter_by(id=id).first()
        print(event)

# Circuit Model
class Circuit(Base):
    __tablename__ = "circuits"
    
    # Table Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    laps = Column(Integer, nullable=False)
    previous_winner = Column(String, nullable=True)
    
    # Relationship: a circuit can have many events
    events = relationship('Event', back_populates='circuit')
    
    # Representation method for debugging
    def __repr__(self):
        return f"Circuit number: {self.id}"\
               + f"  Circuit Name: {self.name}"\
               + f"  Circuit Country: {self.country}"\
               + f"  Circuit Laps: {self.laps}"\
               + f"  Circuit Previous Winner: {self.previous_winner}"
    
    # Class method to create a new circuit
    @classmethod
    def create_circuit(cls, name, country, laps, previous_winner):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Create a new circuit object
        new_circuit = cls(name=name, country=country, laps=laps, previous_winner=previous_winner)
        
        # Add and commit new circuit to database
        session.add(new_circuit)
        session.commit()    
    
    # Class method to delete a circuit by name
    @classmethod
    def delete_circuit(cls, name):
      Session = sessionmaker(bind=engine)
      session = Session()

    # Query for the circuit by name
      query = session.query(Circuit).filter_by(name=name).first()

      if not query:
        # Handle the case where the circuit does not exist
        raise ValueError(f"Circuit '{name}' does not exist.")
      else:
        # Delete the queried circuit
        session.delete(query)
        session.commit()
        
    
    # Class method to get and display all circuits
    @classmethod
    def get_all_circuits(cls):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Query to get all circuit names
        all_circuits = session.query(cls.name).all()
        print([name[0] for name in all_circuits])  # Print just the names
    
    # Class method to find a circuit by its ID
    @classmethod
    def find_by_id(cls, id):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Query to find the circuit by ID
        circuit = session.query(cls).filter_by(id=id).first()
        if not circuit:
            raise ValueError(f"Circuit {id} doesn't exist")
        print(circuit.name)

# Team Model
class Team(Base):
    __tablename__ = 'teams'
   
    # Table Columns 
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    hometown = Column(String, nullable=False)
    drivers = Column(String, nullable=False)
    engine_manufacturer = Column(String, nullable=False)
    
    # Relationship: a team can have many events
    events = relationship('Event', back_populates='team') 
    
    # Representation method for debugging
    def __repr__(self):
        return f"Team number: {self.id}"\
               + f"  Team Name: {self.name}"\
               + f"  Team Hometown: {self.hometown}"\
               + f"  Team Drivers: {self.drivers}"\
               + f"  Engine Manufacturer: {self.engine_manufacturer}"
    
    # Class method to create a new team
    @classmethod
    def create_team(cls, name, hometown, drivers, engine_manufacturer):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Create a new team object
        new_team = cls(name=name, hometown=hometown, drivers=drivers, engine_manufacturer=engine_manufacturer)
        
        # Add and commit new team to database
        session.add(new_team)
        session.commit()    
    
    # Class method to delete a team by name
    @classmethod
    def delete_team(cls, name):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Query for the team by name
        query = session.query(Team).filter(Team.name == name).first()
        if not query:
            raise ValueError(f"Circuit '{name}' does not exist.")
        else:
        # Delete the queried team
         session.delete(query)
         session.commit()  
    
    # Class method to get and display all teams
    @classmethod
    def get_all_teams(cls):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Query to get all team names
        team_names = session.query(cls.name).all()
        print(team_names)
    
    # Class method to find a team by its ID
    @classmethod
    def find_by_id(cls, id):
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Query to find the team by ID
        team = session.query(cls).filter_by(id=id).first()
        if not team:
            raise ValueError(f"Team {id} doesn't exist")
        print(team.name)

