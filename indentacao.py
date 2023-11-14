class Pendrive(object): # A classe pai Pendrive() 
    def __init__(self, tamanho, interface='2.0'):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player(Pendrive): # A classe filha MP3Player() que herda os atributos 

    def __init__(self, tamanho, interface='2.0', turner = False):
        self.turner = turner
        Pendrive.__init__(self, tamanho, interface)

mp3 = MP3Player(1024)
print(mp3.tamanho, mp3.interface, mp3.turner)




