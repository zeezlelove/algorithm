def prime_number(num):
    if num != 1:
        for i in range(2,num):
            if num % i == 0:
                return False
    else:
        return False

    return True 
if prime_number(int(input())) == True:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")
