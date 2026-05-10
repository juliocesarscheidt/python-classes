import unicodedata

# Normalization Form Compatibility Decomposition
  #   NF – Normalization Form (formato de normalização)
  #   C – Composition (composição – une)
  #   D – Decomposition (decomposição – separa)
  #   K – Compatibility (separa por compatibilidade)


['U+' + hex(ord(letter))[2:].zfill(4).upper() for letter in 'café']
# ['U+0063', 'U+0061', 'U+0066', 'U+00E9']
# U+00E9 é  -> https://www.compart.com/en/unicode/U+00E9


['U+' + hex(ord(letter))[2:].zfill(4).upper() for letter
  in unicodedata.normalize("NFC", 'café')]
# ['U+0063', 'U+0061', 'U+0066', 'U+00E9']
# U+00E9 é  -> https://www.compart.com/en/unicode/U+00E9


# separa os caracteres dos acentos
['U+' + hex(ord(letter))[2:].zfill(4).upper() for letter
  in unicodedata.normalize("NFD", 'café')]
# ['U+0063', 'U+0061', 'U+0066', 'U+0065', 'U+0301']
# U+0065 e  -> https://www.compart.com/en/unicode/U+0065
# U+0301 ´  -> https://www.compart.com/en/unicode/U+0301


# separa os caracteres, mas no encode pro utf-8 os acentos sao mantidos
unicodedata.normalize("NFD", 'café').encode("utf-8", "ignore").decode("utf-8")
# 'café'
unicodedata.normalize("NFKD", 'café').encode("utf-8", "ignore").decode("utf-8")
# 'café'


# separa os caracteres, mas aqui ficara sem acentos pois ASCII nao tem acentos
unicodedata.normalize("NFD", 'café').encode("ASCII", "ignore").decode("ASCII")
# 'cafe'
unicodedata.normalize("NFKD", 'café').encode("ASCII", "ignore").decode("ASCII")
# 'cafe'


def remove_accents(text):
  return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII")


print(remove_accents('café'))
# cafe


def remove_diacritics_preserve_script(text):
  """
  Remove diacritics while preserving the original script.
  Works for Arabic, Greek, and other non-Latin scripts.
  """
  # Normalize to NFD (Canonical Decomposition)
  # This separates base characters from combining marks
  nfd_form = unicodedata.normalize('NFD', text)

  # Filter out combining marks (category 'Mn')
  # This removes diacritics while keeping base characters
  filtered = ''.join(
    char for char in nfd_form 
    if unicodedata.category(char) != 'Mn'
  )

  # Normalize back to NFC (Canonical Composition) for consistency
  return unicodedata.normalize("NFC", filtered)

print(remove_diacritics_preserve_script("Café Júlio César"))
# Cafe Julio Cesar
