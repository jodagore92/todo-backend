// todos.js
const API_BASE = import.meta.env.VITE_APP_API_BASE_URL;

export async function fetchTodos() {
  const res = await fetch(`${API_BASE}/todos/`);
  return await res.json();
}

export async function createTodoApi(todo) {
  const res = await fetch(`${API_BASE}/todos/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(todo)
  });
  return await res.json();
}

export async function updateTodoApi(todo) {
  await fetch(`${API_BASE}/todos/${todo.id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(todo)
  });
}

export async function deleteTodoApi(id) {
  await fetch(`${API_BASE}/todos/${id}`, { method: 'DELETE' });
}