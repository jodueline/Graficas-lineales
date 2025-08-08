

# Eraboracion de grafica linear representado por la formula f(x)= D(X)+c
# El valor de D es definida por el usuario 



def Estructura(mas,X,mul_X,mas_o_menos_xd,deXanumero,Y):
   if mas==True:
         print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠')
         print(f'Y = {mul_X}({X}) + {mas_o_menos_xd}')
         print(f'Y = {deXanumero} + {mas_o_menos_xd}')
         print(f'Y = {Y}')
   if mas==False:
         print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠')
         print(f'Y = {mul_X}({X}) {mas_o_menos_xd}')
         print(f'Y = {X_y_numero} {mas_o_menos_xd}')
         print(f'Y = {Y}')
multiplicador_de_x=0       
resta_o_sema_al_multi=0
multiplicador_de_x=int(input('Introduce el numero por que se multiplicara la incongnita: '))
resta_o_sema_al_multi=int(input('Introduce el numero que se va a sumar o a restar a la incongita: '))
Eje_X=[]
while True:
   try:
      Cordenda_X=int(input('introduce la cordenada X: '))
   except ValueError:
      Eje_X.append(Cordenda_X)
      print('TERMINO LA INTRODUCCION DE CORDENADAS')
      break
   Eje_X.append(Cordenda_X)
Eje_X.pop(-1)
print(Eje_X)
if resta_o_sema_al_multi>0 and resta_o_sema_al_multi!=0:
   simbolo_positivo=True
else:
   simbolo_positivo=False
for x in Eje_X:
   X_y_numero=multiplicador_de_x*x
   YY= X_y_numero + resta_o_sema_al_multi
   Estructura(simbolo_positivo,x,multiplicador_de_x,resta_o_sema_al_multi,X_y_numero,YY)
print('Creador del codigo: ingeniero Erick "Jodue" Perez')

# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line
