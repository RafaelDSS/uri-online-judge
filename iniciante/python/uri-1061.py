def segundos_para_hhmmss(segundos):
    dias = segundos // (3600 * 24)
    resto = segundos % (3600 * 24)
    horas = resto // 3600
    resto = resto % 3600
    minutos = resto // 60
    segundos = resto % 60

    return (dias, horas, minutos, segundos)


dia_inicio = input().split(" ")[1]
hora_inicio, minuto_inicio, segundo_inicio = input().split(" : ")

dia_fim = input().split(" ")[1]
hora_fim, minuto_fim, segundo_fim = input().split(" : ")


data_para_segundos = lambda dia, hora, minuto, segundo: (int(dia) * 24 * 60 * 60) + (int(hora) * 60 * 60) + (int(minuto) * 60) + int(segundo)


segundos_inicio = data_para_segundos(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio)
segundos_fim = data_para_segundos(dia_fim, hora_fim, minuto_fim, segundo_fim)

segundos_restantes = segundos_fim - segundos_inicio

dia, hora, minuto, segundo = segundos_para_hhmmss(segundos_restantes)

print(f"{dia} dia(s)")
print(f"{hora} hora(s)")
print(f"{minuto} minuto(s)")
print(f"{segundo} segundo(s)")
