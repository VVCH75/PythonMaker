my_dict={'Яблоко':'Apple','Персик':'Peach','Арбуз':'Watermelon','Дыня':'Melon','Груша':'Pear'}
print(my_dict)
print(my_dict['Арбуз'])
print(my_dict.get('Киви'))
print(my_dict.pop("Арбуз"))
my_dict["Яблоко"]="Тыблако"
print(my_dict)

my_dict.update({'Клубника':'Strawberry',
                'Смородина':'Сurrant'})
print(my_dict)

my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко'}
print(my_set)
my_set.add("Груша")
my_set.remove(42.314)
print(my_set)