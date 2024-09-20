#4

from  te import Te

te1 =Te(1,300)  #instanciando la clase de te con datos
te2 = Te(2,500)

type_te1=type(te1)

type_te2=type(te2)


print(type_te1)
print(type_te2)

if type_te1==type_te2:
    print("ambos objetos son del mismp tipo")
else:
    print("los objetos no son del mismo tipo")