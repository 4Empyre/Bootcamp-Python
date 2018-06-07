def compare(list_one, list_two):
    if list_one == list_two:
        print("The lists are the same.")
    else:
        print("The lists are not the same.")



compare([1,2,5,6,2], [1,2,5,6,2])
compare([1,2,5,6,5],[1,2,5,6,5,3])
compare([1,2,5,6,5,16],[1,2,5,6,5])
compare(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])
