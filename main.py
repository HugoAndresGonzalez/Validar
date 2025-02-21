#Función para validar números, convertirlos a tipo de dato elegido y definir si aceptamos negativos o no
def validar_nums(tipo_a_convertir,pregunta,rango=float('inf')):
  while True:
    try:
      respuesta=tipo_a_convertir(input(pregunta))
      if (rango == 0 and respuesta < 0) :
        print("valor no valido(ingresaste un negativo),vuelve a intentarlo: ")
      else:return respuesta
    except ValueError:print("Igresaste letras, debes ingresar números, vuelve a intentarlo: ")
answer=(validar_nums(float,"ingresa un digito: ",0))
