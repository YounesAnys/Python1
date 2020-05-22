#Auteur : Anys Younes
#Numero d'étudiant : 300145843
def celsius_en_Fahrenheit(temp_Celsius):
    temp_Fahrenheit = 9.0 / 5.0 * temp_Celsius +32
    return temp_Fahrenheit

temp_Celsius = float(input("Entrez la temperature en Celsius"))
temp_Fahrenheit = celsius_en_Fahrenheit(temp_Celsius)

print(temp_Celsius, "Celsius est", temp_Fahrenheit, "Fahrenheit.")

