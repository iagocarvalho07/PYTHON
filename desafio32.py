ANO =  int(input('que ano quer analizar'))
if ANO % 4 == 0 and ANO % 100 != 0:
    print("o ano {} é bissexto".format(ANO))
else:
    print('o ano não é bissexto')
