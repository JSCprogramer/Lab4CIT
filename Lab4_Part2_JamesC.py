hours = int(input('Enter the number of hours worked:'))
payrate = int(input('Enter te hourly pay rate:'))
grosspay = hours*payrate
normhr=40
otpay= 1.5


if hours > normhr:
    ot=hours-normhr
    ottpay=ot*payrate*otpay
    grossot= normhr*payrate+ottpay
    print(f'Your gorss pay is {grosspay}')
else:
    print(f'Your gorss pay is {grosspay}')
    
