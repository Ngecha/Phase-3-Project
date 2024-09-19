from sqlalchemy import create_engine,CheckConstraint, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base=declarative_base()


#Circuit Model
class Circuit(Base):
    __tablename__="circuits"
    __table_args__= (
            CheckConstraint(
            'laps BETWEEN 20 AND 30',
            name='laps_between_20_and_30')
    )
            
    
    id=Column(Integer, primary_key=True )
    name=Column(String,nullable=False, unique=True)
    country=Column(String,nullable=False)
    laps=Column(Integer,nullable=False)
    previous_winner=Column(String,nullable=True)
    
    #One to one Relationship
    events=relationship('event', back_populates='circuit')
    
    def  __repr__(self):
        return f"Circuit number: {self.id}"\
                +f"Circuit Name :{self.name}"\
                +f"Circuit Country: {self.country}"\
                +f"Circuit Laps: {self.laps}"\
                +f"Circuit Previous Winner: {self.previous_winner}"
                
    @classmethod
    def create_circuit(cls, name,country, laps, previous_winner):
     if __name__=='__main__':
        engine=create_engine('sqlite: ///F1_Weekend.db')
        Base.metadata.create_all(engine)
        
        Session=sessionmaker(bind=engine)
        session=Session()     
        
        new_circuit=cls(name=name, country=country,laps=laps, previous_winner=previous_winner)
        
        session.add(new_circuit)
        session.commit()    
        
    @classmethod
    def delete_circuit(cls,name):
     if __name__=='__main__':
        engine=create_engine('sqlite: ///F1_Weekend.db')
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
                
                        