# Información de la práctica
asignatura = "Programación y redes virtualizadas"
mi_nombre = "Angelo Cortés"
nombre_compañero = "Alexander Coito"

# Encabezado
print("=" * 40)
print(f"Asignatura: {asignatura}")
print(f"Estudiante: {mi_nombre}")
print(f"Compañero:  {nombre_compañero}")
print("=" * 40)

# Solicitar datos al usuario
print("\nIngrese los siguientes datos:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
codigo_seccion = input("Código de sección: ")
sede = input("Sede: ")
numero_acl = int(input("Número de ACL: "))

# Clasificar ACL
if 1 <= numero_acl <= 99:
    tipo_acl = "ACL Estándar"
elif 100 <= numero_acl <= 199:
    tipo_acl = "ACL Extendida"
elif 1300 <= numero_acl <= 1399:
    tipo_acl = "ACL Estándar"
elif 2000 <= numero_acl <= 2699:
    tipo_acl = "ACL Extendida"
else:
    tipo_acl = "Número de ACL no válido"

# Mostrar información
print("\n" + "=" * 40)
print("INFORMACIÓN INGRESADA")
print("=" * 40)
print(f"Nombre:            {nombre}")
print(f"Apellido:          {apellido}")
print(f"Código de sección: {codigo_seccion}")
print(f"Sede:              {sede}")
print(f"Número de ACL:     {numero_acl}")
print(f"Tipo de ACL:       {tipo_acl}")
print("=" * 40)
