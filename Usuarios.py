class User():

    def __init__(self, first_name, last_name, city, language, years_old):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.language = language
        self.years_old = years_old

    def describe_user(self):
        print(self.first_name + self.last_name + "\n" + self.city + "\n" + self.language + "\n" + str(self.years_old))

    def greet_user(self):
        print("Olá " + self.first_name + " " + self.last_name + " você tem " + str(self.years_old) + " de idade " + ",fala " + self.language + " e mora em " + self.city)
