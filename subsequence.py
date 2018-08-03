def minion_game(string):
    minion_game1(string,0,0)

def minion_game1(string,stuart,kelvin):
    for i in range(len(string)):
        if string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U":
            kelvin = kelvin+len(string[i:])
        else:
            stuart = stuart+len(string[i:])
        print(string)
    result = max(kelvin,stuart)
    if result == kelvin:	
         print("Kelvin "+str(kelvin))
    else:
         print("Stuart "+str(stuart))			
if __name__ == '__main__':
    s = input()
    minion_game(s)

