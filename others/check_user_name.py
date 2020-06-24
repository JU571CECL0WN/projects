def method_01(user_name, users):
    name_parts = user_name.split('_')
    while True:
        name = '_'.join(name_parts)
        if name in users:
            return True
        name_parts.pop()
        if not name_parts:
            return False
        
        
def method_02(user_name, users):
    name_parts = user_name.split('_')
    for i in range(len(name_parts), 0, -1):
        if '_'.join(name_parts[0:i]) in users:
            return True
    return False



users  = ['afganistan', 'barcelona', 'escandinavia', 'castilla_la_mancha']
user_name = input('>>>')
print(method_02(user_name, users))