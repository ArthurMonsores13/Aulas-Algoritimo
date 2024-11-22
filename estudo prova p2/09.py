def eh_palindromo(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  # Ignorar espaços e pontuações
    return s == s[::-1]

print(eh_palindromo("ovo"))