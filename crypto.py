def system():
    keys = 'abcdefghijklmnopqrstuvwxyz'
    Value = keys[-1] + keys[0:-1]

    encryptSet = dict(zip(keys, Value))
    decryptSet = dict(zip(Value, keys))

    message = input("Please enter a Password : ")
    mode = input("Please select an encryption mode : Encode(E) OR Decode(D) : ")

    if mode.upper() == 'E':
          Message = ''.join([encryptSet[letter]
                             for letter in message.lower()])

    elif mode.upper() == 'D':
          Message = ''.join([decryptSet[letter]
                             for letter in message.lower()])
    else:
        print('Please enter an Valid choice, Decrypt(D) OR Encrypt(E)')

    return Message


print(system())
