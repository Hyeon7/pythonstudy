s = """\
AAA
BBB
CCC
DDD
"""
with open('test.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())