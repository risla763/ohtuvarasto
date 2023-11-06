import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    #tämä testaa alkusaldoa, joka on pienempi kuin 0 MIKS TÄÄ EI TOIMI??
    def test_negatiivinen_alku_saldo(self):
        varasto = Varasto(10,-1)
        self.assertEqual(varasto.saldo,0.0)

    #tässä uusi testi testaa sitä että annetaan negatiivinen tilavuus
    def test_annetaan_negatiivinen_tilavuus(self):
        varasto = Varasto(-5)
        self.assertEqual(varasto.tilavuus,0.0)

    #tässä testataan että lisää jotain joka on alle nollan
    def test_negatiivinen_lisays(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #tässä testataan että lisää jotain joka on yli maksimi määrän
    def test_liian_iso_lisays(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus-self.varasto.saldo+3)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    #tässä testataan että lisää negatiivisen määrän MENEEKÖ TÄMÄ TESTI LÄPI?
    def test_negatiivinen_lisays(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    #testaa että ottaa varastosta negatiivisen määrän
    def test_ottaa_varastosta_negatiivisen_maaran(self):
        varasto = Varasto(10)
        self.assertEqual(varasto.ota_varastosta(-1), 0.0)

    #testaa että ottaa varastosta isomman määrän kuin siellä on saldoa
    def test_ottaa_varastosta_saldon_yli(self):
        varasto = Varasto(10)
        self.assertEqual(varasto.ota_varastosta(varasto.saldo+2), varasto.saldo)
        self.assertAlmostEqual(varasto.saldo, 0.0)
        print("muutos")

    def test_string_varasto(self):
        varasto = Varasto(10)
        self.assertEqual(str(varasto),varasto.__str__())

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
