from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email
# representation o repr nombra a los usuarios al print, con query.all por ejemplo
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    uid = db.Column(db.String(10), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship(User)  como??


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    url = db.Column(db.String(250), nullable=False)
    # favoritos_id = db.Column(Integer, ForeignKey('favoritos.id'))
    # favoritos = relationship(Favoritos)
    # planets_id = db.Column(Integer, ForeignKey('planets.id'))
    # planets = relationship('Planets')
    #desde swapi tech cada personaje tiene su url pero no su uid ese viene con el primer fetch... ponerlo o no?


class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(250))
    vehicle_class = db.Column(db.String(250))
    passengers = db.Column(db.Integer)
    pilots = db.Column(db.String(250))
    url = db.Column(db.String(250), unique=True, nullable=False)
    # favoritos_id = Column(Integer, ForeignKey('favoritos.id'))
    # favoritos = relationship(Favoritos)
    # people_id = Column(Integer, ForeignKey('people.id'))
    # people = relationship(People)


class Planets(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    url = db.Column(db.String(250), unique=True, nullable=False)
    # favoritos_id = db.Column(db.Integer, ForeignKey('favoritos.id'))
    # favoritos = relationship(Favoritos)