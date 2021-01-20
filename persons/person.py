from collections import namedtuple
import os
import importlib

Account = namedtuple('Account', 'username pwd')

class Person():
    #declare here so pycharm and index them
    firstName=None
    lastName=None
    address = None
    postal_code = None
    city = None
    province = None
    phone = None
    email = None
    province_full=None
    card_num=None
    card_month=None
    card_year=None
    LV_accs=None
    LV_acc_offset=0

    def __init__(self, csv, **kwargs):
        self.csv=csv
        self.__dict__.update(kwargs)

    def get_LV_acc(self):
        #todo
        return self.LV_accs[0]

    def load_purchase_history(self):
        file_name = f'purchase_history/{self.__class__.__name__}.py'
        #if file exist already
        if os.path.isfile(file_name):
            module = importlib.import_module(f'persons.purchase_history.{file_name}')




class Sample(Person):

    def __init__(self, csv):
        #define all your data here, then use as sample.email, example shown below
        data ={
            'email': 'example.com',
            'address': 'prince arthur street',
            'postal_code': 'postal_code'
        }
        super(Sample, self).__init__(csv, **data)

if __name__=='__main__':
    s = Sample('csv')
    print(s.email)
    s.load_purchase_history()
