gg = input('Enter Hours: ')
tt = input('Enter Rate: ')
yp = float(gg)
zp = float(tt)
# print(yp,zp)
if yp > 40:
    # print('overtime')
    reg = yp * zp
    otp = (yp - 40.0) * (zp * 0.5)
    # print(reg,otp)
    ee = reg + otp
else:
    #print('regular')
    ee = yp * zp
print('Pay:',ee)        
