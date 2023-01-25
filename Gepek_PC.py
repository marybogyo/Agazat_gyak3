class Gepek_PC:

    def __init__(self, gep):
        self.id = int(gep[0])
        self.hely = gep[1]
        self.tipus = gep[2]
        self.ipcim = gep[3]


    def __str__(self):
        return f"{self.id}, {self.hely}, {self.tipus}, {self.ipcim}"
