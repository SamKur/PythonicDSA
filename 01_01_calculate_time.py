import time

start = time.time()
for i in range(1,101):
    print(i)
end = time.time()


start_while = time.time()
i=1
while i < 101  :
    print(i)
    i+=1
end_while = time.time()


print( end - start ) #0.05 sec
print( end_while - start_while ) #0.04 sec
