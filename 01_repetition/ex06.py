import json

def show_info(prof: str)-> None:
    with open('data_workers.json', 'r', encoding='utf-8') as my_file:
        data = my_file.read()
        data_dict = json.loads(data)
        count_20_29 = 0
        count_30_39 = 0
        count_40_49 = 0
        count_50_59 = 0
        count_60_69 = 0
        female = 0
        male = 0

        filter_dict = [person for person in data_dict if person['occupation'] == prof]

        for person in filter_dict:
            if person['female']:
                female += 1
            else:
                male += 1
            if person['age'] in range(20, 30):
                count_20_29 += 1
            elif person['age'] in range(30, 40):
                count_30_39 += 1
            elif person['age'] in range(40, 50):
                count_40_49 += 1
            elif person['age'] in range(50, 60):
                count_50_59 += 1
            elif person['age'] in range(60, 70):
                count_60_69 += 1

        print('---------------------')
        print(f'| 20-29  | {count_20_29}')
        print(f'| 30-39  | {count_30_39}')
        print(f'| 40-49  | {count_40_49}')
        print(f'| 50-59  | {count_50_59}')
        print(f'| 60-69  | {count_60_69}')
        print('---------------------')
        print(f'| FEMALE | {female}')
        print(f'| MALE   | {male}')
        print('---------------------')



show_info(input())