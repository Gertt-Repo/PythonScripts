import string

def encrypt(message, key):

  shift = key % 26
  cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

  encrypted_message = message.lower().translate(cipher)

  return encrypted_message

def decrypt(encrypted_message, key):

  shift = 26 - (key % 26)
  cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[shift])

  message = encrypted_message.translate(cipher)
  return message

  message = 'Follow to Gertt Repo'
  key = 3

  encrypted_message = encrypt(message, key)
  print(f'Encrypted message: {encrypted_message}')

  decrypted_message = decrypt(message, key)
  print(f'Decrypted message: {decrypted_message}')