items=[]

while True:
    print("\n1.Add item")
    print("2.Remove item")
    print("3.View list")
    print("4.Sort list")
    print("5.Quit")

    choice=input("Enter your choice: ")
    if choice=="1":
        item=input("Enter item to add")
        if item.lower() in [x.lower() for x in items]:
            print("Item is already added")
        else:
            items.append(item)
            print(item,"successfully added")

    elif choice=="2":
        item=input("Enter item to remove")
        for x in items:
            if item.lower()==x.lower():
                items.remove(x)
                print(item,"successfully removed")
                break
            else:
                print("Item not found in list")

    elif choice=="3":
        if len(items)==0:
            print("List is empty")
        else:
            print(items)

    elif choice=="4":
        items.sort(key=str.lower)
        print("Items sorted successfully")

    elif choice=="5":
        print("Thank You")
        break

    else:
        print("Invalid choice")