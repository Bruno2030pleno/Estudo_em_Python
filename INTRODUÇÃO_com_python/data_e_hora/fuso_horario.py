# programa 9.14
# mostra a data atual em diversos fusos horarios
from zoneinfo import ZoneInfo as z
from datetime import datetime as t
from datetime import timezone

# 1. Nomes corrigidos seguindo o padrão IANA (Continente/Cidade)
bruxelas = z('Europe/Brussels')
new_york = z('America/New_York')
tokio = z('Asia/Tokyo')
manaus = z('America/Manaus')
brasilia = z('America/Sao_Paulo') # Fuso oficial para o horário de Brasília
rio_branco = z('America/Rio_Branco')


# 2. Capturando o horário atual em UTC (melhor prática)
agora = t.now(timezone.utc)

print('agora em:')
print('bruxelas :', agora.astimezone(bruxelas))
print('new york :', agora.astimezone(new_york))
print('tokio :', agora.astimezone(tokio))

print('\nagora brasil: ')
print('manaus :', agora.astimezone(manaus))
print('brasilia :', agora.astimezone(brasilia))
print('rio branco :', agora.astimezone(rio_branco))

import zoneinfo

for zone in sorted(zoneinfo.available_timezones()):
    print(zone)