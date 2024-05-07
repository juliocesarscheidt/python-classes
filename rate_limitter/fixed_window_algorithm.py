from time import time, sleep


def forward(packet):
  print("Packet Forwarded: " + str(packet))

def drop(packet):
  print("Packet Dropped: " + str(packet))


class FixedWindow:
  def __init__(self, capacity, window_size, forward_callback, drop_callback):
    self.capacity = capacity
    self.window_size = window_size
    
    # janela inicial
    self.current_window = [0, self.window_size]
    
    self.allowed_within_window = 0
    
    self.forward_callback = forward_callback
    self.drop_callback = drop_callback

  def handle(self, packet):
    # print('---------------------------------')
  
    # verifica se podemos aceitar o pacote ao estar dentro da janela atual
    inside_curr_window = \
      packet >= self.current_window[0] and \
      packet <= self.current_window[1]
    
    # dentro da janela atual, devemos verificar se ha capacidade para aceitar ou nao
    if inside_curr_window:
      if self.allowed_within_window < self.capacity:
        self.allowed_within_window += 1
        return self.forward_callback(packet)
      else:
        return self.drop_callback(packet)
    
    # para uma nova janela, resetamos os pacotes e ajustamos a janela
    else:
      # move a janela atual
      self.current_window[0] += self.window_size
      self.current_window[1] += self.window_size

      if self.capacity > 0:
        # o contador de pacotes aceitos vira 1,
        # pois iremos aceitar este primeiro pacote na nova janela
        self.allowed_within_window = 1
        return self.forward_callback(packet)
      else:
        self.allowed_within_window = 0
        return self.drop_callback(packet)


# rate limiter com limite de aceitar 2 pacotes a cada 10 unidades de tempo
rate_limitter1 = FixedWindow(2, 10, forward, drop)

packet = 1
while True:
  # enviando 10 pacotes por segundo - 0.1 secs
  sleep(0.1)
  rate_limitter1.handle(packet)
  packet += 1
  if packet >= 30:
    break

"""
Packet Forwarded: 1
Packet Forwarded: 2
Packet Dropped: 3
Packet Dropped: 4
Packet Dropped: 5
Packet Dropped: 6
Packet Dropped: 7
Packet Dropped: 8
Packet Dropped: 9
Packet Dropped: 10
Packet Forwarded: 11
Packet Forwarded: 12
Packet Dropped: 13
Packet Dropped: 14
Packet Dropped: 15
Packet Dropped: 16
Packet Dropped: 17
Packet Dropped: 18
Packet Dropped: 19
Packet Dropped: 20
Packet Forwarded: 21
Packet Forwarded: 22
Packet Dropped: 23
Packet Dropped: 24
Packet Dropped: 25
Packet Dropped: 26
Packet Dropped: 27
Packet Dropped: 28
Packet Dropped: 29
"""

print('')

# rate limiter com limite de aceitar 5 pacotes a cada 10 unidades de tempo
rate_limitter2 = FixedWindow(5, 10, forward, drop)

"""
  sequencia sem o 6 e 7 ::
  [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  neste caso deve atender 5 pacotes do 1 ao 10 mesmo sem haver o 6 e 7,
  e a partir do 11 comecar uma nova janela
"""
for p in [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
  rate_limitter2.handle(p)

"""
Packet Forwarded: 1
Packet Forwarded: 2
Packet Forwarded: 3
Packet Forwarded: 4
Packet Forwarded: 5
Packet Dropped: 8
Packet Dropped: 9
Packet Dropped: 10
Packet Forwarded: 11
Packet Forwarded: 12
Packet Forwarded: 13
Packet Forwarded: 14
Packet Forwarded: 15
Packet Dropped: 16
Packet Dropped: 17
Packet Dropped: 18
Packet Dropped: 19
Packet Dropped: 20
"""
