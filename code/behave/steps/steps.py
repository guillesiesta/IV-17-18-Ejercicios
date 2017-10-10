from behave import *
from apuestas import Apuesta

@given('Tenemos Apuesta creada')
def step_impl(context):
    context.apuesta = Apuesta()

@when('Rellenamos la apuesta')
def step_impl(context):
    assert context.apuesta.Apostar("Betis","Sevilla","Martes 13 Junio","2","2") is True

@then('Apuesta realizada!')
def step_impl(context):
    assert context.apuesta.MostrarApuesta() is True
