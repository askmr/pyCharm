def getStudent(name, id, dept='CSE'):  # default arg should be at the end only
    print("Name", name)
    print("RollNo:", id)
    print("Department:", dept)


getStudent('Atul', 10)  # gets the default value or arg passed in method
getStudent('Deepak', 2, "IT")  # overrides the default value in arg
getStudent(21, 'EEE',
           'Akanksha')  # when switching arg positions, data entry may be incorrect. To make it in order, give keyword also as below
getStudent(id=21, dept='EEE', name='Akanksha')
