def palindrome():
    for i in range(1000000):
        num = str(i).zfill(6)
        num = str(num)
        if num[2:] == num[5:1:-1]:
            num = int(num)
            num = num + 1
            num = str(num)
            if num[1:] == num[5:0:-1]:
                num = int(num)
                num = num + 1
                num = str(num)
                if num[1:] == num[4:1:-1]:
                    num = int(num)
                    num = num + 1
                    num = str(num)
                    if num[:] == num[5:0:-1]:
                        print(num)
if __name__ == "__main__":
    palindrome()