class Dog:

    def __init__(self,name,favorite_toy="any"):

        self.known = name
        self.toy = favorite_toy

pauline = Dog("fido", "Tennis ball")
print(pauline.known) 
print(pauline.toy)  
     