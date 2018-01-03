#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score > 100 or self.score < 0:
            raise ValueError('ssssss')
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'
