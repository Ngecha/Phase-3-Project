from sqlalchemy import create_engine,CheckConstraint, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base=declarative_base()


class Event(Base):
    __tablename__='events'
    
    id=Column(Integer,primary_key=True)
    name=Column(String,unique=True)
    circuit_id=Column(String, ForeignKey('circuits.id'))
    teams_id=Column(String, ForeignKey('teams.id'))
    
    #Relationship
    circuit=relationship('Circuit' ,back_populates='events')
    teams=relationship('Circuit', back_populates='events')
    
    def __repr__(self):
        return f"Event number;{self.id}"\
            +f"Circuit Name: {self.name}"\
            +f"Circuit id;{self.circuit_id}"\
                +f"team id: {self.teams_id}"                  

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
                +f"Circuit Name :{self.name}"\
                +f"Circuit Country: {self.country}"\
                +f"Circuit Laps: {self.laps}"\
                +f"Circuit Previous Winner: {self.previous_winner}"
                
    @classmethod
    def create_circuit(cls, name,country, laps, previous_winner):
     if __name__=='__main__':
        engine=create_engine('sqlite:///F1_Weekend.db')
        Base.metadata.create_all(engine)
        
        Session=sessionmaker(bind=engine)
        session=Session()     
        
        new_circuit=cls(name=name, country=country,laps=laps, previous_winner=previous_winner)
        
        session.add(new_circuit)
        session.commit()    
        
        
    @classmethod
    def delete_circuit(cls,name):
     if __name__=='__main__':
        engine=create_engine('sqlite:///F1_Weekend.db')
        Base.metadata.create_all(engine)
        
        Session=sessionmaker(bind=engine)
        session=Session()
         
        query = session.query(Circuit).filter(Circuit.name==name)
        session.delete(query)
        session.commit()
        
    @classmethod
    def get_all_circuits(cls):
        if __name__ == '__main__':
            # Create the engine and bind it to the session
            engine = create_engine('sqlite:///F1_Weekend.db')
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Query to get all circuits
            all_circuits = session.query(cls).all()
            
            return all_circuits  
    
    def find_by_id(cls, circuit_id):
        if __name__ == '__main__':
            # Create the engine and bind it to the session
            engine = create_engine('sqlite:///F1_Weekend.db')
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Query to find circuit by ID
            circuit = session.query(cls).get(circuit_id)  # Or use filter_by(id=circuit_id).first()
            
            # Optionally close the session after
            session.close()
            
            return circuit
             
             
Circuit.create_circuit('Spa Franco-champs', 'Belgium',43, "Lewis Hamilton")   
                        
class Team(Base):
    __tablename__= 'teams'
   
   #Table Columns 
    id=Column(Integer, primary_key=True)
    name=Column(String, unique=True, nullable=False)
    hometown=Column(String, nullable=False)
    drivers=Column(String, nullable=False)
    engine_manufacturer= Column(String, nullable=False)
     
    #Relationships
    events=relationship('event', back_populates='team') 
    
    def  __repr__(self):
        return f"Team number: {self.id}"\
                +f"Team Name :{self.name}"\
                +f"Team Hometown: {self.hometown}"\
                +f"Team Drivers: {self.drivers}"\
                +f"Engine Manufacturer: {self.engine_manufacturer}"
        
    @classmethod
    def create_team(cls, name,hometown, drivers, engine_manufacturer):
     if __name__=='__main__':
        engine=create_engine('sqlite:///F1_Weekend.db')
        Base.metadata.create_all(engine)
        
        Session=sessionmaker(bind=engine)
        session=Session()     
        
        new_team=cls(name=name, hometown=hometown, drivers=drivers, engine_manufacturer=engine_manufacturer)
        
        session.add(new_team)
        session.commit()    
    
     
    @classmethod
    def delete_team(cls,name):
     if __name__=='__main__':
        engine=create_engine('sqlite:///F1_Weekend.db')
        Base.metadata.create_all(engine)
        
        Session=sessionmaker(bind=engine)
        session=Session()
         
        query = session.query(Team).filter(Team.name==name)
        session.delete(query)
        session.commit()  
    
    
    @classmethod
    def get_all_teams(cls):
        if __name__ == '__main__':
            # Create the engine and bind it to the session
            engine = create_engine('sqlite:///F1_Weekend.db')
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Query to get all teams
            all_teams = session.query(cls).all()
            
            return all_teams 
    
    @classmethod    #Method to find a teams using id
    def find_by_id(cls, id):
        if __name__ == '__main__':
            # Create the engine and bind it to the session
            engine = create_engine('sqlite:///F1_Weekend.db')
            Session = sessionmaker(bind=engine)
            session = Session()
            
            # Query to find teams by ID
            team = session.query(cls).filter_by(id=id).first()
            
            return team          
        
