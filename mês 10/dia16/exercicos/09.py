def eh_palindromo(texto):
  """Verifica se uma string é um palíndromo.

  Args:
    texto: A string a ser verificada.

  Returns:
    True se a string for um palíndromo, False caso contrário.
  """

  # Remover espaços e transformar tudo para minúsculas
  texto = texto.replace(" ", "").lower()
  
  # Inverter a string
  texto_invertido = texto[::-1]
  print(texto_invertido)

  # Comparar a string original com a invertida
  if texto == texto_invertido:
      return True
  else:
      return False

texto1 = "radar"
texto2 = "Python"

print(eh_palindromo(texto1))  # Output: True
print(eh_palindromo(texto2))  # Output: False