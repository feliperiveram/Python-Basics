nombre = [1,2,50,-1,54,20,340,234,23,21,23]
nombre.remove(23)
print(f"REMOVE = nombre.remove(23) = {nombre}")
nombre.pop(0)
print(f"POP = nombre.pop(0) = {nombre}")
nombre.reverse()
print(f"REVERSE = nombre.reverse() = {nombre}")
nombre.sort()
print(f"SORT = nombre.sort() = {nombre}")
nombre.sort(reverse=True)
print(f"SORT INVERTIDO = nombre.sort(reverse=True) = {nombre}")
