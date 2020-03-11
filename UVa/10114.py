loan = input().split()
loan_duration = int(loan[0])

while loan_duration >= 0:
    down_pay = float(loan[1])
    loan_amount = float(loan[2])
    parcela = loan_amount/float(loan_duration)
    number_of_records = int(loan[3])
    initial_value = loan_amount + down_pay
    deprecated_value = initial_value
    
    dicio_mes = {}

    for j_record in range(number_of_records):
        current_record_line = input().split()
        dicio_mes[int(current_record_line[0])] = float(current_record_line[1])
    
    full_dict = {}

    lista_de_meses = list(range(loan_duration+1))
    for mes in lista_de_meses:
        if mes not in dicio_mes.keys():
            full_dict[mes] = ""
        else:
            full_dict[mes] = dicio_mes[mes]
        if full_dict[mes] == "":
            full_dict[mes] = full_dict[mes-1]

    for mes in lista_de_meses:
        depreciation_percentage = full_dict[mes]
        deprecated_value *= (1 - depreciation_percentage)
        if mes != 0:
            loan_amount -= parcela
        if (deprecated_value >= loan_amount):
            break

    if (mes > 1) or (mes < 1):
        print(str(mes) + " months")
    else:
        print("1 month")

    loan = input().split()
    loan_duration = int(loan[0]) 