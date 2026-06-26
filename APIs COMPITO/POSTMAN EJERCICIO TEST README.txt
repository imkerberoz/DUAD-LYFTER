

1. Descripción general de la API

Nombre de la API: JSONPlaceholder  
URL base: `https://jsonplaceholder.typicode.com`  
Tipo: API de prueba / Fake REST API  

JSONPlaceholder es una *API gratuita y pública* diseñada especialmente para pruebas y aprendizaje. Permite practicar todas las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sin necesidad de registro ni clave de API. 

Proporciona recursos falsos como Posts, Users, Comments, Albums, Photos, etc. Es muy utilizada en cursos y tutoriales para aprender sobre APIs REST y Postman.

-----------------------------------------------------------------------------------------

2. Explicación de cada solicitud

1. GET - Lista de Posts
- Método: `GET`
- Endpoint: `/posts`
- Parámetros: Ninguno (opcional: `?_limit=10`)
- Descripción: Obtiene una lista de 100 posts.
- Código de respuesta esperado: `200 OK`
- Respuesta: Array de objetos JSON

2. GET - Obtener un Post específico
- Método: `GET`
- Endpoint: `/posts/1`
- Parámetros: Ninguno
- Descripción: Devuelve la información detallada de un solo post según su ID.
- Código de respuesta: `200 OK`

3. POST - Crear un nuevo Post
- Método: `POST`
- Endpoint: `/posts`
- Cuerpo (Body):
  ```json
  {
    "title": "Mi primer post de prueba",
    "body": "Este es el contenido de mi post para la tarea de Postman.",
    "userId": 1
  }
  ```
- Descripción: Simula la creación de un nuevo recurso.
- Código de respuesta esperado: `201 Created`
- Observación: Devuelve el recurso creado con un nuevo `id`.

4. PUT - Actualizar un Post (Actualización completa)
- Método: `PUT`
- Endpoint: `/posts/1`
- Cuerpo (Body):
  ```json
  {
    "id": 1,
    "title": "Título ACTUALIZADO con PUT",
    "body": "Este contenido fue modificado completamente.",
    "userId": 1
  }
  ```
- Descripción: Reemplaza completamente los datos de un recurso existente.
- Código de respuesta: `200 OK`

5. DELETE - Eliminar un Post
- Método: `DELETE`
- Endpoint: `/posts/1`
- Cuerpo: Ninguno
- Descripción: Simula la eliminación de un recurso.
- Código de respuesta: `200 OK`

-----------------------------------------------------------------------------------------

3. Ejemplos de respuestas

Ejemplo de respuesta POST (201 Created):
```json
{
  "title": "Mi primer post de prueba",
  "body": "Este es el contenido de mi post para la tarea de Postman.",
  "userId": 1,
  "id": 101
}


Ejemplo de respuesta GET (/posts/1):
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit..."
}
```

-----------------------------------------------------------------------------------------

## 4. Qué aprendí del proceso

Durante esta práctica pude comprender de forma práctica los conceptos fundamentales de las APIs REST:

- La diferencia y el uso correcto de los métodos HTTP (GET, POST, PUT, DELETE).
- Cómo estructurar y enviar datos en formato JSON en el Body.
- La importancia de los códigos de estado HTTP y qué significan (200, 201, etc.).
- Cómo funciona una API de solo lectura (PokéAPI) comparada con una API que permite operaciones CRUD completas (JSONPlaceholder).
- El uso de Postman como herramienta profesional para probar y documentar APIs.
- La utilidad de las colecciones, environments y variables en Postman.
- Buenas prácticas para documentar solicitudes y respuestas.

Esta actividad me ha ayudado a implementar de primera mano lo explicado en clase y a visualizar el 
flujo de trabajo de las APIs y su importancia. 

