import personclass as p

name = 'John'
adress = '1234 Main ST.'
phone_number = '123-456-789'
cust_number = 1234
on_list_flag = True


#create an instance of person class
person1 = p.Person(name, adress, phone_number)

#create an instance of customer class
customer1 = p.Customer(name,adress, phone_number, cust_number, on_list_flag)

person1.print_person()

