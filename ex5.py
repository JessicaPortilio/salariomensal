sal = float(input("Informe o valor recebido por hora de trabalho: "))
htrab = float(input("Número de horas trabalhadas por dia: "))
sal_dia = sal * htrab
sal_mes = sal_dia * 30
print("O salário mensal será de %.2f" %sal_mes)