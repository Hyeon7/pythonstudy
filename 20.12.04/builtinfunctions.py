import builtins

builtins.globals()

ranking = {
    'A' : 100,
    'B' : 85,
    'C' : 95
}

#ranking.get('A')
print(sorted(ranking, key = ranking.get, reverse = True))