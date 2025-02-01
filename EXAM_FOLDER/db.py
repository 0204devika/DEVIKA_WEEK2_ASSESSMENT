from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self,data):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self,data):
        pass
class SQL(IDatabaseOperations):
    def insert(self,data):
        self.data=data
        print("data inserted successfully")
    def update(self):
        print("data updated successfully")
    def delete(self,data):
        self.data=data
        print("data deleted successfully")
class NoSQL(IDatabaseOperations):
    def insert(self,data):
        self.data=data
        print("data inserted successfully")
    def update(self):
        print("data updated successfully")
    def delete(self,data):
        self.data=data
        print("data deleted successfully")
s=SQL()
s.insert("abc")
n=NoSQL()
n.delete("xyz")
    
        
        
    