import crud
import display
from phone import Phone

if __name__ == '__main__':
    crud.create_table_agenda()
    crud.create_table_email()
    Phone().create_table_phone()
    display.display_options()
