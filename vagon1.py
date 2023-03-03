n=int(input('введите номер места в вагоне'))
print()
if n>36 and n%2:
print('боковое место сверху')
elif n>36 and n!=n%2:
print('боковое место сверху')
elif n<36 and n%2:
print('купе сверху')
else:
print('купе сверху')
