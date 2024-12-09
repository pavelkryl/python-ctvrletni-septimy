class Zak:

	def __init__(self, jmeno, prijmeni, rodne_cislo):
		self.jmeno = jmeno
		self.prijmeni = prijmeni
		self.rodne_cislo = rodne_cislo
		
class Skola:
	
    def __init__(self):
        self._zaci = []

    def pridej(self, zak):
        self._zaci.append(zak)

    def najdi(self, rodne_cislo):
        for z in self._zaci:
            if z.rodne_cislo == rodne_cislo:
                return z
        return None


# zkusebni kod
skola = Skola()	
z = Zak("Karel", "Svoboda", "1122335566")
skola.pridej(z)

print(skola.najdi("1122335566").jmeno)
