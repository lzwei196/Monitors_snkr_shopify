
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
    def __init__(self, csv, **kwargs):
        self.csv=csv
        self.__dict__.update(kwargs)
        print(type(kwargs))


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
