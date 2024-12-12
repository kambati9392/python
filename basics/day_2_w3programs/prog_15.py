#str1=input("enter the passwprd")
def password(str1):
    if len(str1)<6 or len(str1)>16:
      return "invalid"
    has_special=False
    # dct=0
    # lct=0
    # uct=0
    # sct=0
    for char in str1:
          if char.isdigit():
              has_isdigit=True
            #   dct+=1
          if char.islower():
             has_islower=True
            #  lct+=1
          if char.isupper():
              has_isupper=True
            #   uct+=1
          if char in "@#$":
              has_special=True
            #   sct+=1
    if not has_isdigit :
        return "invalid"
    if not has_islower :
        return "invalid"
    if not has_isupper :
        return "invalid"
    if not has_special :
        return "invalid"
    else:
        return "valid"
print(password("12Ram@23"))