# fun��o para calcular tempo com base na distancia e velocidade media
# tempo = distancia / velocidade media

class Person(object):
  name: str
  def __init__(self, name: str) -> None:
    self.name = name
  def __eq__(self, other: object) -> bool:
    print('__eq__ called')
    if isinstance(other, Person):
      if other.name == self.name:
        return True
    return False
  def __ne__(self, other: object) -> bool:
    print('__ne__ called')
    return not self.__eq__(other)
  def __str__(self) -> str:
    return f"Person {self.name}"
  def get_name(self):
    return self.name



def calcula_tempo_entre(distancia, velocidade_media):
  tempo_em_horas = distancia / velocidade_media
  tempo_em_minutos = tempo_em_horas * 60
  minutos_resto = tempo_em_minutos % 60
  horas_exatas = tempo_em_minutos // 60
  return f"{horas_exatas} horas e {minutos_resto} minutos" \
    if \
      horas_exatas > 0 \
    else \
      f"{minutos_resto} minutos"

# 400 km, 40 km/h
print(calcula_tempo_entre(400, 40))
# 10.0 horas e 0.0 minutos

# 4 km, 40 km/h
print(calcula_tempo_entre(4, 40))
# 6.0 minutos

# 4 km, 15 km/h
print(calcula_tempo_entre(4, 15))
# 16.0 minutos

print(calcula_tempo_entre(4, 0))
# ZeroDivisionError: division by zero
