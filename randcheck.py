import time
number = 30834

count = 1
start = time.time()

while (count < number):
    print("Not the number")
    count += 1
end = time.time()
print("Got the number")
time = end - start

print(time)