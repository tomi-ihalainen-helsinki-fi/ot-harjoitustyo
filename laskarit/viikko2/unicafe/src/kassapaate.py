class Kassapaate:
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def __kateismaksu(self, maksu, onEdullinen):
        hinta = self.__hae_hinta(onEdullinen)

        if maksu >= hinta:
            self.kassassa_rahaa = self.kassassa_rahaa + hinta
            self.__lisaa_lounas(onEdullinen)
            return maksu - hinta
        
        return maksu

    def __korttimaksu(self, kortti, onEdullinen):
        hinta = self.__hae_hinta(onEdullinen)

        if kortti.saldo >= hinta:
            kortti.ota_rahaa(hinta)
            self.__lisaa_lounas(onEdullinen)
            return True
        
        return False

    def __hae_hinta(self, onEdullinen):
        if onEdullinen:
            return 240

        return 400

    def __lisaa_lounas(self, onEdullinen):
        if onEdullinen:
            self.edulliset += 1
        else:
            self.maukkaat += 1

    def syo_edullisesti_kateisella(self, maksu):
        return self.__kateismaksu(maksu, True)

    def syo_maukkaasti_kateisella(self, maksu):
        return self.__kateismaksu(maksu, False)


    def syo_edullisesti_kortilla(self, kortti):
        return self.__korttimaksu(kortti, True)

    def syo_maukkaasti_kortilla(self, kortti):
        return self.__korttimaksu(kortti, False)

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
