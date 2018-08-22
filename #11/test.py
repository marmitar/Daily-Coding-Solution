from query import Query


autocomplete = Query()
autocomplete.insert(["dog", "deer", "deal"])

print(autocomplete['de'])
