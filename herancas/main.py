from ingresso import Ingresso
from ingresso_vip import IngressoVip

valor_padrão = 59.99

ingresso_normal = Ingresso(valor_padrão)
ingresso_vip = IngressoVip(valor_padrão, 120.00)

print(ingresso_normal)
print(ingresso_vip)
