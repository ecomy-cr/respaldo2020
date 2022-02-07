a = 'Numero: {0} interpolated'.format(1.23)
b = 'Numero: {0} interpolated'.replace('{0}',str(1.23))
c = 'Numero: {0} interpolated'.replace('{0}','1.23')
d = 'Numero:  {0} y {1} interpolated'.format('1.23', 9.9999)
e = 'Numero:  {0} y {1} interpolated'.format('1.23', 9.9999)

retorno_practica = 'Numero: {0:>10} se ha formateado '.format(123)
retorno_practica = 'Numero: {0:<10} se ha formateado '.format(123)
retorno_practica = 'Numero: {0:010} se ha formateado '.format(123)
retorno_practica = 'Numero: {0:+} se ha formateado '.format(123)
retorno_practica = 'Numero: {0:-} se ha formateado '.format(123)
retorno_practica = 'Numero: {0: } se ha formateado '.format(123)

retorno_practica = 'Numero: {0:b} se ha formateado '.format(123)
retorno_practica = 'Numero: {0:c} se ha formateado '.format(123)
retorno_practica = 'Numero: {0:d} se ha formateado '.format(123)
retorno_practica = 'Numero: {0:o} se ha formateado '.format(123)
retorno_practica = 'Numero: {0:x} se ha formateado '.format(123)

retorno_practica = 'Numero: {0:+#016b} se ha formateado '.format(123)

print(a)
print(b)
print(c)
print(d)
print(e)

print(retorno_practica)
