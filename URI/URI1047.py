from datetime import timedelta as td
from datetime import datetime as dt

# LEITURA DOS INPUTS:

line = input().split()
startHour = int(line[0])
startMin = int(line[1])
finalHour = int(line[2])
finalMin = int(line[3])

# CÁLCULO DO DELTA-TEMPO:

duration = td(hours = finalHour, minutes = finalMin) - td(hours = startHour, minutes = startMin)

# SE O JOGO COMEÇAR EM UM DIA X E TERMINAR NO DIA X+1:

if duration < td(0):
    duration += td(days = 1)

# CONVERSÃO DO DELTA-TEMPO ENTRE TIPOS PARA PERMITIR MANIPULAÇÃO DA STRING FINAL:

duration = str(duration)
durationObj = dt.strptime(duration, '%H:%M:%S').time()

# FORMATAÇÃO COMO O URI PEDE:

durationHourList = list(durationObj.strftime('%H'))

if durationHourList[0] == "0":
    del durationHourList[0]

durationMinList = list(durationObj.strftime('%M'))

if durationMinList[0] == "0":
    del durationMinList[0]

# CASO ESPECIAL (JOGO DURANDO EXATAMENTE 24H (DURAÇÃO MÁXIMA)):

if durationHourList[0] == "0" and durationMinList[0] == "0":
    durationHourList[0] = "24"

print("O JOGO DUROU " + "".join(durationHourList) + " HORA(S) E " + "".join(durationMinList) + " MINUTO(S)")