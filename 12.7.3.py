money = int(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ':4.28, 'СБЕР': 4.0}
deposit = [int(per_cent.get("ТКБ")*money/100),
           int(per_cent.get("СКБ")*money/100),
           int(per_cent.get("ВТБ")*money/100),
           int(per_cent.get("СБЕР")*money/100)]
deposit = list(map(round, deposit))
print(list(deposit))

deposit_max = max(deposit)
print('Максимальная сумма депозита', deposit_max)
