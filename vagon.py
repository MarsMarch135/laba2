n = int(input( 'введите номер вашего места в плацкартном вагоне :'))
print()
if n > 36:
    print('ваше место - боковое.')
elif n % 2:
    print('ваше место в купе внизу.')
else:
    print('ваше место в купе наверху.')
