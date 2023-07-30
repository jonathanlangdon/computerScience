# stop a loop when it hits an exception

for num in range(-3, 3):
    try:
        print(5 / num)
    except:
        break
