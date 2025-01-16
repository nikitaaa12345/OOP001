from abc import abstractmethod


class Dzivnieki:
    def __init__(self, vards,kajas):
        self.vards=vards
        self.kajas=kajas
    @abstractmethod
    def skanja(self):
        print("random animal noise")
    def __str__(self):
        return f"{self.vards} un {self.kajas} kajas"


class Suns(Dzivnieki):
    def __init__(self,vards,kajas):
        super().__init__(vards,kajas)
        self.vards="Komisars "+self.vards
    def skanja(self):
        print("Vau vau")

class Kakjis(Dzivnieki):
    def __init__(self, vards, kajas):
        super().__init__(vards, kajas)
        self.vards = "Minkans " + self.vards
    def skanja(self):
        print("MurMjau")

class Govs(Dzivnieki):
    def skanja(self):
        print("MUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")

d1=Dzivnieki("Gauja",4)
print(d1)
d1.skanja()


s1=Suns("Reksis",4)
print(s1)
s1.skanja()

s2=Kakjis("Muris", 4)
print(s2)
s2.skanja()
dzivniekuSaraksts=[]
dzivniekuSaraksts.append(Suns("Reksis", 3))
dzivniekuSaraksts.append(Suns("Volvis",4))
dzivniekuSaraksts.append(Suns("Caps", 4))
dzivniekuSaraksts.append(Kakjis("Murcis", 4))
dzivniekuSaraksts.append(Kakjis("Burkaans", 4))
dzivniekuSaraksts.append(Govs("Gauja", 4))



print("#####################")
for dzivnieks in dzivniekuSaraksts:
    print(dzivnieks)
    dzivnieks.skanja()


