# Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно
# и не стоит спать более B часов. Сейчас Аня спит H часов в сутки. Если режим сна Ани
# удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
# Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
#
A = int(input())
B = int(input())
H = int(input())
if ((H >= A) and (H <= B)):
  print('Это нормально')
if H < A:
  print('Недосып')
if H > B:
  print('Пересып')