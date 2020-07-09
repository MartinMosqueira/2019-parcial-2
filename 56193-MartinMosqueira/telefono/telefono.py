
class Telefono():
    def __init__(self):
        self.agregar=False
        self.credito=0
    
    
    def dial(self,numero):
        if len(numero)== 3:
            if numero[0] == '9' or numero[0] == '8':
                return True
        
        if len(numero) == 7:
            if self.agregar == True:
                if self.credito > 10:
                    self.credito=self.credito-10
                    return True
                else:
                    return False
            else:
                return False
        
        if numero[0] == '0' and numero[1] == '0':
            if self.agregar == True:
                if self.credito > 100:
                    self.credito=self.credito-100
                    return True
                else:
                    return False
            else:
                return False
            
    
    def agregar_credito(self,credito):
        
        if credito > 10 or credito > 100:
            self.agregar=True
            self.credito=credito
