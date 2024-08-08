class Weapon:
    def __init__(self,id,name,model,manufacturer,cost_in_credits,length,type,description,films):
        self.id=id
        self.name=name
        self.model=model
        self.manufacturer=manufacturer
        self.cost_in_credits=cost_in_credits
        self.length=length
        self.type=type
        self.description=description
        self.films=films

    def mostrar_att(self):
        print(f'''
|----------------------------------------------------------------------------------------------|
Se ha registrado el arma "{self.name}"
|----------------------------------------------------------------------------------------------|             

                Descripción del arma:
              
                {self.description}

''')  