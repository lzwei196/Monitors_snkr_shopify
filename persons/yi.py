from persons.person import Person, Account

class Yi(Person):

    def __init__(self, csv):
        #define all your data here, then use as sample.email, example shown below
        data ={
            'email': 'yaqixyz@gmail.com',
            'address': '3306-4688 Kingsway',
            'postal_code': 'V5H 0E9',
            'city': 'Burnaby',
            'province': 'BC',
            'phone': '7789260206',
            'firstName': 'Yi',
            'lastName': 'Yang',
            'province_full': 'British Columbia',
            'card_num': '4505530131063651', #todo
            'card_month': '02',
            'card_year': '2024',
            'LV_accs' : [ Account(username='yaqixyz@gmail.com', pwd='Canada2911.')
                         ]

        }
        super(Yi, self).__init__(csv, **data)


