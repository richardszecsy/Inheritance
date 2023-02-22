class Person:
    def __init__(self, name, adress, phone):
        self.name = name
        self.adress = adress
        self.phone = phone

    def get_name(self):
        return self.name
    def get_adress(self):
        return self.adress
    def get_phone_number(self):
        return self.phone
    def print_person(self):
        print(f'Name: {self.name}')
        print(f'Addr: {self.adress}')
        print(f'Phone: {self.phone}')



class Customer(Person):
    def __init__(self,name,adress,phone,cust_num,on_list):
        Person.__init__(self, name,adress,phone)
        self.__cust_num = cust_num
        self.__on_list = on_list

    def print_person(self):
        print(f'Name: {self.name}')
        print(f'Addr: {self.adress}')
        print(f'Phone: {self.phone}')

        print(f'Customer Number{self.cust_num}')
        if self.__on_list:
            print('On Mailing List: Yes')
        else:
            print('On Mailing List: No')
