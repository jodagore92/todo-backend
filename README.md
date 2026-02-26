# 📝 ToDo Fullstack (FastAPI + Vue 3)

Proyecto **ToDo List** fullstack, con **backend en FastAPI** y **frontend en Vue 3 + Vite**, siguiendo buenas prácticas de **arquitectura limpia**, **Docker**, y **tests automatizados**.

Este proyecto fue creado con fines de aprendizaje profesional y para demostrar un flujo completo de desarrollo backend + frontend.

---

## 🚀 Tecnologías usadas

### Backend

* **Python 3.12**
* **FastAPI**
* **Pydantic v2**
* **Pytest**
* **Uvicorn**
* **Docker / Docker Compose**
* Arquitectura limpia (Models, Schemas, Repositories, Services)

### Frontend

* **Vue 3**
* **Vite**
* **JavaScript / TypeScript**
* **HTML5 / CSS3**
* **Docker**

---

## 📁 Estructura del proyecto

```text
todo-fullstack/
├── backend/
│   ├── app/
│   │   ├── api/v1/
│   │   │   ├── todos.py
│   │   │   └── auth.py
│   │   ├── models/
│   │   │   ├── todo.py
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   ├── todo.py
│   │   │   └── user.py
│   │   ├── services/
│   │   │   ├── todo_service.py
│   │   │   └── auth_service.py
│   │   ├── repositories/
│   │   │   ├── todo_repository.py
│   │   │   └── user_repository.py
│   │   └── main.py
│   ├── tests/
│   │   ├── conftest.py
│   │   └── test_todos_service.py
│   ├── docker/
│   │   └── Dockerfile
│   ├── requirements.txt
│   └── alembic.ini
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   │   ├── components/
│   │   │   └── TodoList.vue
│   │   ├── views/
│   │   │   └── Home.vue
│   │   └── main.js
│   ├── docker/
│   │   └── Dockerfile
│   └── .env.local
├── docker-compose.yml
└── README.md
```

---

## 🧠 Arquitectura

### Backend

* **Schemas**: DTOs de entrada/salida (Pydantic)
* **Models**: Entidades de dominio
* **Services**: Lógica de negocio, independientes de FastAPI
* **Repositories**: Acceso a datos (DB o in-memory)
* **Routers**: Capa HTTP (FastAPI)

### Frontend

* **Components**: Componentes reutilizables (Vue)
* **Views**: Páginas completas
* **Store / Composables**: Lógica compartida entre componentes
* **API Services**: Comunicación con backend

El frontend consume los endpoints del backend a través de Axios o Fetch, manteniendo separación de responsabilidades.

---

## 🐳 Levantar el proyecto con Docker Compose

```bash
docker-compose up --build
```

La aplicación quedará disponible en:

* Backend: [http://localhost:8001](http://localhost:8001)
* Frontend: [http://localhost:5173](http://localhost:5173)
* API docs (Swagger UI): [http://localhost:8001/docs](http://localhost:8001/docs)

> Internamente FastAPI corre en el puerto 8000 y Vite en 5173; Docker los expone según `docker-compose.yml`.

---

## 🧪 Ejecutar tests (Backend)

```bash
docker exec -it todo_backend pytest
```

* Tests unitarios de services
* Repositorio reseteado automáticamente con fixtures
* Sin dependencia de HTTP ni DB real

---

## 📌 Endpoints principales (Backend)

| Método | Endpoint              | Descripción       |
| ------ | --------------------- | ----------------- |
| GET    | /api/v1/todos         | Listar todos      |
| GET    | /api/v1/todos/{id}    | Obtener por ID    |
| POST   | /api/v1/todos         | Crear todo        |
| PUT    | /api/v1/todos/{id}    | Actualizar        |
| DELETE | /api/v1/todos/{id}    | Eliminar          |
| POST   | /api/v1/auth/login    | Login de usuario  |
| POST   | /api/v1/auth/register | Registrar usuario |

---

## ⚡ Funcionalidades Frontend

* Listado de todos los ítems
* Crear, actualizar y eliminar tareas
* Interacción con backend vía API
> Futuro: Login y registro de usuarios, UI responsiva y dinámica

---

## 🔮 Próximos pasos sugeridos

* Añadir JWT / autenticación completa
* Tests de integración backend + frontend
* Mejorar UI con librerías de componentes (Vuetify, Tailwind)
* Docker Compose multi-servicio listo para producción

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica profesional fullstack, integrando **FastAPI + Vue 3 + Docker**.

---

⭐ Si este proyecto te sirvió como referencia, ¡úsalo, mejóralo y experimenta!
