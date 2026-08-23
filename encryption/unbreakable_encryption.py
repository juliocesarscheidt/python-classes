from typing import Tuple
from secrets import token_bytes

def generate_random_key(length: int) -> int:
  tb = token_bytes(length)
  return int.from_bytes(tb, "big")

def encrypt(random_key: int, original: str) -> int:
  original_bytes = original.encode()
  # print("original_bytes", original_bytes)
  # b'Hello World'

  original_key = int.from_bytes(original_bytes, "big")
  # print("original_key", original_key)
  # 87521618088882533792115812

  # XOR -> 1^1=0 / 0^0=0 / 1^0=1 / 0^1=1
  # A ^ B = C
  # C ^ B = A
  # C ^ A = B
  encrypted_key = original_key ^ random_key
  # print("encrypted_key", encrypted_key)
  # 84086130982047758896179470

  return encrypted_key

def decrypt(random_key: int, encrypted_key: int) -> str:
  original_key = random_key ^ encrypted_key
  # print("original_key", original_key)
  # 87521618088882533792115812

  # +7 to make sure we round up to the nearest byte
  decrypted_size = (original_key.bit_length()+7) // 8
  # print("decrypted_size", decrypted_size)
  # 11

  original_bytes = original_key.to_bytes(decrypted_size, "big")
  # print("original_bytes", original_bytes)
  # b'Hello World'

  return original_bytes.decode()

if __name__ in "__main__":
  original = "Hello World"
  # original_bytes = original.encode()

  random_key = 16814025581319699169527146
  # random_key = generate_random_key(len(original_bytes))
  # print("random_key", random_key)

  encrypted_key = encrypt(random_key, original)
  print("encrypted_key", encrypted_key)
  # 84086130982047758896179470

  original = decrypt(random_key, encrypted_key)
  print("original", original)
