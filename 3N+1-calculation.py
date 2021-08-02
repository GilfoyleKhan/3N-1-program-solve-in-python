numc=int(input("insert number :"))
def threen(numc):
    if numc ==1:
        return 1
    elif numc%2 == 0:#even
        numc = numc/2
        print(numc)
    else:#odd
        numc = 3*numc+1
        print(numc)
    return threen(numc)+1
threen(numc)+1
print("Your number that you just insert is >>",numc,"<<")
