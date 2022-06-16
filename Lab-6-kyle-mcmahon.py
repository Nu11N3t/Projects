SIZE = 12
def main():
    AccUsr = ['John walters',
          'Claire Steins',
          'Steven Hall',
          'Justine Lorne',
          'Katie Happ',
          'Joe Campbell',
          'Carl Abbott',
          'Fred Malone',
          'Chris Simpson',
          'Jill Freeburg',
          'Patty Caine',
          'Tom Sadler']
    AccNum = ['5658845',
          '4520125',
          '7895122',
          '8777541',
          '8451277',
          '1302850',
          '8080152',
          '4562555',
          '5552012',
          '5050552',
          '7825877',
          '1250255']
    found = False
    index = 0
    UsrNum = input('Please input your Account Number\n')
    while found == False and index <= SIZE - 1:
        if AccNum[index] == UsrNum:
            found = True
        else:
            index = index + 1
    if found:
        print("The account for", AccNum[index], "under the name", AccUsr[index], "while be charged accordingly")
    else:
        print("We're sorry that account number is invalid")
main()
