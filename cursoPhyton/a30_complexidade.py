"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
     <- Constagem de complexidade (ruim)
"""

velocidade = 61  # velocidade do carro atual
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

velocidade_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <=  (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_pass_radar_1

if velocidade_carro_pass_radar_1:
     print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
     print('Carro passou pelo radar 1')

if carro_passou_radar_1 and velocidade_carro_pass_radar_1:
     print('Carro multado em radar 1')