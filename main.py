def enigma():
    keys = "abcdefghijklmnopqrstuvwxyz !"
    values = keys[-1] + keys[0:-1]
    
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
    msg =input("Enter your secret mesaage: ").lower()
    mode = input("You want to encrypt(e) or decrypt(d)").lower()
    if mode == "e":
        new_msg = ''.join([dict_e[letter] for letter in msg])
    elif mode == "d":
         new_msg = ''.join([dict_d[letter] for letter in msg])
    else:
        return "Are you sure you know what you're doing?"
    return new_msg.capitalize()    

print(enigma())