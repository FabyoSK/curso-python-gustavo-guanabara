"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista.

No final, mostre:
a. Quantas pessoas foram cadastradas
b. A média de idade do grupo
c. uma lista com todas as mulheres
d. uma lista com todas as pessoas com idade acima da média.
"""

person_dict = dict()
general_info = list()
names = list()
names_quantity = list()
ages = list()
women = list()
above_mean = list()
counter = 0

while True:
    person_dict['name'] = input("Nome: \n")

    # sex = input("Sexo [M/F]: \n")
    # sex = sex[0].upper()
    # person_dict['sex'] = sex

    person_dict['age'] = float(input("Idade: \n"))
    

    general_info.append(person_dict.copy())

    leave = input("Continuar? [S/N] \n")
    leave = leave.upper()
    if leave[0] == "N":
        print(general_info)
        break

# a.: quantas pessoas foram cadastradas:
for dictionary in general_info:
    names_quantity.append(dictionary.get("name"))
print(f"Pessoas cadastradas: {len(names_quantity)}")

# b.: a média de idade do grupo:
# for dictionary in general_info:
#     ages.append(dictionary.get("age"))
#     age_mean = sum(ages)/len(ages)
# print(f"Média de idade do grupo: {age_mean:.1f} anos.")

# c.: uma lista com todas as mulheres:

# for dictionary in general_info:
#     for key, value in dictionary.items():
#         if value == "F":
#             women.append(dictionary.get("name"))
# print(f"Lista com todas as mulheres: {women}")


# d.: uma lista com todas as pessoas com idade acima da média:
# for dictionary in general_info:
#     if dictionary.get("age") > (age_mean):
#         above_mean.append(dictionary.get("name"))
# print(above_mean)