#!/usr/bin/python3
import uuid
from datetime import datetime

"""A los atributos que inicializan una lista, hay que ponerles metodos para unir tipo:
def add_amenity(self, amenity):
        self.amenities.append(amenity)

para que funcione la lista"""

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class User(BaseModel):
    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

class Place(BaseModel):
    def __init__(self, name, description, address, city, latitude, longitude, host_id, num_rooms, num_bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []
        """No tengo idea si este reviews va aqui o se qutia ya que hay una clase para eso y no se si hara conlficto o que onda"""
        self.reviews = []

class Amenities(BaseModel):
    def __init__(self, amenities):
        super().__init__)
        self.amenities = []

"""Aqui esta el otro sin contar que aqui review recibe mas valores"""
class Review(BaseModel):
    def __init__(self, stars, review):
        super().__init__)
        self.stars = stars
        self.review = []

class City(BaseModel):
    def __init__(self, name, country):
        super().__init__)
        self.country = country
        self.name = name
