class Doktorats:
    def __init__(self, nosaukums, pacientuSkaits):
        self.nosaukums=nosaukums
        self.pacientuSkaits=pacientuSkaits
    def ievade(self):
        self.nosaukums=input("Ievadi nosaukumu")
        try:
            self.pacientuSkaits=int(input("Ievadi pacientu skaitu --> "))
        except:
            self.pacientuSkaits=0
        finally:
            print("Ievade veiksmīga", self.pacientuSkaits)

    def izvade(self):
        print(f"Doktorāts {self.nosaukums} apkalpo {self.pacientuSkaits} pacientus.")




# d1=Doktorats("asdad", -325)
# d1.izvade()
# d1.ievade
# d1.izvade
d2 = Doktorats("sssss")
d2.izvade()
d2.ievade
d2.izvade



class Skolotajs:
    stunduSkNedela=0
    skolotajaTips=0
    uzvards="Nezinams"
    klase="x.i"

class SakumskolasSkolotajs(Skolotajs):
    def __init__(self):
        self.skolotajaTips=1
    def izvade(self):
        print(f"Sākumskolas (tips - {self.skolotajaTips})")


class VidusskolasSkolotajs(Skolotajs):
    pirmaisPrieksmets="x prieksmets"
    otraisPrieksmets="y prieksmets"
    pirmaisPrieksmetsStundas=0
    otraisPrieksmetsStundas=0



ss1=SakumskolasSkolotajs()
ss1.izvade()


