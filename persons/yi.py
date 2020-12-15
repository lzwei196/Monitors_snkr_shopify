from persons.person import Person

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

        }
        super(Yi, self).__init__(csv, **data)