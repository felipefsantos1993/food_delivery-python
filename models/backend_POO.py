
class restaurants:
    Name = ''
    Category = ''
    Status = False

rodizio = restaurants()
rodizio.Name = 'Didio'
rodizio.Category = 'Gourmet'

print(dir(rodizio))
print(vars(rodizio))
print(rodizio.Status)