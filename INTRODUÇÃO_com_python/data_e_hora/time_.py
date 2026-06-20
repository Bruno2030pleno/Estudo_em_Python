import datetime as t
# tempo = t.date.today()
# print(tempo)

# tempo1 = t.datetime.now().time()
# print(tempo1)



momento = t.datetime.now()
print(f' hora {momento.hour} minutos {momento.minute} segundos {momento.second}')
print(f'dia da semana {momento.isoweekday()}')
print(f'formato em string {momento.isoformat()}')
def dia():
    data = t.date(year=2026, day=9, month=6)
    print(data)
dia()    

tempo = t.datetime.now()
print(tempo)