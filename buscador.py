from rdflib import Graph

print("Iniciando el motor de búsqueda de la biblioteca...")
g = Graph()


archivo_ontologia = r"C:\Users\PC\Desktop\ProyectoBuscador\ontologia.owl"

try:
    g.parse(archivo_ontologia, format="xml")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

while True:
    print("\n" + "="*45)
    print(" 🔍 METABUSCADOR SEMÁNTICO DE LA BIBLIOTECA")
    print("="*45)
    print("1. Buscar usuario (ver qué libro tiene y su tipo)")
    print("2. Buscar libro (ver quién lo tiene y qué tipo de usuario es)")
    print("3. Salir del programa")
    
    opcion = input("\nElige una opción (1/2/3): ")

    #1: BUSQUEDA POR USUARIO
    
    if opcion == "1":
        nombre_buscado = input("Escribe el nombre del usuario (ej. Juan): ")
        
        consulta_usuario = f"""
        PREFIX ont: <http://www.biblioteca.com/ontologia#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        
        SELECT DISTINCT ?tituloLibro ?tipoUsuario
        WHERE {{
            ?usuario ont:nombre ?nombreUsuario .
            FILTER(regex(str(?nombreUsuario), "{nombre_buscado}", "i"))
            
            # 👇 Extraemos el tipo de usuario
            ?usuario rdf:type ?tipoURI .
            BIND(STRAFTER(STR(?tipoURI), "#") AS ?tipoUsuario)
            FILTER(?tipoUsuario IN ("Estudiante", "Investigador", "Profesor", "PublicoGeneral", "Usuario"))
            
            ?usuario ont:realizaPrestamo ?prestamo .
            ?prestamo ont:incluyeRecurso ?libro .
            ?libro ont:tieneTitulo ?tituloLibro .
        }}
        """
        resultados = list(g.query(consulta_usuario))
        
        if resultados:
            print(f"\n✅ Resultados encontrados para el usuario '{nombre_buscado}':")
            for fila in resultados:
                print(f"   -> Tipo de perfil: {fila.tipoUsuario}")
                print(f"   -> Tiene prestado el libro: {fila.tituloLibro}")
        else:
            print(f"\n❌ No se encontraron préstamos activos para '{nombre_buscado}'.")
            
    
    #2: BUSQUEDA POR LIBRO
    
    elif opcion == "2":
        libro_buscado = input("Escribe el título del libro (ej. Quijote): ")
        
        consulta_libro = f"""
        PREFIX ont: <http://www.biblioteca.com/ontologia#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        
        SELECT DISTINCT ?nombreUsuario ?apellidoUsuario ?tipoUsuario
        WHERE {{
            ?prestamo ont:incluyeRecurso ?libro .
            ?libro ont:tieneTitulo ?tituloLibro .
            FILTER(regex(str(?tituloLibro), "{libro_buscado}", "i"))
            
            ?usuario ont:realizaPrestamo ?prestamo .
            ?usuario ont:nombre ?nombreUsuario .
            ?usuario ont:apellido ?apellidoUsuario .
            
            # 👇 Extraemos el tipo de usuario también aquí
            ?usuario rdf:type ?tipoURI .
            BIND(STRAFTER(STR(?tipoURI), "#") AS ?tipoUsuario)
            FILTER(?tipoUsuario IN ("Estudiante", "Investigador", "Profesor", "PublicoGeneral", "Usuario"))
        }}
        """
        resultados = list(g.query(consulta_libro))
        
        if resultados:
            print(f"\n⚠️ El libro '{libro_buscado}' NO está disponible.")
            for fila in resultados:
                print(f"   -> Prestado a: {fila.nombreUsuario} {fila.apellidoUsuario} (Perfil: {fila.tipoUsuario})")
        else:
            print(f"\n✅ El libro '{libro_buscado}' SÍ está disponible (o no existe en el catálogo).")
            
    
    #3: SALIR

    elif opcion == "3":
        print("\n¡Cerrando el buscador!")
        break
        
    else:
        print("\n❌ Opción no válida. Por favor, escribe 1, 2 o 3.")