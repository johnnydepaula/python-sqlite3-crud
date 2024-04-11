import crud
from phone import Phone


def display_options():
    loop = True

    while loop:
        rows = []
        print("---------------------------------------------")
        print("Select operation to perform: ")

        print("1. Display Agenda")
        print("2. Insert Into Agenda")
        print("3. Update Agenda")
        print("4. Delete From Agenda")

        print("5. Display Email")
        print("6. Insert Into Email")
        print("7. Update Email")
        print("8. Delete From Email")

        print("9. Display Phone")
        print("10. Insert Into Phone")
        print("11. Update Phone")
        print("12. Delete From Phone")

        print("0. Exit")

        print("---------------------------------------------")
        opt = input("Number : ")
        print("---------------------------------------------")

        ## Manipulating Agenda Table ##
        # 1 = display all data from Agenda in Table Format
        if opt == "1":
            crud.display_table_agenda()

        # 2 = insert data into database.agenda table
        elif opt == "2":
            first_name = input("First Name : ")
            last_name = input("Last Name : ")
            # email = input("Email : ")
            # phone = input("Phone Number : ")
            crud.insert_data_agenda(first_name, last_name)
            crud.display_table_agenda()

        elif opt == "3":
            crud.display_table_agenda()
            id = int(input("Register ID : "))
            data_list = crud.data_list_agenda()

            if id in data_list:
                first_name = input("First Name : ")
                last_name = input("Last Name : ")
                # email = input("Email : ")
                # phone = input("Phone Number : ")
                crud.update_data_agenda(id, first_name, last_name)
                crud.display_table_agenda()
            else:
                print("Invalid or Non-existent ID")

        elif opt == "4":
            crud.display_table_agenda()
            id = int(input("Register ID : "))
            data_list = crud.data_list_agenda()

            if id in data_list:
                crud.delete_data_agenda(id)
                crud.display_table_agenda()
            else:
                print("Invalid or Non-existent ID")

        ## Manipulating Email Table ##
        elif opt == "5":
            crud.display_table_email()

        elif opt == "6":
            email_adress = input("Email adress: ")
            id = input("Register (Person) ID : ")
            # email = input("Email : ")
            # phone = input("Phone Number : ")
            crud.insert_data_email(email_adress, id)
            crud.display_table_email()

        elif opt == "7":
            crud.display_table_email()
            id_email = int(input("Register (Email) ID : "))
            data_list = crud.data_list_email()

            if id_email in data_list:
                email_adress = input("New Email : ")
                # last_name = input("Last Name : ")
                # email = input("Email : ")
                # phone = input("Phone Number : ")
                crud.update_data_email(id_email, email_adress)
                crud.display_table_email()
            else:
                print("Invalid or Non-existent Email ID")

        elif opt == "8":
            crud.display_table_email()
            id_email = int(input("Register (Email) ID : "))
            data_list = crud.data_list_email()

            if id_email in data_list:
                crud.delete_data_email(id_email)
                crud.display_table_email()
            else:
                print("Invalid or Non-existent Email ID")

        ## Manipulating Phone Table ##
        elif opt == "9":
            Phone().display_table_phone()

        elif opt == '10':
            phone_number = input("Phone number : ")
            id = input("Register (Person) ID : ")
            Phone().insert_data_phone(phone_number, id)
            Phone().display_table_phone()

        elif opt == '11':
            Phone().display_table_phone()
            id_phone = int(input("Register (Phone) ID : "))
            data_list = Phone().data_list_phone()
            if id_phone in data_list:
                phone_number = input("New Phone number : ")
                Phone().update_data_phone(id_phone, phone_number)
                Phone().display_table_phone()
            else:
                print("Invalid or Non-existent Phone ID")

        elif opt == '12':
            Phone().display_table_phone()
            id_phone = int(input("Register (Phone) ID : "))
            data_list = Phone().data_list_phone()
            if id_phone in data_list:
                Phone().delete_data_phone(id_phone)
                Phone().display_table_phone()
            else:
                print("Invalid or Non-existent Phone ID")



        elif opt == "0":
            print("See ya!!")
            return False

        else:
            print("Invalid option")

