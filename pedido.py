from te import Te


sabor = int(input("ingrese el sabor del te:"))
formato=int(input("ingrese el formato :"))


te=Te(sabor, formato)

print(f"el sabor del te es {te.obtener_sabor()}")  #metodo de instancia
print(f"el formato es de {te.formato}   gramos")    
print(f"el precio del te es de :${Te.obtener_precio(formato)} ") #metodo estatico
tiempo, recomendacion= Te.obtener_tiempo_recomendacion(sabor)  #deestructuramos

print(f"el tiempo de maceracion es: {tiempo} minutos")
print(f"Se recomienda:  {recomendacion}")

print(f"tiene una duracion de {Te.duracion} dias")