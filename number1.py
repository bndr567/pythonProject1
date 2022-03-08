numbers = [1111111111,2222222222,3333333333,4444444444,5555555555,6666666666,7777777777]
names = ['Amal','Mohammed','Khadijah','Abdullah','Rawan' ,'Faisal' , 'Layla']
login = input()





def numbers():
    names = []
    numbers = input('Enter number >/')# asking use

    if numbers.isdigit() == False:
            print('This is invalid number ')
    elif numbers == int('1111111111'):
            print('Amal')
    elif numbers =='2222222222':
            print('Mohammed')
    elif numbers == '3333333333':
        print('Khadijah')
    elif numbers == '4444444444':
            print('Abdullah')
    elif numbers == '5555555555':
        print('Rawan')
    elif numbers == '6666666666':
        print('Faisal')
    elif numbers =='7777777777':
        print('luyla')
    else:
        print('Sorry, the number is not found ')


def names():
    names = input('Enter your name >')
    if names == 'Amal':
        print(1111111111)
    elif names == 'Mohammed':
        print(22222222222)
    elif names == 'Khadijah':
        print(3333333333)
    elif names == 'Abdullah':
        print(4444444444)
    elif names == 'Rawan':
        print(5555555555)
    elif names == 'Faisal':
        print(6666666666)
    elif names == 'Layla':
        print(7777777777)

