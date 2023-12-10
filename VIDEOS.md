### Django Nivel Inicial - Arquitectura

#### Modulo 1
Unidad 1: Instalación y Primeros Pasos
- Instalación y Primeros Pasos: https://youtu.be/JRP0EffFDXQ
Unidad 2: Uso de los modelos del patrón MTV
- Patrón MTV: https://youtu.be/QpHUg_6RstI
Unidad 3: Panel de Administración
- Backend, models.py y admin.py: https://youtu.be/GK4LMY0yHSU
- Configuración de admin.py: https://youtu.be/g4sKM6QfKEs
- Relaciones 1-N de tablas en la base de datos: https://youtu.be/h5MzflSZtLM
Unidad 4: Registro de usuario y permisos
- Presentación de la unidad: https://youtu.be/aYB7FSGw8A0
- Power shell: https://youtu.be/okwfmEUb9ew
- Instalamos registration redux: https://youtu.be/AaqP3dcsKaQ
- Activación de usuario: https://youtu.be/eyzseLXnEJI
- Autenticación de usuario: https://youtu.be/U4FulX7MV1g

#### Modulo 2
Unidad 1: Debug y testing
- Presentación: https://youtu.be/3RlNp2ket_8
- Uso de marcas: https://youtu.be/9IYAnsjWm8w
- Uso de fixture: https://youtu.be/r4DGobKGdtM
- Cuando se ejecuta un fixture: https://youtu.be/HzH4CEQmHnc
- Acceso a base de datos: https://youtu.be/SY7De7L8K4g
- Archivo conftest.py: https://youtu.be/IGu89oToz3A
- Factory: https://youtu.be/zeIA8P45on8

Unidad 2: Maquetación de Frontend I
- Presentación: https://youtu.be/QJVFNBl5GOs
- Editor Bluegriffon: https://youtu.be/WvKPZCWHNTM
- DOM: https://youtu.be/Veplq-xj0sA
- Display: https://youtu.be/TMK3zVIv7dQ
- Position: https://youtu.be/rDJzmxQu57Y
- Margin y Padding: https://youtu.be/IUgja36Gg44
- CSS3: https://youtu.be/WIPJnDMVjX4
- Media Queries: https://youtu.be/maXZh5ZILWI
- Estilos en django: https://youtu.be/-m0oXSeFcAs
- Sistema de plantillas: https://youtu.be/J2hrbPm1iNg

Unidad 3: Maquetación de Frontend II
- Bootstrap, instalación y grid: https://youtu.be/Qvqf7Qz-45g
- Tablas, colores y botones: https://youtu.be/Dd6SC1544tw
- Listas, forms y navbars: https://youtu.be/tPXyDE5M9S4
- Uso de carrouselle en django, include y vínculos: https://youtu.be/1Djush7Ujvg
- Modal: https://youtu.be/m3-yuP0bEY0

Unidad 4: Maquetaión de Frontend III SASS
- Presentación: https://youtu.be/U4D2etTuAIw
- Estructura: https://youtu.be/2J3H3su749g
- Variables SASS: https://youtu.be/_j8PstYYoFs
- Tarea: https://youtu.be/bbl_MV3h-eo

### Django - Nivel Intermedio - Diseño de plataformas

#### Modulo 1
Unidad 1: Trabajo con formularios
- Introducción y cambio de estructura - app contacto: https://youtu.be/A5Z21x7dXS8
- Formulario de contacto-urls: https://www.youtube.com/watch?v=gi3JgqsP1Gs
- Formulario de contacto-models: https://www.youtube.com/watch?v=BaqG3xx9M1g&t=1s
- Formulario de contacto-frontend: https://www.youtube.com/watch?v=XTGIaSy9g4c&t=1s
- Formulario de contacto-admin: https://www.youtube.com/watch?v=znMPvegC_G4&t=1s
- Creación de app tienda: https://www.youtube.com/watch?v=i0-8jlmOAUI&t=1s
- Formulario de tienda: https://www.youtube.com/watch?v=XRb6Ue_jazE
- Views.py de tienda: https://www.youtube.com/watch?v=swhL6uXbLHM
- Visualización de productos: https://www.youtube.com/watch?v=zaV9giPHRQM&t=1s
- Lo que vimos en la unidad y lo que viene: https://www.youtube.com/watch?v=9RHnd7G44yA&t=2s

Unidad 2: Uso de templetags
- Comentarios de cambios en el sitio antes de iniciar: https://www.youtube.com/watch?v=ObrK0ee6_ds&t=1s
- Renderizar vista con clase en lugar de función - Uso de Templatetags en Django: https://www.youtube.com/watch?v=mphXASWxdFI&t=1s
- Uso de include filtros y variable de sessión en Django: https://www.youtube.com/watch?v=vfS0TltaNdg&t=1s
- Templatetags y filtros personalizados: https://www.youtube.com/watch?v=glMI8x1mkfw
- Lo que vimos y lo que vamos a ver la siguiente unidad: https://www.youtube.com/watch?v=spmYbjkmK08&t=3s
- Aplicación de la unidad: https://cursos.utnba.centrodeelearning.com/pluginfile.php/172851/mod_book/chapter/24397/librosonline.7z
- Parche de templatetags:
```
{% if request.session.el_pedido %}
    <span>{{producto|en_pedido:request.session.el_pedido}}</span>
{% endif %}
```

Unidad 3: Implementación de Signals
- Estructura de las Signals: https://www.youtube.com/watch?v=y6ce7mDKwnE
- Signals.py (referencia a archivo y comento accounts en urls.py): https://www.youtube.com/watch?v=1wPv_3iCpT0
- registro, login, logout (.html y views): https://www.youtube.com/watch?v=rnOSI71SIwc
- Login (forms.py, views.py, archivos .html): https://www.youtube.com/watch?v=zCGqjQZ23V0
- logout, registro(forms.py, views.py, archivos .html): https://www.youtube.com/watch?v=v6LBrz-0-bE
- signals: https://www.youtube.com/watch?v=uJy5j7rwHD4
- Lo que hemos visto, y lo que viene: https://www.youtube.com/watch?v=hBFL6FzdZjs

Unidad 4: Optimización del panel Admin
- Introducción: https://www.youtube.com/watch?v=5NJGNV_w0sI&t=1s 
- Acción en panel admin: https://www.youtube.com/watch?v=Rzo94BVZWfE&t=1s
- Acción en panel admin en clase:  https://www.youtube.com/watch?v=J5PU2b5sCl4&t=1s 
- Página intermedia al vuelo: https://www.youtube.com/watch?v=1PEIqzL7kTA&t=1s 
- Página intermedia en html: https://www.youtube.com/watch?v=4U655kj4bHw&t=1s
- Lo que hemos visto y lo que viene: https://www.youtube.com/watch?v=jPa-jGUKHro&t=1s

#### Modulo 2

Unidad 1: Comunicación con LocalStorage
- Presentación:  https://www.youtube.com/watch?v=PInO0jgb-tg&t=2s
- javaScript en Django: https://www.youtube.com/watch?v=ZyaCKJ6x6-4&t=1s
- javaScript - uso de var, let: https://www.youtube.com/watch?v=94RdHfOVDas&t=1s
- javaScript - declaración de funciones: https://www.youtube.com/watch?v=FJwmMtv6URg&t=1s
- CRUD en la base del explorador: https://www.youtube.com/watch?v=u3SaA--I7no&t=1s
- Interacción con variables de sesión II (no hay I): https://www.youtube.com/watch?v=YGeZvNftgXw&t=1s
- Interacción con variables de sesión III: https://www.youtube.com/watch?v=YGeZvNftgXw&t=1s
- Interacción con variables de sesión VI: https://www.youtube.com/watch?v=OQJz_QVD7TI&t=2s
- Interacción con variables de sesión V: https://www.youtube.com/watch?v=8R-HnjeVYX0&t=1s

Unidad 2: Animaciones I - GreenSock - GSAP
- Presentación: https://www.youtube.com/watch?v=xsETCDe2aoo&t=1s
- ¿Qué es jQuery?: https://www.youtube.com/watch?v=gxNM19W7Tgc&t=1s 
- Cuando se ejecuta jQuery?: https://www.youtube.com/watch?v=qpn0rk548w8&t=1s
- Selectores: https://www.youtube.com/watch?v=8K8yHbXRGbk&t=7s
- Uso de filtros: https://www.youtube.com/watch?v=OqBXRLRGeyw&t=1s
- Contenido HTML: https://www.youtube.com/watch?v=hK5gC2DSL5g&t=2s
- Estilos: https://www.youtube.com/watch?v=rf8TD1NIirg&t=1s
- Eventos I: https://www.youtube.com/watch?v=GjDrToRGTXI&t=1s
- Eventos II: https://www.youtube.com/watch?v=dAmCnglyvhU&t=1s
- Efectos: https://www.youtube.com/watch?v=CS6jvgae02U&t=2s 
- Lo que vimos y lo que se viene: https://www.youtube.com/watch?v=W_tGE8QPv8Q&t=1s

Unidad 3: Animaciones II - GreenSock - GSAP
- Presentación: https://www.youtube.com/watch?v=kskNimm37rk&t=1s
- Instalamos Green Sock y Plugins: https://www.youtube.com/watch?v=Az8nCTqlUkE&t=1s
- Primer Programa: https://www.youtube.com/watch?v=nII6eJrb4UU&t=1s
- From Set: https://www.youtube.com/watch?v=oZMDhy7Bd1c&t=4s 
- Scroll: https://www.youtube.com/watch?v=TzizjrNF6eQ&t=3s
- Threejs - Presentacion: https://www.youtube.com/watch?v=2qdUsWT1jL0&t=1s
- Threejs - Analisis de codigo: https://www.youtube.com/watch?v=FAzwmzYoMKw&t=2s
- Lo que vimos y lo que se viene: https://www.youtube.com/watch?v=60cUDvZHVB4&t=1s

Unidad 4: Consultas asíncronas - AJAX
- Creamos campo de formulario: https://www.youtube.com/watch?v=ADKgvFlhAEk&t=1s 
- Creamos urls py, views.py y archivo: https://www.youtube.com/watch?v=L45-pQBirLU&t=1s 
- Autocompletado de campos: https://www.youtube.com/watch?v=oIg19ljPQyY&t=2s
- jQuery UI y menú: https://www.youtube.com/watch?v=yWwdCwmFtd4&t=1s 
- Recuperamos productos con ajax: https://www.youtube.com/watch?v=mza7o-5eY9w&t=1s

### Django Nivel Avanzado - En producción

### Modulo 1

Unidad 1: 
- Introducción y programas a instalar: https://www.youtube.com/watch?v=Wp7z3GxO7_Y
- Creamos una maquina virtual: https://www.youtube.com/watch?v=i4p4YcR6SK0
- Configuramos interfaz de máquina virtual: https://www.youtube.com/watch?v=xZJqPY8lK94
- Instalamos servidor apache I: https://www.youtube.com/watch?v=e36Fbg7yGcs
- Instalamos servidor apache II: https://www.youtube.com/watch?v=fs1jPBGP8II
- Instalamos servidor apache III: https://www.youtube.com/watch?v=KGsIVpNs3Qg
- Instalación de módulos, creación de proyecto, configuración de permisos, actualización de wsgi.py y apache: https://www.youtube.com/watch?v=6CO05SLKhvw
- Creación de carpeta media y static – reconfiguración de apache: https://www.youtube.com/watch?v=Judl8O4qY_M
- Creamos conexión ftp y pasamos archivos desde nuestra app en windows: https://www.youtube.com/watch?v=AJAsTJFBFg4

Unidad 2: 
- Transacciones: https://www.youtube.com/watch?v=_jBH32NFRXc
- Triggers: https://www.youtube.com/watch?v=v8ub1CZjXfI
- Instalamos MariaDB: https://www.youtube.com/watch?v=nDqYc-MfaeM
- Instalamos php y phpmyadmin: https://www.youtube.com/watch?v=R4TEue8Vx9Q
- Configuración de Django: https://www.youtube.com/watch?v=SNEj8r8s3D4

Unidad 3: 
- Instalación de MongoDB: https://www.youtube.com/watch?v=lMkrNZKYzXs
- Mongo CRUD: https://www.youtube.com/watch?v=qWw37WoRjZ4
- Pymongo vs MongoEngine vs Djongo: https://www.youtube.com/watch?v=-qApTSsu_7E
- Integración con Pymongo: https://www.youtube.com/watch?v=rfEzz1UJY1E
- Integración con MongoEngine: https://www.youtube.com/watch?v=XiN-jyvlZ3E

Unidad 4: 
- Presentación de las tareas a realizar: https://www.youtube.com/watch?v=H9a0k-gJtgo
- Configurar Apache en otro puerto: https://www.youtube.com/watch?v=JyBpj3x4-7o
- Configurar NGINX para funcionar con Apache: https://www.youtube.com/watch?v=UwCotHQ_-_M

### Modulo 2
Unidad 1: Rest Api
-  Presentación e instalación
-  Serialización
-  Creación de CRUD

 Unidad 2: Carrito de compras.
-  Presentación y reorganización de app
-  https en desarrollo
-  Selección de productos
-  Registro de Usuario y datos de envío
-  Checkout

Unidad 3: SEO
-  Introducción – White Hat – Black Hat
-  Palabras claves – Optimización interna y externa
-  Microdatos
-  Json-Id
-  robot.txt y sitemap.xml

Unidad 4: Últimos pasos
-  WYSIWYG - ckeditor
-  django-simple-history
-  https en producción
-  Aclaración