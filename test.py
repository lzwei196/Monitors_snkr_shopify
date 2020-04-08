def checkRestock(dataList, sneakerData):
  try:
        pair = zip(dataList, sneakerData)
  except Exception as e:
      print(pair)
      print(str(e))

dict1 = [
    {"1":{
                'unique_id': '001',
                'key1': 'AAA',
                'key2': 'BBB',
                'key3': 'EEE'
             }},
    {"2":         {
                'unique_id': '002',
                'key1': 'AAA',
                'key2': 'CCC',
                'key3': 'FFF'
             }}
         ]

dict2 = [
    { "1": {
                'unique_id': '001',
                'key1': 'AAA',
                'key2': 'DDD',
                'key3': 'EEE'
             }}
         ]

checkRestock(dict1,dict2)
