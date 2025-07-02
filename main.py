authors = [
    {'id':1, 'name': "Ilona", "surname":"balsyte"},# 0
    {'id':2, 'name': "Birute", "surname":"Vaskaite"},# 1
    {'id':3, 'name': "Valdas", "surname":"Adamkus"},# 2
]

# print(authors[0])
id_counter = 3
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
            for i in authors:
                print(f"{i["id"]},{i['name']},{i['surname']}")

        case '2':
            print("sukurti nauja autoriu")
            id_counter+=1
            id=id_counter
            print("Iveskite autoriaus varda")
            name= input()
            print("Iveskite autoriaus pavarde")
            surname= input()
            #reikia padaryti issaugojima
            authors.append({'id':id, 'name':name, 'surname':surname})
        case '3':
            print('redaguoti autorius')
            print("Pasirinkite ID autoriaus kurias norite redaguoti")
            edit_id = input()
            for author in authors:
                if str(author['id']) == edit_id:
                    print(f"{author['id']},{author['name']},{author['surname']}")
                    print('íveskite varda')
                    author['name'] = input()
                    print('íveskite pavarde')
                    author['surname'] = input()

            # edit_author(authors)
            #pirma reikia sukurti saugojimo funkcionaluma
        case '4':
            print('salinti autoriu')
            print("Pasirinkite ID autorius kuri norite redaguoti")
            delete_id = input()
            for author in authors:
                if delete_id == str(author['id']):
                    print(f'{author['id']}. Šalinama: Autorius {author['name']} {author['surname']}')
                    author_index = authors.index(author)
                    del authors[author_index]
        case '5':
            print("iseiti is programos")
            break

