i = 1

# while(i<10):
#     print('em loop')
loop = True
while (loop):
    print(i)
    i+=1
    
    if i>10:
        loop = False
        
tecla = ' '
while (tecla!='q'):
   tecla = input('aperte uma tecla')
   
#o Break pula direto pro final do while e encerra o loop
#o continue volta pro começo do while a partir de onde ele está