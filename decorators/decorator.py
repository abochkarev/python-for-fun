decs = []

def deco(func):
    def inner():
        print ('Calling inner')
    decs.append(inner)
    return inner

@deco
def target():
    print ('Calling target')


target()
print (decs)

