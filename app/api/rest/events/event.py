import uuid

class Event:
    def __init__(self,name,description,location,url,price,category,time):
        self.id= str(uuid.uuid4())
        self.name=name
        self.description = description
        self.location = location
        self.url = url
        self.price = price    
        self.category = category
        self.time = time