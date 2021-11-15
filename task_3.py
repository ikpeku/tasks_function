'''A funtion to accept a list argument of only integers and return even numbers only'''
num_list = []
even_list = []
def even_number(num_list):
    while True:
        try:
            num = int(input('input desirable number: '))
        except ValueError:
            print('input is not a number.')
        else:
            if len(num_list) == 5:
                break
            else:
                if num not in num_list:
                    num_list.append(num)
                    for n in num_list:
                        if n %2 == 0:
                            even_list.append(n)
                        
                else:
                    print('number already in list')
    return even_list
even_number(num_list)
print(f'your desirable numbers are: {num_list}')
print(f'even numbers from desirable numbers: {set(even_list)}')

