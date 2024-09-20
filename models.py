from sqlalchemy import create_engine,CheckConstraint, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine=create_engine('sqlite:///F1_Weekend.db')
Base=declarative_base()
Base.metadata.create_all(engine)

class Event(Base):
    __tablename__='events'
    
    id=Column(Integer,primary_key=True)
    name=Column(String(15),unique=True)
    circuit_id=Column(String, ForeignKey('circuits.id'))
    team_id=Column(String, ForeignKey('teams.id'))
    
    #Relationship
    circuit=relationship('Circuit' ,back_populates='events')
    team=relationship('Team', back_populates='events')
    
    def __repr__(self):
        return f"Event number; {self.id}"\
            +f"  Circuit Name: {self.name}"\
            +f"  Circuit id; {self.circuit_id}"\
                +f"  team id: {self.team_id}"   
                
                
    @classmethod
    def create_event(cls,name, circuit_id, team_id):
        Session=sessionmaker(bind=engine)
        session=Session()     
        
        new_event=cls(name=name, circuit_id=circuit_id, team_id=team_id)
        
        session.add(new_event)
        session.commit()    
    
     
    @classmethod
    def delete_event(cls,id):
        Session=sessionmaker(bind=engine)
        session=Session()
         
        query = session.query(Event).filter_by(id=id).first()
        session.delete(query)
        session.commit()  
    
    
    @classmethod
    def get_all_events(cls):
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Query to get all teams
            all_events = session.query(cls).all()
            
            return all_events 
    
    @classmethod    #Method to find a teams using id
    def find_by_id(cls, id):
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Query to find teams by ID
            event = session.query(cls).filter_by(id=id).first()
            
            print(event)               



#Circuit Model
class Circuit(Base):
    __tablename__="circuits"       
    
    id=Column(Integer, primary_key=True )
    name=Column(String,nullable=False, unique=True)
    country=Column(String,nullable=False)
    laps=Column(Integer,nullable=False)
    previous_winner=Column(String,nullable=True)
    
    #One to one Relationship
    events =relationship('Event', back_populates='circuit')
    
    def  __repr__(self):
        return f"Circuit number: {self.id}"\
                +f"  Circuit Name :{self.name}"\
                +f"  Circuit Country: {self.country}"\
                +f"  Circuit Laps: {self.laps}"\
                +f"  Circuit Previous Winner: {self.previous_winner}"
                
    @classmethod
    def create_circuit(cls, name,country, laps, previous_winner):        
        Session=sessionmaker(bind=engine)
        session=Session()     
        
        new_circuit=cls(name=name, country=country,laps=laps, previous_winner=previous_winner)
        
        session.add(new_circuit)
        session.commit()    
        
        
    @classmethod
    def delete_circuit(cls,name):
        Session=sessionmaker(bind=engine)
        session=Session()
         
        query = session.query(Circuit).filter_by(name=name).first()
        session.delete(query)
        session.commit()
        
    @classmethod
    def get_all_circuits(cls):
            Session = sessionmaker(bind=engine)
            session = Session()
            all_circuits = session.query(cls.name).all()
            
            print([name[0] for name in all_circuits])  
    @classmethod
    def find_by_id(cls,id):
            Session = sessionmaker(bind=engine)
            session = Session()
            circuit = session.query(cls).filter_by(id=id).first()
            
            print (circuit.name)
             
                                        
class Team(Base):
    __tablename__= 'teams'
   
   #Table Columns 
    id=Column(Integer, primary_key=True)
    name=Column(String, unique=True, nullable=False)
    hometown=Column(String, nullable=False)
    drivers=Column(String, nullable=False)
    engine_manufacturer= Column(String, nullable=False)
     
    #Relationships
    events=relationship('Event', back_populates='team') 
    
    def  __repr__(self):
        return f"Team number: {self.id}"\
                +f"Team Name :{self.name}"\
                +f"Team Hometown: {self.hometown}"\
                +f"Team Drivers: {self.drivers}"\
                +f"Engine Manufacturer: {self.engine_manufacturer}"
        
    @classmethod
    def create_team(cls, name,hometown, drivers, engine_manufacturer):
        Session=sessionmaker(bind=engine)
        session=Session()     
        
        new_team=cls(name=name, hometown=hometown, drivers=drivers, engine_manufacturer=engine_manufacturer)
        
        session.add(new_team)
        session.commit()    
    
     
    @classmethod
    def delete_team(cls,name):
        Session=sessionmaker(bind=engine)
        session=Session()
         
        query = session.query(Team).filter(Team.name==name)
        session.delete(query)
        session.commit()  
    
    
    @classmethod
    def get_all_teams(cls):
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Query to get all teams
            team_names = session.query(cls.name).all()
            
            print(team_names) 
    
    @classmethod    #Method to find a teams using id
    def find_by_id(cls, id):
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Query to find teams by ID
            team = session.query(cls).filter_by(id=id).first()
            
            print(team.name)          
        
Team.find_by_id(1)