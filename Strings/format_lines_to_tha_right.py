def to_celcius(x):
    return (x-32)*5/9
for x in range (1,101,10):
    print("{:>3} F | {:>6.2f}".format(x,to_celcius(x)))