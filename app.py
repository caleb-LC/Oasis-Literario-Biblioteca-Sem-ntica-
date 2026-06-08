import os
from flask import Flask, render_template, request
from SPARQLWrapper import SPARQLWrapper, XML
from database import consultar_base_datos, obtener_todos_los_libros, inicializar_base_de_datos
 
app = Flask(__name__)
 
# Inicializar siempre al arrancar (funciona con gunicorn y con python directo)
inicializar_base_de_datos()
 
def buscar_en_biblioteca(termino, idioma, tipo_busqueda):
    sparql = SPARQLWrapper(f"http://{idioma}.dbpedia.org/sparql")
    recurso = termino.strip().replace(" ", "_")
    
    if tipo_busqueda == "obras":
        consulta = f"""
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT DISTINCT ?obraNombre
        WHERE {{
            ?obra dbo:author <http://{idioma}.dbpedia.org/resource/{recurso}> .
            ?obra rdfs:label ?obraNombre .
        }} LIMIT 15
        """
        sparql.setQuery(consulta)
        sparql.setReturnFormat(XML)
        
        try:
            resultados_dom = sparql.query().convert()
            resultados_xml = resultados_dom.getElementsByTagName("result")
            
            obras = []
            for resultado in resultados_xml:
                bindings = resultado.getElementsByTagName("binding")
                for binding in bindings:
                    if binding.getAttribute("name") == "obraNombre":
                        literales = binding.getElementsByTagName("literal")
                        if literales:
                            nombre = "".join(nodo.nodeValue for nodo in literales[0].childNodes if nodo.nodeValue)
                            if nombre not in obras:
                                obras.append(nombre)
            
            if obras:
                return {"exito": True, "tipo": "lista", "titulo": f"Obras de {termino}", "datos": obras}
            else:
                return {"exito": False, "mensaje": f"No se encontraron obras registradas para el autor '{termino}' en este idioma."}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error de conexión: {e}"}
 
    else:
        consulta = f"""
        PREFIX dbo: <http://dbpedia.org/ontology/>
        SELECT ?descripcion
        WHERE {{
            <http://{idioma}.dbpedia.org/resource/{recurso}> dbo:abstract ?descripcion .
        }}
        """
        sparql.setQuery(consulta)
        sparql.setReturnFormat(XML)
        
        try:
            resultados_dom = sparql.query().convert()
            resultados_xml = resultados_dom.getElementsByTagName("result")
            
            if resultados_xml:
                primer_resultado = resultados_xml[0]
                nodo_literal = primer_resultado.getElementsByTagName("literal")[0]
                descripcion = "".join(nodo.nodeValue for nodo in nodo_literal.childNodes if nodo.nodeValue)
                return {"exito": True, "tipo": "texto", "titulo": f"Información sobre: {termino}", "datos": descripcion}
            else:
                return {"exito": False, "mensaje": f"No se encontró información sobre '{termino}'. Revisa la ortografía y las mayúsculas."}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error de conexión: {e}"}
 
@app.route('/')
def index():
    libros = obtener_todos_los_libros()
    return render_template('index.html',
                           libros_catalogo=libros,
                           total_libros=len(libros))
 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
