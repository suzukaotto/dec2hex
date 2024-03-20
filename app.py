def dec2hex(dex_num):
    hex_num = hex(dex_num)
    return hex_num

while 1:
    try:
        dec_num = input("dec: ")
        dec_num = int(dec_num)
    except KeyboardInterrupt:
        print("\nprogram exited.")
        exit(0)
    except:
        print("only dec input")
        continue
    
    hex_num = dec2hex(dec_num)
    print("10진수: ", dec_num)
    print("16진수: ", hex_num)
