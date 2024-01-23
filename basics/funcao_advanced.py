# função para calcular tempo com base na distancia e velocidade media
# tempo = distancia / velocidade media

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
16.0 minutos

print(calcula_tempo_entre(4, 0))
# ZeroDivisionError: division by zero
