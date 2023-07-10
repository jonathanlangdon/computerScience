# Making Breakfast

egg = False
milk = True
butter = False
flour = True

if egg and milk and butter and flour:
    print("pancakes")
elif egg and milk and butter:
    print("omelette")
elif egg and milk:
    print("custard")
elif egg:
    print("poached eggs")
else:
    print("Go to the store!")
