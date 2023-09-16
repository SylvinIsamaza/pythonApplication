import re

fname = input('Enter the file')


sum = 0
count = 0
try:
    hand = open(fname)
    for line in hand:
        float_line = re.findall('^X-DSPAM-Confidence:.([0-9]\.[0-9])', line)

        if not len(float_line) < 1:
            for num in float_line:
                el=float(num)
                sum=sum+el
            count=count+1

    average = sum / count
    print(average)
    # print(count)






except FileNotFoundError:
    print('Something went wrong while opening the file:', fname)
    exit()
