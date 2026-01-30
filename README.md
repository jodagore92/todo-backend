# 📝 ToDo Backend (FastAPI)

Backend de una aplicación **ToDo List** construido con **FastAPI**, siguiendo principios de **arquitectura limpia**, con **Docker**, **tests automatizados** y separación clara de responsabilidades.

Este proyecto fue creado con fines de aprendizaje profesional y buenas prácticas backend.

---

## 🚀 Tecnologías usadas

- **Python 3.12**
- **FastAPI**
- **Pydantic v2**
- **Pytest**
- **Docker / Docker Compose**
- **Uvicorn**
- Arquitectura limpia (Services, Repositories, Models, Schemas)

---

## 📁 Estructura del proyecto

```text
todo-backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── todos.py
│   ├── models/
│   │   └── todo.py
│   ├── schemas/
│   │   └── todo.py
│   ├── services/
│   │   └── todo_service.py
│   ├── repositories/
│   │   └── todo_repository.py
│   └── main.py
├── tests/
│   ├── conftest.py
│   └── test_todos_service.py
├── docker/
│   └── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧠 Arquitectura

- **Schemas**: DTOs de entrada y salida (Pydantic)
- **Models**: Entidades de dominio (dataclasses)
- **Services**: Lógica de negocio
- **Repositories**: Acceso a datos (en memoria, por ahora)
- **Routers**: Capa HTTP (FastAPI)

Los services **no dependen de FastAPI ni de la base de datos**, lo que facilita testing y escalabilidad.

---

## 🐳 Levantar el proyecto con Docker

```bash
docker-compose up --build
```

La API quedará disponible en:

- http://localhost:8001
- http://localhost:8001/docs (Swagger UI)

> Internamente FastAPI corre en el puerto 8000, Docker lo expone en el 8001.

---

## 🧪 Ejecutar tests

```bash
docker exec -it todo_backend pytest
```

Características de los tests:
- Tests unitarios de services
- Repositorio reseteado automáticamente con fixtures
- Sin dependencia de HTTP ni DB

---

## 📌 Endpoints principales

| Método | Endpoint | Descripción |
|------|---------|------------|
| GET | /api/v1/todos | Listar todos |
| GET | /api/v1/todos/{id} | Obtener por ID |
| POST | /api/v1/todos | Crear todo |
| PUT | /api/v1/todos/{id} | Actualizar |
| DELETE | /api/v1/todos/{id} | Eliminar |

---

## 🔮 Próximos pasos sugeridos

- Tests de API con `TestClient`
- Base de datos real (SQLite + SQLAlchemy)
- Autenticación JWT
- Frontend en React
- Docker Compose fullstack

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica profesional de backend con Python y FastAPI.

---

⭐ Si este proyecto te sirvió como referencia, ¡úsalo, mejóralo y experimenta!
