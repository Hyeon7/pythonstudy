class UppercaseError(Exception):
    pass

def check():
    words = ['apple', 'orange', 'banana', 'WATERMELON']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)
try:
    check()
except UppercaseError as exc:
    print('This is my falut. Go next')