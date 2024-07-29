lista = [ 9, 8 , 7 , 2]
nstring = str(lista)
nstring = nstring.replace(" ", "")
nstring = nstring.replace("[", '"')
nstring = nstring.replace("]", '"')
print(nstring)