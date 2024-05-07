import faker
def Reg_up_data_rnd():
    fake = faker.Faker()
    name = fake.name()
    email = fake.email()
    password = fake.password()
    return name,email,password

def Sing_up_data_rnd():
    name = 'Dmitriy'
    email = 'Dmitriy_Kondakov_565@ya.ru'
    password = 1234567
    return name, email, password


