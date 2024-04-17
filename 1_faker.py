# 
# Uzdevums: Izmantojot bibliotēku Faker uzģenerēt fake datus
# https://faker.readthedocs.io/en/master/
# https://faker.readthedocs.io/en/stable/providers.html
# 
# Uzinstalē bibliotēku ievadot terminālī
# > pip install Faker
#
from faker import Faker
fake = Faker()
while True:
    print("\nNejaušo datu ģenerators:")
    print("1. 5 personu vārdi un uzvārdi")
    print("2. 5 personu vārdi un uzvārdi latviešu valodā")
    print("3. 5 persona vārdi un uzvārdi ar telefona numuru, adresi un personas kodu")
    print("4. Teksts dotā maksimāla garumā") # lietotājs ievada maksimalo garumu
    print("5. 5 Dazādas cenas") # valūtas zīme un summa
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        for _ in range(5):
            print(fake.name())
    elif choice == "2":
        fake = Faker('lv_LV')
        for _ in range(5):
            print(fake.name())
    elif choice == "3":
        for _ in range(5):
            print(fake.name(),fake.address(),fake.phone_number(),fake.ssn())  
    elif choice == "4":
        print(fake.text(100))
    elif choice == "5":
        for _ in range(5):
            print(fake.pricetag())
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")