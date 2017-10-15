from apuestas import Apuesta


def test_Apostar():
    apuesta = Apuesta()
    assert apuesta.Apostar("Betis", "Sevilla", "Martes 13 Junio", "2", "2") is True


def test_MostrarApuesta():
    apuesta = Apuesta()
    assert apuesta.MostrarApuesta() is True


def test_ApuestaAcertada():
    apuesta1 = Apuesta()
    apuesta1.Apostar("Betis", "Sevilla", "Martes 13 Junio", "2", "2")
    apuesta2 = Apuesta()
    apuesta2.Apostar("Betis", "Sevilla", "Martes 13 Junio", "2", "2")

    assert apuesta1.ApuestaAcertada(apuesta1, apuesta2) is True
