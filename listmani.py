def list_manipulation(li,command,loc,value=0):
    if command=='remove':
        if loc=='end':
            return li.pop()
        elif loc=='beginning':
            return li.pop(0)
    elif command=='add':
        if loc=='end':
            return li.insert(-1,value)
        elif loc=='beginning':
            return li.insert(0,value)

print(list_manipulation([1,2,3],'add','beginning',20))