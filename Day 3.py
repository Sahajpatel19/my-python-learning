def high(name):
    if name=='cap':
        return 'School Captain'
    elif name=='vic':
        return 'Vice Captain'
    elif name=='cul':
        return 'Cultural Captain'
    elif name == 'spo':
        return 'Sports Captain'
    else:
        print("Invalid Choice")
print(high('cap'),'Sahaj')
print(high('vic'),'Kavya')
print(high('cul'),'Zara')
print(high('spo'),'Shikhar')
