small_alpha=[chr(x) for x in range(97,123)]
big_alpha=[chr(x) for x in range(65,91)]
print(r'''
  ______                                                            ______   __            __                                 
 /      \                                                          /      \ |  \          |  \                                
|  $$$$$$\  ______    ______    _______   ______    ______        |  $$$$$$\ \$$  ______  | $$____    ______    ______        
| $$   \$$ |      \  /      \  /       \ |      \  /      \       | $$   \$$|  \ /      \ | $$    \  /      \  /      \       
| $$        \$$$$$$\|  $$$$$$\|  $$$$$$$  \$$$$$$\|  $$$$$$\      | $$      | $$|  $$$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\      
| $$   __  /      $$| $$    $$ \$$    \  /      $$| $$   \$$      | $$   __ | $$| $$  | $$| $$  | $$| $$    $$| $$   \$$      
| $$__/  \|  $$$$$$$| $$$$$$$$ _\$$$$$$\|  $$$$$$$| $$            | $$__/  \| $$| $$__/ $$| $$  | $$| $$$$$$$$| $$            
 \$$    $$ \$$    $$ \$$     \|       $$ \$$    $$| $$             \$$    $$| $$| $$    $$| $$  | $$ \$$     \| $$            
  \$$$$$$   \$$$$$$$  \$$$$$$$ \$$$$$$$   \$$$$$$$ \$$              \$$$$$$  \$$| $$$$$$$  \$$   \$$  \$$$$$$$ \$$            
                                                                                | $$                                          
                                                                                | $$                                          
                                                                                 \$$      

''',end="\n\n")


def caesar_cipher():
    while True:
        choice = input("You want to decode or encode? : ")
        msg = input("type the message : ")
        shift = int(input("Enter the shift value :"))
        shift_text = ""
        if choice == "encode":

            for letter in msg:
                if letter in small_alpha:
                    shift_text += chr((ord(letter) - 97 + shift) % 26 + 97)
                elif letter in big_alpha:
                    shift_text += chr((ord(letter) - 65 + shift) % 26 + 65)
                else:
                    shift_text += letter
            print("Your encoded message is : ", shift_text)
        elif choice == "decode":
            shift_text = ""
            for letter in msg:
                if letter in small_alpha:
                    shift_text += chr((ord(letter) - 97 - shift) % 26 + 97)
                elif letter in big_alpha:
                    shift_text += chr((ord(letter) - 65 - shift) % 26 + 65)
                else:
                    shift_text += letter
            print("Your decoded message is :", shift_text)
        else:
            print("select valid option!")
        again = input("want to continue 'y' or 'n' : ").lower()
        if again == 'y':
            continue
        elif again == 'n':
            print("Thanks for using!")
            break
        else:
            print("choose valid option!")
            break
caesar_cipher()
