
El proyecto tiene la siguiente estructura:
├── main.py
├── automata/
│   ├── __init__.py
│   ├── automata.py
│   ├── transitions.py
│
├── drawing/
│   ├── __init__.py
│   ├── shapes.py
│
├── visualization/
│   ├── __init__.py
│   ├── graph.py
│
└── utils/
    ├── __init__.py
    ├── formatter.py

Las obligaciones recaen de la siguiente manera:

1. main.py: Punto de entrada del programa. Orquestación del sistema .Interacción con el usuario. Llamado a los módulos. Flujo general del programa. NO tiene lógica del automata ni lógica del dibujo

2. automata.py: Contiene la definición del presente automata. Es el corazón 

3. transitions.py: Define la función, la tabla y la lógica para pasar de un estado a otro.

4. shapes.py: funciones que dibujan.

5. graph.py: generación del grafo del automata.

6. formatter.py: Formateo de salidas por consola, estética.