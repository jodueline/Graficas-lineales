
# Edicion de la formula
multiplicador_de_x=3
resta_o_sema_al_multi=-2

print('esta es la formula por defauld')
print(f'Y= {multiplicador_de_x} X {resta_o_sema_al_multi}')
modificacion=input('Quieres modificarla?')
if modificacion=='si':
   while True:
      print('Que quieres modificar')
      print(multiplicador_de_x,'= A')
      print(resta_o_sema_al_multi, '= B')
      optios=input('(1 o 2): ')
      if optios== 'A':
         print('Introduce el nuevo valor: ')
         multiplicador_de_x=int(input(': '))
         print('Quieres cambiar otro valor?: ')
         regresar=input(': ')
         if regresar=='no':
            break
      elif optios== 'B':
         print('Introduce el nuevo valor: ')
         resta_o_sema_al_multi=int(input(': '))
         print('Quieres cambiar otro valor?: ')
         regresar=input(': ')
         if regresar=='no':
            break
# Diferecia entre +2 y -2 porque no puedo hacer una suma sin el pero si una resta 
# Con un numero negativo -2
if resta_o_sema_al_multi>0 and resta_o_sema_al_multi !=0:
   print(f'y= {multiplicador_de_x}X +{resta_o_sema_al_multi}')
else:
   print(f'y= {multiplicador_de_x}X {resta_o_sema_al_multi}')
# Introduccion de cordendas
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

# Resolucion de ecuaciones y inpresion de resultados
for x in Eje_X:
   print('♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠')
   X_y_numero=multiplicador_de_x*x
   Y= X_y_numero + resta_o_sema_al_multi
   print(f'Y = {multiplicador_de_x}({x}) {resta_o_sema_al_multi}')
   print(f'Y = {X_y_numero} {resta_o_sema_al_multi}')
   print(f'Y = {Y}')
#

# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line







