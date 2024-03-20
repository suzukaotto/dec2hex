import os as os
def dec2hex(dex_num):
    hex_num = hex(dex_num)
    return hex_num
while 1:
    dec_num = input("dec: ")
    try:
        dec_num = int(dec_num)
    except:
        print("only dec input")
        continue
    
    hex_num = dec2hex(dec_num)
    print("0x는 읽지 마세요!!")
    print("10진수: ", dec_num)
    print("16진수: ", hex_num)
    
    print("계속 하시겠습니까? Y=1, N=2\n\n")
    select = input("숫자를 입력하세요. : ")
    if select == "1":
        os.system("cls")
        continue
    elif select == "2":
        print("종료 하였습니다.")
        break
    else : 
        print("잘못된 입력입니다.")