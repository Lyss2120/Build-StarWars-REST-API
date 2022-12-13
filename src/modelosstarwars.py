class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False)


class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)  # id del personaje
    # name del personaje vehiculo o planeta
    name = Column(String(250), nullable=False)
    uid = Column(String(5))
    url = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.###
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    url = Column(String(250), nullable=False)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    favoritos = relationship(Favoritos)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets')



class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    vehicle_class = Column(String(250))
    passengers = Column(Integer)
    pilots = Column(String(250))
    url = Column(String(250), nullable=False)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    favoritos = relationship(Favoritos)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)



class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
    url = Column(String(250), nullable=False)
    favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    favoritos = relationship(Favoritos)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
