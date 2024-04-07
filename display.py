import crud
def display_options():
    loop = True

    while loop:
        rows = []
        print("---------------------------------------------")
        print("Select operation to perform: ")
        print("1. Display All Data")
        print("2. Insert Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        print("---------------------------------------------")
        opt = input("Number : ")
        print("---------------------------------------------")

        # 1 = display all data in Table Format
        if opt == "1":
            crud.display_table()

        # 2 = insert data into database.agenda table
        elif opt == "2":
            first_name = input("First Name : ")
            last_name = input("Last Name : ")
            email = input("Email : ")
            phone = input("Phone Number : ")
            crud.insert_data(first_name, last_name, email, phone)
            crud.display_table()

        elif opt == "3":
            crud.display_table()
            id = int(input("Register ID : "))
            data_list = crud.data_list()

            if id in data_list:
                first_name = input("First Name : ")
                last_name = input("Last Name : ")
                email = input("Email : ")
                phone = input("Phone Number : ")
                crud.update_data(id, first_name, last_name, email, phone)
                crud.display_table()
            else:
                print("Invalid or Non-existent ID")

        elif opt == "4":
            crud.display_table()
            id = int(input("Register ID : "))
            data_list = crud.data_list()

            if id in data_list:
                crud.delete_data(id)
                crud.display_table()
            else:
                print("Invalid or Non-existent ID")

        elif opt == "5":
            print("See ya!!")
            return False

        else:
            print("Invalid option")

# print(type(display_options()))
