cook_book = {}

recept=[]

pod_recept = []

#передача разбитой строки с | по ключам
def prisv(list):
    new_dict = {}
    new_dict['ingredient_name'] = list[0]
    new_dict['quantity'] = list[1]
    new_dict['measure'] = list[2]
    return new_dict

# нахождение строки с |
def perebor(massiv):

    new_massive = []
    for nstring in massiv:

        if '|' in nstring:

            new_massive.append(prisv(nstring.split('|')))

    return new_massive
#обрабатывает переданный массив
def nazv(recept):

    for massive in recept:

        cook_book[massive[0]]=perebor(massive)



def ingredients(val, num, k=0):
    prom_spisok = {}
    prom_spisok['measure']=val['measure']
    prom_spisok['quntity'] = int(val['quantity']) * num + k

    return prom_spisok




def vern_znach(ob):
    return int(ob['quntity'])

def get_shop_list_by_dishes(massive,number):



    new_massive = set(massive)
    konechniy_spisok = {}
    for string in new_massive:
        for keys,values in cook_book.items():
            if string in keys:
                for val in values:
                    k = 0
                    if val['ingredient_name'] in konechniy_spisok.keys():
                        k = vern_znach(konechniy_spisok[val['ingredient_name']])

                    konechniy_spisok[val['ingredient_name']] = ingredients(val, num, k)



    print(konechniy_spisok)













with open('Рецепт.txt','r',encoding='utf8') as file :

        for string in file:

            if  string == '\n':
                recept.append(pod_recept)
                pod_recept = []

            else:

                pod_recept.append(string.replace('\n',''))


print('решение первой задачи:\n')
nazv(recept)

print(cook_book)

print('решение второй задачи:\n')

dishes = input('Вводите назваия блюд через запятые:').split(',')

num = int(input('ввдите колтчество персон:'))

dishes_massive = list(dishes)

print(dishes_massive)


get_shop_list_by_dishes(dishes_massive,num)






