my_dict = {
    "Speros": "(555)-555-5555",
    "Michael": "(999)999-9999",
    "Jay": "(777)777-7777"
}

def tuple(dict):
    tuple = ()
    list = []
    for key,data in dict.iteritems():
        tuple = key, data
        list.append(tuple)
    return list

print tuple(my_dict)
