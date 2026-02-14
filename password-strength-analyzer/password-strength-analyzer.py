pw=input("enter a password:\n")
s=0
def length_check(pw):
    s=0
    if len(pw)<8:
        print("\n-increase length of password")
        s=0
    elif 8<=len(pw)<12:
        print("\n-length of password is moderate, can be increased")
        s=1
    else:
        s=2
    return s
def sp_char(pw):
    p=0
    for i in pw:
        if not i.isalnum():
            p=p+1
    if p>0 and p<3:
        s=1
    elif p>=3:
        s=2
    else:
        s=0
        print("\n-add special characters to the password")
    return s
def cases(pw):
    u=0
    l=0
    for i in pw:
        if i.isupper():
            u=u+1
        elif i.islower():
            l=l+1
    if u>0 and l>0:
        s=2
    else:
        s=0
        print("\n-mix uppercase and lowercase chars")
    return s
def al_num_mix(pw):
    d=0
    al=0
    for i in pw:
        if i.isdigit():
            d=d+1
        elif i.isalpha():
            al=al+1
    if al>0 and d>0:
        s=1
    else:
        s=0
        print("\n-mix alphabets and numbers")
    return s
print("\nsuggestions:")
s+=length_check(pw)
s+=sp_char(pw)
s+=cases(pw)
s+=al_num_mix(pw)
if s<3:
    print("\npassword is weak")
elif s<5:
    print("\npassword is moderate")
elif s<7:
    print("\npassword is strong")
else:
    print("\npassword is very strong!")
