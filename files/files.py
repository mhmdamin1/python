print("hello mhmd amiin")
pairtesFile = open("pairets","w")
list_of_pairets = ["\nluffy", "\nzoro", "\nnami", "\nsabo"]
pairtesFile.writelines(list_of_pairets)
pairtesFile.close()