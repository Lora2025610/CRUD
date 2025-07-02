def load_authors():
    return [
    {'id':1, 'name': "Ilona", "surname":"balsyte"},# 0
    {'id':2, 'name': "Birute", "surname":"Vaskaite"},# 1
    {'id':3, 'name': "Valdas", "surname":"Adamkus"},# 2
]

def print_authors(authors):
    for i in authors:
        print(f"{i["id"]},{i['name']},{i['surname']}")

def create_author(authors):
    print("sukurti nauja autoriu")

    id = str( int(authors[-1]['id']) + 1) if len(authors) > 0 else 1
    print("Iveskite autoriaus varda")
    name = input()
    print("Iveskite autoriaus pavarde")
    surname = input()
    # reikia padaryti issaugojima
    authors.append({'id': id, 'name': name, 'surname': surname})

def edit_author(authors):
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

def delete_author(authors):
    print('salinti autoriu')
    print("Pasirinkite ID autorius kuri norite redaguoti")
    delete_id = input()
    for author in authors:
        if delete_id == str(author['id']):
            print(f'{author['id']}. Šalinama: Autorius {author['name']} {author['surname']}')
            author_index = authors.index(author)
            del authors[author_index]