import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKasspaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luodun_kassapäätteen_rahamäärä_ja_myytyjen_lounaiden_määrä_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_kateismaksu_edullinen_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateismaksu_edullinen_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateismaksu_maukas_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateismaksu_maukas_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttimaksu_edullinen_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttimaksu_edullinen_ei_riita(self):
        self.kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttimaksu_maukas_riittaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttimaksu_maukas_ei_riita(self):
        self.kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1)
        self.assertEqual(self.kortti.saldo, 1001)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100001)