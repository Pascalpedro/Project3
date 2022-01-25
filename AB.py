
def students_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# students_info('Math', 'Art', name='John', age=22)
students_info(*courses, **info)