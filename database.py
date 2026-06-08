import sqlite3
import os

DB_NAME = "biblioteca.db"

def obtener_conexion():
    """Establece una conexión segura con la base de datos SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permite acceder a las columnas por su nombre
    return conn

def inicializar_base_de_datos():
    """Crea la estructura de la base de datos e inyecta los 200 libros iniciales."""
    
    if os.path.exists(DB_NAME):
        return

    conn = obtener_conexion()
    cursor = conn.cursor()

    # 1. CREACIÓN DE LA TABLA 
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            autor TEXT NOT NULL,
            titulo TEXT NOT NULL,
            sinopsis TEXT NOT NULL,
            genero TEXT NOT NULL,
            estado TEXT NOT NULL,
            idioma TEXT NOT NULL
        )
    """)

    # 2. LISTA DE LOS 200 LIBROS 
    libros_iniciales = [
        # === LITERATURA ===
        ("Gabriel García Márquez", "Cien años de soledad", "La historia de la familia Buendía a lo largo de siete generaciones en el mítico pueblo de Macondo.", "Literatura", "DISPONIBLE", "es"),
        ("Miguel de Cervantes", "Don Quijote de la Mancha", "Un hidalgo manchego pierde la cordura por leer novelas de caballerías y se transforma en caballero andante.", "Literatura", "PRESTADO", "es"),
        ("J.R.R. Tolkien", "El Señor de los Anillos", "La épica travesía de Frodo Bolsón para destruir el Anillo Único en los fuegos del Monte del Destino.", "Literatura", "DISPONIBLE", "es"),
        ("George Orwell", "1984", "Una perturbadora novela distópica sobre el Gran Hermano y el control absoluto de una sociedad vigilada.", "Literatura", "RESERVADO", "es"),
        ("Jorge Luis Borges", "El Aleph", "Una célebre colección de cuentos que explora laberintos, infinitos y las paradojas del universo.", "Literatura", "DISPONIBLE", "es"),
        ("Oscar Wilde", "El Retrato de Dorian Gray", "Un joven obsesionado con la juventud eterna vende su alma para que su retrato envejezca por él.", "Literatura", "DISPONIBLE", "es"),
        ("Fiódor Dostoyevski", "Crimen y Castigo", "El dilema moral y psicológico de Raskólnikov tras cometer un asesinato justificado por su intelecto.", "Literatura", "DISPONIBLE", "es"),
        ("Antoine de Saint-Exupéry", "El Principito", "Un piloto varado en el desierto conoce a un pequeño príncipe que le enseña el valor de lo invisible.", "Literatura", "DISPONIBLE", "es"),
        ("Julio Cortázar", "Rayuela", "Una contranovela que ofrece múltiples secuencias de lectura y rompe los moldes de la narrativa lineal.", "Literatura", "PRESTADO", "es"),
        ("Franz Kafka", "La Metamorfosis", "Gregorio Samsa amanece una mañana convertido en un monstruoso insecto, alterando su vida familiar.", "Literatura", "DISPONIBLE", "es"),
        ("Jane Austen", "Orgullo y Prejuicio", "La relación entre Elizabeth Bennet y el aristócrata Fitzwilliam Darcy en la Inglaterra rural.", "Literatura", "DISPONIBLE", "es"),
        ("Mary Shelley", "Frankenstein", "Un científico desafía las leyes de la naturaleza dando vida a una criatura creada con partes humanas.", "Literatura", "PRESTADO", "es"),
        ("Ernest Hemingway", "El viejo y el mar", "La dura lucha de un viejo pescador cubano contra un enorme pez espada en alta mar.", "Literatura", "DISPONIBLE", "es"),
        ("Herman Melville", "Moby Dick", "La obsesiva persecución del capitán Ahab contra la gran ballena blanca que le arrancó la pierna.", "Literatura", "RESERVADO", "es"),
        ("Dante Alighieri", "La Divina Comedia", "Un viaje alegórico por el Infierno, el Purgatorio y el Paraíso guiado por el poeta Virgilio.", "Literatura", "DISPONIBLE", "es"),
        ("Homero", "La Odisea", "El peligroso viaje de regreso de Odiseo a Ítaca tras la finalización de la Guerra de Troya.", "Literatura", "DISPONIBLE", "es"),
        ("William Shakespeare", "Hamlet", "El príncipe de Dinamarca busca vengar la muerte de su padre a manos de su tío Claudio.", "Literatura", "PRESTADO", "es"),
        ("Leo Tolstoy", "Guerra y Paz", "Una monumental crónica de las vidas de familias aristocráticas durante las guerras napoleónicas.", "Literatura", "DISPONIBLE", "es"),
        ("Isabel Allende", "La casa de los espíritus", "Cuatro generaciones de la familia Trueba en un entorno de pasiones, magia y cambios políticos.", "Literatura", "RESERVADO", "es"),
        ("Juan Rulfo", "Pedro Páramo", "Juan Preciado viaja al pueblo fantasma de Comala en busca de su padre, un cacique despiadado.", "Literatura", "DISPONIBLE", "es"),
        ("Charles Dickens", "Historia de dos ciudades", "Un relato sobre la redención y el sacrificio ambientado entre Londres y París durante la Revolución Francesa.", "Literatura", "DISPONIBLE", "es"),
        ("Virginia Woolf", "Al faro", "Una meditación sobre el tiempo, el arte y las relaciones familiares de la familia Ramsay.", "Literatura", "DISPONIBLE", "es"),
        ("Albert Camus", "El extranjero", "Meursault vive su día a día de forma apática hasta que comete un crimen aparentemente absurdo.", "Literatura", "PRESTADO", "es"),

        # === CIENCIA ===
        ("Charles Darwin", "El Origen de las Especies", "La obra fundamental que introdujo la teoría de la evolución por selección natural.", "Ciencia", "PRESTADO", "es"),
        ("Stephen Hawking", "Breve Historia del Tiempo", "Un viaje explicativo a través del espacio-tiempo, la relatividad y los agujeros negros.", "Ciencia", "DISPONIBLE", "es"),
        ("Carl Sagan", "Cosmos", "Una magistral obra de divulgación sobre el universo, la evolución planetaria y la ciencia moderna.", "Ciencia", "DISPONIBLE", "es"),
        ("Richard Dawkins", "El gen egoísta", "Una revolucionaria perspectiva evolutiva centrada en el papel de los genes en lugar del individuo.", "Ciencia", "DISPONIBLE", "es"),
        ("Isaac Newton", "Principia Mathematica", "El tratado físico donde se enuncian las leyes del movimiento y la gravitación universal.", "Ciencia", "DISPONIBLE", "es"),
        ("Albert Einstein", "Sobre la teoría de la relatividad", "La explicación accesible de la famosa teoría especial y general de la relatividad espacio-temporal.", "Ciencia", "RESERVADO", "es"),
        ("Rachel Carson", "Primavera silenciosa", "Un libro de alerta ecológica que expone el impacto devastador de los pesticidas químicos.", "Ciencia", "DISPONIBLE", "es"),
        ("James Watson", "La doble hélice", "El relato personal y científico sobre el emocionante descubrimiento de la estructura del ADN.", "Ciencia", "PRESTADO", "es"),
        ("Neil deGrasse Tyson", "Astrofísica para personas con prisa", "Una guía rápida y amena sobre las fuerzas cuánticas y cósmicas que rigen el universo.", "Ciencia", "DISPONIBLE", "es"),
        ("Michio Kaku", "Física de lo imposible", "Un análisis científico sobre la viabilidad futura de tecnologías como la teletransportación.", "Ciencia", "DISPONIBLE", "es"),
        ("Bill Bryson", "Una breve historia de casi todo", "Un ameno recorrido divulgativo sobre cómo pasamos de la nada al desarrollo de la civilización.", "Ciencia", "DISPONIBLE", "es"),
        ("Siddhartha Mukherjee", "El emperador de todos los males", "Una biografía exhaustiva y humana sobre el desarrollo de la investigación del cáncer.", "Ciencia", "RESERVADO", "es"),
        ("Oliver Sacks", "El hombre que confundió a su mujer con un sombrero", "Relatos clínicos sobre pacientes con extraños e fascinantes trastornos neurológicos.", "Ciencia", "DISPONIBLE", "es"),
        ("Brian Greene", "El universo elegante", "Una explicación detallada sobre la teoría de supercuerdas y la búsqueda de la teoría unificada.", "Ciencia", "PRESTADO", "es"),
        ("Carlo Rovelli", "Siete breves lecciones de física", "Una hermosa síntesis de la relatividad, la mecánica cuántica y las partículas elementales.", "Ciencia", "DISPONIBLE", "es"),
        ("Marie Curie", "Investigaciones sobre las sustancias radiactivas", "La tesis fundamental que detalla el aislamiento del radio y el polonio.", "Ciencia", "DISPONIBLE", "es"),
        ("Jared Diamond", "Armas, gérmenes y acero", "Un estudio sobre los factores ambientales que moldearon el éxito de diferentes civilizaciones.", "Ciencia", "DISPONIBLE", "es"),
        ("Edward O. Wilson", "La diversidad de la vida", "Una exploración del proceso de especiación y el impacto humano sobre la biosfera terrestre.", "Ciencia", "DISPONIBLE", "es"),
        ("Steven Pinker", "Cómo funciona la mente", "Un enfoque evolutivo y computacional para comprender las facultades del cerebro humano.", "Ciencia", "PRESTADO", "es"),
        ("Ben Goldacre", "Mala ciencia", "Un mordaz análisis que desmitifica los engaños médicos, las dietas milagro y las pseudociencias.", "Ciencia", "DISPONIBLE", "es"),
        ("Daniel Kahneman", "Pensar rápido, pensar despacio", "Un estudio psicológico sobre los dos sistemas que dirigen nuestra forma de razonar y elegir.", "Ciencia", "DISPONIBLE", "es"),
        ("James Gleick", "Caos: La creación de una ciencia", "La fascinante crónica del desarrollo de la teoría del caos y los fractales geométricos.", "Ciencia", "DISPONIBLE", "es"),

        # === FILOSOFÍA ===
        ("Platón", "La República", "Un diálogo filosófico monumental sobre la justicia, el Estado ideal y el mito de la caverna.", "Filosofía", "PRESTADO", "es"),
        ("Sun Tzu", "El Arte de la Guerra", "El tratado militar cuyas estrategias se aplican hoy al liderazgo y la toma de decisiones.", "Filosofía", "DISPONIBLE", "es"),
        ("Friedrich Nietzsche", "Así habló Zaratustra", "La obra cumbre que introduce el concepto del superhombre y la muerte de Dios.", "Filosofía", "DISPONIBLE", "es"),
        ("Aristóteles", "Ética a Nicómaco", "La investigación fundamental sobre la virtud, la justicia y la búsqueda de la felicidad.", "Filosofía", "DISPONIBLE", "es"),
        ("René Descartes", "Discurso del método", "El tratado racionalista que establece la duda metódica como base para el conocimiento.", "Filosofía", "DISPONIBLE", "es"),
        ("Immanuel Kant", "Crítica de la razón pura", "Un riguroso examen sobre los límites de la metafísica y la naturaleza del entendimiento humano.", "Filosofía", "RESERVADO", "es"),
        ("Karl Marx", "El Capital", "Un exhaustivo análisis crítico de la economía política y el funcionamiento del capitalismo.", "Filosofía", "DISPONIBLE", "es"),
        ("Jean-Paul Sartre", "El ser y la nada", "La biblia del existencialismo que analiza la libertad absoluta y la angustia humana.", "Filosofía", "PRESTADO", "es"),
        ("Maquiavelo", "El Príncipe", "El clásico tratado político sobre las dinámicas del poder y la conservación del Estado.", "Filosofía", "DISPONIBLE", "es"),
        ("Séneca", "Cartas a Lucilio", "Consejos prácticos morales que constituyen una excelente introducción al estoicismo antiguo.", "Filosofía", "DISPONIBLE", "es"),
        ("Marco Aurelio", "Meditaciones", "Reflexiones personales sobre el deber, la ecuanimidad y la fortaleza espiritual estoica.", "Filosofía", "DISPONIBLE", "es"),
        ("Thomas Hobbes", "Leviatán", "La obra fundacional del contrato social sobre la necesidad de un Estado fuerte y centralizado.", "Filosofía", "DISPONIBLE", "es"),
        ("John Locke", "Segundo Tratado sobre el Gobierno Civil", "El texto base del liberalismo que defiende los derechos naturales a la vida y propiedad.", "Filosofía", "PRESTADO", "es"),
        ("Jean-Jacques Rousseau", "El contrato social", "Una propuesta filosófica sobre la libertad, la igualdad jurídica y la voluntad general.", "Filosofía", "DISPONIBLE", "es"),
        ("Arthur Schopenhauer", "El mundo como voluntad y representación", "Un sistema filosófico pesimista que define la existencia como un deseo insaciable.", "Filosofía", "RESERVADO", "es"),
        ("Byung-Chul Han", "La sociedad del cansancio", "Un ensayo contemporáneo sobre cómo la autoexigencia nos conduce al agotamiento psicológico.", "Filosofía", "DISPONIBLE", "es"),
        ("Simone de Beauvoir", "El segundo sexo", "El ensayo fundacional que analiza las causas históricas de la opresión de la mujer.", "Filosofía", "DISPONIBLE", "es"),
        ("Baruch Spinoza", "Ética", "Un tratado racionalista geométrico que redefine a Dios como la naturaleza misma.", "Filosofía", "DISPONIBLE", "es"),
        ("Michel Foucault", "Vigilar y castigar", "Un estudio sobre el nacimiento de la prisión moderna y las estructuras de control social.", "Filosofía", "PRESTADO", "es"),
        ("Zygmunt Bauman", "Modernidad líquida", "Un análisis sociológico sobre la fragilidad e inestabilidad de las relaciones humanas actuales.", "Filosofía", "DISPONIBLE", "es"),
        ("Thomas Kuhn", "La estructura de las revoluciones científicas", "El texto que acuñó el término 'cambio de paradigma' en la evolución de las ciencias.", "Filosofía", "DISPONIBLE", "es"),
        ("Walter Benjamin", "La obra de arte en la época de su reproductibilidad técnica", "Un ensayo estético sobre la pérdida del aura única de las obras de arte.", "Filosofía", "DISPONIBLE", "es"),

        # === ARTE ===
        ("Ernst Gombrich", "Historia del Arte", "El manual de referencia más famoso del mundo que narra la evolución del arte universal.", "Arte", "PRESTADO", "es"),
        ("Giorgio Vasari", "Las vidas de los más excelentes pintores", "Biografías fundamentales de los grandes maestros del Renacimiento italiano.", "Arte", "DISPONIBLE", "es"),
        ("Leonardo da Vinci", "Tratado de la pintura", "Anotaciones científicas y estéticas del genio florentino sobre la perspectiva y la luz.", "Arte", "DISPONIBLE", "es"),
        ("Wassily Kandinsky", "De lo espiritual en el arte", "El manifiesto plástico que sentó las bases teóricas de la abstracción pictórica moderna.", "Arte", "DISPONIBLE", "es"),
        ("Umberto Eco", "Historia de la belleza", "Un recorrido estético y visual sobre cómo ha cambiado el concepto de lo bello en la historia.", "Arte", "RESERVADO", "es"),
        ("Umberto Eco", "Historia de la fealdad", "Un complemento filosófico que analiza el rechazo, lo macabro y lo grotesco en el arte.", "Arte", "DISPONIBLE", "es"),
        ("John Ruskin", "Las siete lámparas de la arquitectura", "Los principios morales y artísticos que rigen el diseño y la preservación constructiva.", "Arte", "DISPONIBLE", "es"),
        ("Le Corbusier", "Hacia una arquitectura", "El manifesto funcionalista que revolucionó el urbanismo y la edificación moderna.", "Arte", "PRESTADO", "es"),
        ("Heinrich Wölfflin", "Conceptos fundamentales de la historia del arte", "El análisis formal comparativo entre el Renacimiento clásico y la exuberancia barroca.", "Arte", "DISPONIBLE", "es"),
        ("Robert Hughes", "El impacto de lo nuevo", "Una vibrante crónica sobre el auge, provocación y desarrollo del arte de vanguardia.", "Arte", "DISPONIBLE", "es"),
        ("Susan Sontag", "Sobre la fotografía", "Una serie de lúcidos ensayos sobre el impacto ético y estético de las imágenes capturadas.", "Arte", "DISPONIBLE", "es"),
        ("John Berger", "Modos de ver", "Un texto analítico que cambia la perspectiva de cómo interpretamos la pintura y la publicidad.", "Arte", "PRESTADO", "es"),
        ("Rudolf Arnheim", "Arte y percepción visual", "Un enfoque basado en la psicología de la Gestalt aplicado al análisis de las artes visuales.", "Arte", "DISPONIBLE", "es"),
        ("Gilles Deleuze", "Francis Bacon: Lógica de la sensación", "Un estudio filosófico sobre la distorsión corporal y pictórica en la obra de Bacon.", "Arte", "RESERVADO", "es"),
        ("Erwin Panofsky", "El significado en las artes visuales", "La obra metodológica fundamental para el estudio de la iconografía e iconología.", "Arte", "DISPONIBLE", "es"),
        ("Adolf Loos", "Ornamento y delito", "Un manifiesto crítico contra la decoración superflua en los objetos y la arquitectura.", "Arte", "DISPONIBLE", "es"),
        ("Paul Klee", "Diarios 1898-1918", "Anotaciones íntimas sobre la formación estética, el color y el proceso creativo del pintor.", "Arte", "DISPONIBLE", "es"),
        ("Charles Baudelaire", "El pintor de la vida moderna", "El ensayo que define la figura del flâneur y la belleza transitoria de la modernidad.", "Arte", "DISPONIBLE", "es"),
        ("Arthur Danto", "Después del fin del arte", "Un análisis sobre la condición del arte contemporáneo tras la era de las vanguardias.", "Arte", "PRESTADO", "es"),
        ("Roland Barthes", "La cámara lúcida", "Una íntima meditación sobre la fotografía, la memoria, la ausencia y la muerte.", "Arte", "DISPONIBLE", "es"),
        ("Kenneth Clark", "El desnudo", "Un exhaustivo estudio histórico del desnudo humano en la tradición artística occidental.", "Arte", "DISPONIBLE", "es"),
        ("Vincent van Gogh", "Cartas a Theo", "La emotiva correspondencia que revela la genialidad, pobreza y tormento del pintor.", "Arte", "DISPONIBLE", "es"),

        # === TECNOLOGÍA ===
        ("Stuart Russell", "Inteligencia Artificial", "El libro de texto definitivo utilizado a nivel mundial para comprender los agentes inteligentes.", "Tecnología", "DISPONIBLE", "es"),
        ("Alan Turing", "Sistemas de computación basados en lógica", "Recopilación de ensayos que definieron la computación moderna y la máquina universal.", "Tecnología", "DISPONIBLE", "es"),
        ("Donald Knuth", "El arte de programar ordenadores", "La enciclopedia técnica fundamental sobre análisis de algoritmos y estructuras de datos.", "Tecnología", "DISPONIBLE", "es"),
        ("Robert C. Martin", "Código Limpio", "Una guía de buenas prácticas esenciales para escribir software legible, elegante y mantenible.", "Tecnología", "DISPONIBLE", "es"),
        ("Kevin Mitnick", "El arte de la decepción", "El testimonio del hacker más famoso del mundo sobre las técnicas de ingeniería social.", "Tecnología", "PRESTADO", "es"),
        ("Ray Kurzweil", "La singularidad está cerca", "Un análisis prospectivo sobre cómo la fusión humano-máquina transformará nuestra especie.", "Tecnología", "RESERVADO", "es"),
        ("Linus Torvalds", "Just for Fun", "La divertida historia del creador de Linux sobre el nacimiento del sistema operativo libre.", "Tecnología", "DISPONIBLE", "es"),
        ("Andrew Tanenbaum", "Redes de computadoras", "La biblia académica para entender los protocolos, enrutamiento y arquitectura de Internet.", "Tecnología", "PRESTADO", "es"),
        ("Martin Fowler", "Refactoring", "El manual definitivo sobre cómo mejorar el diseño del código existente de forma segura.", "Tecnología", "DISPONIBLE", "es"),
        ("Thomas Cormen", "Introducción a los Algoritmos", "El riguroso libro de referencia matemática para el diseño eficiente de algoritmos.", "Tecnología", "DISPONIBLE", "es"),
        ("Walter Isaacson", "Steve Jobs", "La biografía oficial del cofundador de Apple que detalla la revolución de la tecnología de consumo.", "Tecnología", "DISPONIBLE", "es"),
        ("Christopher Bishop", "Reconocimiento de Patrones", "El texto avanzado matemático clave para el desarrollo del Deep Learning moderno.", "Tecnología", "RESERVADO", "es"),
        ("Erich Gamma", "Patrones de Diseño", "La obra clásica que introdujo soluciones reutilizables para el desarrollo de software orientado a objetos.", "Tecnología", "DISPONIBLE", "es"),
        ("Edward Snowden", "Vigilancia permanente", "El testimonio del analista que reveló los programas de espionaje masivo digital del gobierno.", "Tecnología", "DISPONIBLE", "es"),
        ("Kai-Fu Lee", "Superpotencias de la Inteligencia Artificial", "Un análisis geopolítico sobre la carrera tecnológica entre Silicon Valley y China.", "Tecnología", "PRESTADO", "es"),
        ("Nick Bostrom", "Superinteligencia", "Un profundo examen sobre los riesgos existenciales si la IA supera la capacidad humana.", "Tecnología", "DISPONIBLE", "es"),
        ("Cathy O'Neil", "Armas de destrucción matemática", "Cómo el uso de algoritmos y Big Data amplifica la desigualdad y sesga los derechos civiles.", "Tecnología", "DISPONIBLE", "es"),
        ("Tim Berners-Lee", "Tejiendo la Red", "El relato directo del creador de la World Wide Web sobre el diseño de la red mundial.", "Tecnología", "DISPONIBLE", "es"),
        ("Gene Kim", "El Proyecto Phoenix", "Una entretenida novela de TI que explica los principios de DevOps y la eficiencia laboral.", "Tecnología", "DISPONIBLE", "es"),
        ("Chris Anley", "El manual del hacker web", "La guía técnica práctica avanzada para auditoría de sistemas y ciberseguridad.", "Tecnología", "PRESTADO", "es"),
        ("Don Norman", "La psicología de los objetos cotidianos", "La obra maestra del diseño de experiencia de usuario (UX) y usabilidad de productos.", "Tecnología", "DISPONIBLE", "es"),
        ("Satoshi Nakamoto", "Bitcoin: Un sistema de efectivo electrónico", "El manifiesto original que dio origen a la tecnología Blockchain y las criptomonedas.", "Tecnología", "DISPONIBLE", "es"),

        # === EDUCACIÓN ===
        ("Paulo Freire", "Pedagogía del Oprimido", "El texto clásico que propone una educación liberadora basada en el diálogo crítico.", "Educación", "PRESTADO", "es"),
        ("Jean Piaget", "El nacimiento de la inteligencia en el niño", "La obra fundacional de la psicología constructivista del desarrollo cognitivo temprano.", "Educación", "DISPONIBLE", "es"),
        ("Lev Vygotsky", "Pensamiento y Lenguaje", "El análisis sobre la mediación social y cultural en el aprendizaje y el desarrollo humano.", "Educación", "DISPONIBLE", "es"),
        ("John Dewey", "Democracia y Educación", "La propuesta pragmática de aprender haciendo y la escuela como centro comunitario.", "Educación", "DISPONIBLE", "es"),
        ("Maria Montessori", "El método de la pedagogía científica", "La guía original sobre el ambiente preparado y la autoeducación en la infancia.", "Educación", "DISPONIBLE", "es"),
        ("Ken Robinson", "El Elemento", "Un llamado a transformar las escuelas rígidas para descubrir el talento y pasión individual.", "Educación", "RESERVADO", "es"),
        ("Howard Gardner", "Estructuras de la mente", "El libro que revolucionó la psicología al proponer la teoría de las inteligencias múltiples.", "Educación", "DISPONIBLE", "es"),
        ("Émile Durkheim", "Educación y sociología", "El estudio sociológico clásico sobre el rol de la escuela en la socialización moral.", "Educación", "PRESTADO", "es"),
        ("Edgar Morin", "Los siete saberes necesarios", "Una propuesta de la UNESCO orientada hacia la complejidad y la ética humana universal.", "Educación", "DISPONIBLE", "es"),
        ("Célestin Freinet", "Por una escuela del pueblo", "Técnicas pedagógicas modernas basadas en la imprenta escolar y el trabajo cooperativo.", "Educación", "DISPONIBLE", "es"),
        ("Carl Rogers", "Libertad y creatividad en la educación", "El enfoque humanista de la enseñanza centrado en el alumno y el crecimiento afectivo.", "Educación", "DISPONIBLE", "es"),
        ("Daniel Goleman", "Inteligencia Emocional", "La tesis que demuestra la importancia del autocontrol y la empatía en el rendimiento escolar.", "Educación", "RESERVADO", "es"),
        ("B.F. Skinner", "Tecnología de la enseñanza", "La propuesta del conductismo radical aplicada al diseño de máquinas de enseñar.", "Educación", "DISPONIBLE", "es"),
        ("Henry Giroux", "Teoría y resistencia en educación", "Un marco teórico para comprender el aula como espacio de contestación y lucha política.", "Educación", "DISPONIBLE", "es"),
        ("Pierre Bourdieu", "La reproducción", "Un crudo análisis sobre cómo el sistema educativo perpetúa las desigualdades de clase.", "Educación", "PRESTADO", "es"),
        ("Philippe Meirieu", "Frankenstein educador", "Una reflexión ética sobre el peligro de querer moldear al alumno según el deseo del maestro.", "Educación", "DISPONIBLE", "es"),
        ("David Ausubel", "Psicología educativa", "La teoría del aprendizaje significativo basado en los conocimientos previos del alumno.", "Educación", "DISPONIBLE", "es"),
        ("John Hattie", "Aprendizaje Visible", "El mayor estudio empírico estadístico sobre qué estrategias pedagógicas funcionan mejor.", "Educación", "DISPONIBLE", "es"),
        ("Francesco Tonucci", "La ciudad de los niños", "Una innovadora propuesta urbana y escolar que aboga por escuchar la voz infantil.", "Educación", "PRESTADO", "es"),
        ("Neil Postman", "El fin de la educación", "Una crítica a la visión tecnológica corporativa y una defensa de los valores humanos escolares.", "Educación", "DISPONIBLE", "es"),
        ("bell hooks", "Enseñar a transgredir", "Una perspectiva antirracista y feminista sobre la educación como práctica colectiva de la libertad.", "Educación", "DISPONIBLE", "es"),
        ("Jerome Bruner", "El proceso de la educación", "La introducción del aprendizaje por descubrimiento y el concepto de currículo en espiral.", "Educación", "DISPONIBLE", "es"),

        # === DERECHO ===
        ("Víctor Pérez", "Introducción al Derecho", "Un compendio educativo estructurado para comprender las bases e instituciones jurídicas.", "Derecho", "DISPONIBLE", "es"),
        ("Hans Kelsen", "Teoría pura del derecho", "La cumbre del positivismo que estructura el ordenamiento jurídico en forma de pirámid.", "Derecho", "DISPONIBLE", "es"),
        ("Cesare Beccaria", "De los delitos y de las penas", "El tratado ilustrado que sentó las bases del derecho penal moderno y abolió la tortura.", "Derecho", "DISPONIBLE", "es"),
        ("H.L.A. Hart", "El concepto de derecho", "El análisis analítico anglosajón que divide las normas en reglas primarias y secundarias.", "Derecho", "PRESTADO", "es"),
        ("John Rawls", "Teoría de la Justicia", "La propuesta del velo de la ignorancia para diseñar una sociedad justa y equitativa.", "Derecho", "RESERVADO", "es"),
        ("Montesquieu", "El espíritu de las leyes", "El célebre tratado que propuso la división del Estado en los poderes ejecutivo, legislativo y judicial.", "Derecho", "DISPONIBLE", "es"),
        ("Ronald Dworkin", "Los derechos en serio", "Una crítica al positivismo radical, argumentando que el derecho incluye principios y moral.", "Derecho", "DISPONIBLE", "es"),
        ("Robert Alexy", "Teoría de los derechos fundamentales", "El desarrollo del principio de proporcionalidad para ponderar conflictos entre derechos civiles.", "Derecho", "PRESTADO", "es"),
        ("Carl Schmitt", "Teología política", "Un polémico análisis sobre la soberanía, el estado de excepción y los conceptos constitucionales.", "Derecho", "DISPONIBLE", "es"),
        ("Luigi Ferrajoli", "Derecho y razón", "La monumental obra de referencia sobre el garantismo penal y la protección constitucional.", "Derecho", "DISPONIBLE", "es"),
        ("Gustav Radbruch", "Introducción a la filosofía del derecho", "El texto que enuncia que una ley extremadamente injusta carece de validez jurídica.", "Derecho", "DISPONIBLE", "es"),
        ("Norberto Bobbio", "Teoría del ordenamiento jurídico", "Un análisis estructural sobre la unidad, coherencia y lagunas de los sistemas legales.", "Derecho", "RESERVADO", "es"),
        ("Jean Bodin", "Los seis libros de la República", "El tratado histórico que acuñó y sistematizó el concepto moderno de soberanía estatal.", "Derecho", "DISPONIBLE", "es"),
        ("Hugo Grocio", "Del derecho de la guerra y de la paz", "El texto fundacional del derecho internacional que regula las relaciones interestatales.", "Derecho", "DISPONIBLE", "es"),
        ("Karl Llewellyn", "El arbusto de la zarza", "La obra clave del realismo jurídico estadounidense sobre cómo juzgan realmente los tribunales.", "Derecho", "PRESTADO", "es"),
        ("Duncan Kennedy", "La enseñanza del derecho como acción política", "Un análisis de los Critical Legal Studies que expone la carga ideológica en las leyes.", "Derecho", "DISPONIBLE", "es"),
        ("Claus Roxin", "Derecho Penal: Parte General", "La enciclopedia alemana indispensable para comprender la teoría del delito y la imputación objetiva.", "Derecho", "DISPONIBLE", "es"),
        ("Michel Villey", "Compendio de filosofía del derecho", "Un brillante retorno metodológico a la tradición clásica del derecho natural aristélico.", "Derecho", "DISPONIBLE", "es"),
        ("Eduardo García Máynez", "Introducción al estudio del derecho", "El manual clásico de referencia en Latinoamérica para comprender la técnica jurídica.", "Derecho", "PRESTADO", "es"),
        ("Piero Calamandrei", "Elogio de los jueces escrito por un abogado", "Un entrañable y agudo retrato sobre las debilidades y virtudes del proceso judicial.", "Derecho", "DISPONIBLE", "es"),
        ("Guillermo Cabanellas", "Diccionario enciclopédico de derecho usual", "El compendio lexicográfico esencial para el uso correcto de la terminología legal.", "Derecho", "DISPONIBLE", "es"),
        ("Jürgen Habermas", "Facticidad y validez", "Una teoría del derecho basada en la acción comunicativa y la deliberación democrática.", "Derecho", "DISPONIBLE", "es"),

        # === MEDICINA ===
        ("Henry Gray", "Anatomía Humana", "La guía clásica mundial de referencia médica descriptiva de los sistemas corporales.", "Medicina", "RESERVADO", "es"),
        ("Guyton y Hall", "Tratado de Fisiología Médica", "La biblia de estudio universitario para comprender los mecanismos celulares y orgánicos.", "Medicina", "DISPONIBLE", "es"),
        ("Harrison", "Principios de Medicina Interna", "El tratado clínico global indispensable para el diagnóstico y tratamiento de patologías.", "Medicina", "DISPONIBLE", "es"),
        ("Robbins y Cotran", "Patología estructural y funcional", "El texto de referencia para comprender los cambios celulares que provocan las enfermedades.", "Medicina", "DISPONIBLE", "es"),
        ("Paul de Kruif", "Los cazadores de microbios", "La emocionante crónica histórica sobre el descubrimiento de bacterias, virus y vacunas.", "Medicina", "DISPONIBLE", "es"),
        ("Hipócrates", "Tratados hipocráticos", "Escritos éticos y médicos antiguos que inauguraron el juramento y método clínico.", "Medicina", "DISPONIBLE", "es"),
        ("Atul Gawande", "Ser mortal", "Una lúcida reflexión sobre las limitaciones de la medicina moderna frente a la vejez y la muerte.", "Medicina", "PRESTADO", "es"),
        ("Eric Topol", "Medicina profunda", "Cómo la Inteligencia Artificial y el Big Data humanizarán el diagnóstico médico del futuro.", "Medicina", "DISPONIBLE", "es"),
        ("Frank Netter", "Atlas de Anatomía Humana", "El compendio ilustrado a mano de mayor calidad y precisión visual del cuerpo humano.", "Medicina", "DISPONIBLE", "es"),
        ("Goodman y Gilman", "Las bases farmacológicas de la terapéutica", "El texto avanzado indispensable sobre el mecanismo de acción de los fármacos.", "Medicina", "PRESTADO", "es"),
        ("James Moore", "Inmunología básica", "Un análisis simplificado sobre las respuestas del sistema inmune ante infecciones y vacunas.", "Medicina", "DISPONIBLE", "es"),
        ("Michel Foucault", "El nacimiento de la clínica", "Una mirada arqueológica filosófica sobre cómo cambió la mirada médica en el siglo XIX.", "Medicina", "DISPONIBLE", "es"),
        ("David Wertham", "El cerebro en la mesa de operaciones", "Casos clínicos fascinantes de neurocirugía compleja comentados paso a paso.", "Medicina", "RESERVADO", "es"),
        ("Sackett", "Medicina basada en la evidencia", "El manual que definió el método científico moderno para la toma de decisiones clínicas.", "Medicina", "DISPONIBLE", "es"),
        ("Robert Sapolsky", "Compórtate", "Una magistral neurobiología de nuestras mejores y peores conductas humanas.", "Medicina", "DISPONIBLE", "es"),
        ("John Hall", "Tratado de Cardiología", "Estudio clínico avanzado de los desórdenes vasculares y patologías del corazón humano.", "Medicina", "PRESTADO", "es"),
        ("Andreas Vesalio", "De humani corporis fabrica", "El texto histórico renacentista que fundó la anatomía científica mediante la disección.", "Medicina", "DISPONIBLE", "es"),
        ("Emil Kraepelin", "Tratado de Psiquiatría", "La clasificación clínica alemana fundacional de los trastornos mentales mayores.", "Medicina", "DISPONIBLE", "es"),
        ("William Osler", "Aequanimitas", "Discursos y ensayos éticos humanistas sobre la conducta profesional del médico.", "Medicina", "DISPONIBLE", "es"),
        ("David Hunter", "Enfermedades profesionales", "Un manual de referencia clínica sobre los riesgos de salud en los entornos laborales.", "Medicina", "PRESTADO", "es"),
        ("Alexander Fleming", "Sobre el cultivo de penicilina", "El artículo científico original que reportó el aislamiento fortuito del primer antibiótico.", "Medicina", "DISPONIBLE", "es"),
        ("Santiago Ramón y Cajal", "Recuerdos de mi vida", "La autobiografía del premio Nobel español que descubrió la individualidad de las neuronas.", "Medicina", "DISPONIBLE", "es"),

        # === MATEMÁTICA ===
        ("Euclides", "Elementos", "El tratado geométrico deductivo más influyente de la historia intelectual humana.", "Matemática", "DISPONIBLE", "es"),
        ("G.H. Hardy", "Apología de un matemático", "Una conmovedora justificación personal sobre el valor de la matemática pura y estética.", "Matemática", "DISPONIBLE", "es"),
        ("Marcus du Sautoy", "La música de los números primos", "Un viaje fascinante por el misterio de los números primos y la hipótesis de Riemann.", "Matemática", "DISPONIBLE", "es"),
        ("Simon Singh", "El último teorema de Fermat", "La épica crónica de Andrew Wiles para resolver el acertijo matemático más famoso.", "Matemática", "PRESTADO", "es"),
        ("Ian Stewart", "Las 17 ecuaciones que cambiaron el mundo", "Un repaso ameno por las fórmulas matemáticas fundamentales desde Pitágoras hasta la relatividad.", "Matemática", "DISPONIBLE", "es"),
        ("Richard Courant", "¿Qué es la matemática?", "Una introducción magistral y comprensible que captura la esencia real de la disciplina.", "Matemática", "DISPONIBLE", "es"),
        ("Carl Friedrich Gauss", "Disquisitiones Arithmeticae", "La obra cumbre que estructuró la teoría de números moderna de forma sistemática.", "Matemática", "DISPONIBLE", "es"),
        ("John von Neumann", "Fundamentos matemáticos de la mecánica cuántica", "El texto riguroso que proveyó el marco formal de espacios de Hilbert a la física.", "Matemática", "RESERVADO", "es"),
        ("Edward Frenkel", "Amor y matemáticas", "El relato personal de un genio ruso que expone la belleza oculta del programa de Langlands.", "Matemática", "DISPONIBLE", "es"),
        ("Steven Strogatz", "El placer de la X", "Un recorrido guiado y lúdico desde la acritmética escolar hasta el análisis multivariable.", "Matemática", "DISPONIBLE", "es"),
        ("Paul Erdős", "Problemas de combinatoria", "Recopilación de teoremas y elegantes conjeturas sobre grafos y estructuras discretas.", "Matemática", "PRESTADO", "es"),
        ("Keith Devlin", "El lenguaje de las matemáticas", "Una explicación accesible sobre cómo la matemática hace visible lo invisible del mundo.", "Matemática", "DISPONIBLE", "es"),
        ("Roger Penrose", "El camino a la realidad", "Una monumental guía matemática completa para comprender las leyes de la física moderna.", "Matemática", "RESERVADO", "es"),
        ("Benoît Mandelbrot", "La geometría fractal de la naturaleza", "El texto revolucionario que descubrió las formas autosimilares complejas de la realidad.", "Matemática", "DISPONIBLE", "es"),
        ("Douglas Hofstadter", "Gödel, Escher, Bach", "Un genial lazo dorado interdisciplinar sobre la autorreferencia, la mente y el infinito.", "Matemática", "DISPONIBLE", "es"),
        ("Terence Tao", "Análisis Real: Volumen 1", "El riguroso y didáctico manual de introducción al cálculo moderno y la teoría de conjuntos.", "Matemática", "PRESTADO", "es"),
        ("George Pólya", "Cómo resolverlo", "El manual clásico de heurística que enseña estrategias lógicas para abordar problemas.", "Matemática", "DISPONIBLE", "es"),
        ("Al-Juarismi", "Compendio de cálculo por reintegración", "El manuscrito histórico persa que fundó el álgebra y los métodos algorítmicos.", "Matemática", "DISPONIBLE", "es"),
        ("Stephen Wolfram", "Un nuevo tipo de ciencia", "Una controvertida propuesta que utiliza autómatas celulares para explicar la complejidad.", "Matemática", "DISPONIBLE", "es"),
        ("David Hilbert", "Problemas matemáticos", "La célebre conferencia de 1900 que listó los 23 desafíos que guiaron el siglo XX.", "Matemática", "DISPONIBLE", "es"),
        ("Martin Gardner", "¡Ajá! Inspiración paradójica", "Una recopilación de acertijos de lúgica recreativa y rompecabezas matemáticos.", "Matemática", "PRESTADO", "es"),
        ("Gilbert Strang", "Álgebra Lineal y sus aplicaciones", "El manual universitario indispensable para entender vectores, matrices y transformaciones.", "Matemática", "DISPONIBLE", "es")
    ]

    cursor.executemany("""
        INSERT INTO libros (autor, titulo, sinopsis, genero, estado, idioma)
        VALUES (?, ?, ?, ?, ?, ?)
    """, libros_iniciales)

    conn.commit()
    conn.close()

# 3. MÓDULO DE CONSULTAS Y FILTROS SEMÁNTICOS / BUSCADOR INTERACTIVO
def consultar_base_datos(termino, idioma, tipo_busqueda):
    """Maneja las peticiones del buscador interactivo de dos pasos."""
    conn = obtener_conexion()
    cursor = conn.cursor()

    #1: Buscar todas las obras escritas por el autor
    if tipo_busqueda == "obras":
        cursor.execute(
            "SELECT titulo FROM libros WHERE autor LIKE ? AND idioma = ?", 
            (f"%{termino}%", idioma)
        )
        filas = cursor.fetchall()
        conn.close()

        if filas:
            lista_obras = [f["titulo"] for f in filas]
            return {
                "exito": True,
                "tipo": "lista_desplegable",
                "titulo": f"Libros locales de: {termino}",
                "datos": lista_obras
            }
        else:
            return {"exito": False, "mensaje": f"No se encontraron libros del autor '{termino}' en este idioma."}

    #2: Extraer la sinopsis nativa del libro seleccionado
    elif tipo_busqueda == "sinopsis_obra":
        cursor.execute(
            "SELECT sinopsis FROM libros WHERE titulo = ? AND idioma = ?", 
            (termino, idioma)
        )
        fila = cursor.fetchone()
        conn.close()

        if fila:
            return {
                "exito": True,
                "tipo": "texto",
                "titulo": f"Sinopsis de: {termino}",
                "datos": fila["sinopsis"]
            }
        else:
            return {"exito": False, "mensaje": "No se pudo recuperar la sinopsis."}

    conn.close()
    return {"exito": False, "mensaje": "Tipo de consulta no válido."}

# 4. FUNCIONES DE ADMINISTRACIÓN INTERNA 
def obtener_todos_los_libros():
    """Devuelve la colección completa de los 200 libros para alimentar el catálogo."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, autor, titulo, sinopsis, genero, estado, idioma FROM libros ORDER BY id DESC")
    filas = cursor.fetchall()
    conn.close()
    return [dict(f) for f in filas]

def insertar_nuevo_libro(autor, titulo, sinopsis, genero, estado, idioma):
    """Agrega de forma segura un nuevo libro a la base de datos (Acción + Agregar libro)."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO libros (autor, titulo, sinopsis, genero, estado, idioma)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (autor, titulo, sinopsis, genero, estado, idioma))
    conn.commit()
    conn.close()

def eliminar_libro_por_id(libro_id):
    """Borra de forma definitiva un libro mediante su ID numérico (Acción 🗑️ Eliminar)."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (libro_id,))
    conn.commit()
    conn.close()