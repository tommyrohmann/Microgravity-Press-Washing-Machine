import time
display = ['|','/','—','\\']
i=0
while True:
    i+=1
    if i >= len(display):
        i = 0
    print(display[i],display[i-1],display[i-2],display[i-3],display[i-4],display[i-1],display[i-2],display[i-3],display[i-4])
    time.sleep(.1)