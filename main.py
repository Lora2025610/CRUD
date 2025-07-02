from list_CRUD import *

authors = load_authors()

# print(authors[0])
while True:
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti autoriu sarasa")
    print("2. Įtraukti autoriu i sarasa")
    print("3. koreguoti autorius")
    print("4. šalinti autorius")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    opt = input()
    match opt:
        case '1':
            print_authors(authors)
        case '2':
            create_author(authors)
        case '3':
            edit_author(authors)
        case '4':
            delete_author(authors)
        case '5':
            print("iseiti is programos")
            break

