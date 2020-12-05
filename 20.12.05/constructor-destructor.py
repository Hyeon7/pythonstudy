class Person(object):
    def __init__(self, name):
        self.name = name
        
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)
        
    def run(self, num):
        print('run' * num)
        
    def __del__(self):
        print('good bye')
        
person = Person('Mike')
person.say_something()

del person

print('#########')