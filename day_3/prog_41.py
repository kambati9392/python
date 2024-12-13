yy=int(input("Enter the year"))
mm=int(input("Enter the month"))
dd=int(input("Enter the day"))

if mm==1 and dd==31 or mm==2 and dd==28 or 29 and mm==3 and dd==31 or mm==4 and dd==30 or mm==5 and dd==31 or mm==6 and dd==30 or mm==7 and dd==31 or mm==8 and dd==31 or mm==9 and dd==30 or mm==10 and dd==31 or mm==11 and dd==30 or mm==12 and dd==31:
    dd=1
    mm=1
    yy+=1
else:
    dd+=1
    mm=mm+1


print( yy,"-",mm,"-",dd)
