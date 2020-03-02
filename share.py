#以后再加中文版

categories = ['YOLO', 'Fruits_burst', 'Flavoured_tea', 'Cheezy', 'Diet_tea']

YOLO = ['YOLO Strawberry','YOLO Mango','YOLO Advocado', 'YOLO Dragon Fruit']
Fruits_burst = ['Cheezy Rambutan', 'Fruits BOOM', 'Cheezy Pineapple',
                'Cheezy Watermelon', 'Passion Lemon Tea', 'Coconut Mango']
Flavoured_tea = ['Ice Cream Taro Latte', 'Cheezy Roasted Latte', 'Femi\'s Special Latte',
                 'Purple Taro Latte', 'Black Sugar Fresh Milk', 'Yakult Passion Fruit',
                 'Yakult Lemon Lime', 'Fujiyama Latte', 'Fresh Milk Tea']
Cheezy = ['Cheezy Peach Oolong', 'Cheezy Matcha', 'Cheezy Osmanthus Oolong',
          'Cheezy Jinfeng Oolong', 'Cheezy Jasmine']
Diet_tea = ['Peach Oolong', 'Osmanthus Oolong', 'Jinfeng Oolong', 'Jasmine']

product_dict = {'Cheezy': ['Cheezy Peach Oolong',
            'Cheezy Matcha',
            'Cheezy Osmanthus Oolong',
            'Cheezy Jinfeng Oolong',
            'Cheezy Jasmine'],
 'Diet_tea': ['Peach Oolong', 'Osmanthus Oolong', 'Jinfeng Oolong', 'Jasmine'],
 'Flavoured_tea': ['Ice Cream Taro Latte',
                   'Cheezy Roasted Latte',
                   "Femi's Special Latte",
                   'Purple Taro Latte',
                   'Black Sugar Fresh Milk',
                   'Yakult Passion Fruit',
                   'Yakult Lemon Lime',
                   'Fujiyama Latte',
                   'Fresh Milk Tea'],
 'Fruits_burst': ['Cheezy Rambutan',
                  'Fruits BOOM',
                  'Cheezy Pineapple',
                  'Cheezy Watermelon',
                  'Passion Lemon Tea',
                  'Coconut Mango'],
 'YOLO': ['YOLO Strawberry',
          'YOLO Mango',
          'YOLO Advocado',
          'YOLO Dragon Fruit']}


def menu_construct(categories):

    for subcategory in categories:
        product_dict[subcategory] = eval(subcategory)