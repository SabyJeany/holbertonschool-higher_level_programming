#!/usr/bin/python3
'''Module student'''


class Student:
    '''
    class Student defined by:
        first_name
        last_name
        age
    '''
    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        Public method that retrieves
        a dictionnary representation of Student instance
        '''
        return self.__dict__
