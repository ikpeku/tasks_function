'''A program to convert temperature of value from farenheit to celsius'''
def Farenheit(farenheit):
    """return the value of Celsius"""
    celsuis = (farenheit - 32) * (5/9)
    return (f'{num_of_Farenheit} degree Farenheit = {round(celsuis,2)} degree celsius')
    
    
num_of_Farenheit = float(input("input number of farenheit: "))   
print(Farenheit(num_of_Farenheit))

