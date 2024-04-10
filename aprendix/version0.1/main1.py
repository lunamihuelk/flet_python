import re

texto = "Este es un enlace https://flet.dev/docs/controls/text/ y hay varios enlaces https://flet.dev/docs/text/ww https://flet.dev/docs/controls/text/1"

lstexto = texto.split(' ')
lsstext = []
listafinal=[]
esword=True
for word in lstexto:
    if 'https:' in word:
        esword=False
        stringUnido=' '.join(lsstext)
        listafinal.append(stringUnido)
        listafinal.append(word)
        lsstext=[]
    else:
        if esword:
            lsstext.append(word)
        else:
            stringUnido=' '.join(lsstext)
            listafinal.append(stringUnido)
            esword=True
            lsstext=[word]
listafinal = list(filter(bool, listafinal))
print('#############')
print(listafinal)