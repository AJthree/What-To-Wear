# Project: What to wear

temperature = int(input('What is the current temperature? '))

if temperature >= 80:
    outfit = 'shorts and pack your sunglasses'

elif temperature <= 79 and temperature >= 55:
    outfit = 'a light jacket'

elif temperature <= 54 and temperature >= 10:
    outfit = 'a coat in addition to a hat, gloves, and scarf'

elif temperature == 9 and temperature <= 9:
    outfit = 'anything you want and just lie by the fireplace and stay inside!'

advice = (f"""

Today you should wear {outfit}. """)

print(advice)
