<template>
  <div class="container">
    <h1>Mis Tareas</h1>

    <form @submit.prevent="handleCreate">
      <input v-model="newTitle" placeholder="Título" required />
      <input v-model="newDescription" placeholder="Descripción" />
      <button class="button button-primary" type="submit">Agregar</button>
    </form>

    <TodoList
      :todos="todos"
      @update="handleUpdate"
      @delete="handleDelete"
    />
  </div>
</template>

<script>
import { fetchTodos, createTodoApi, updateTodoApi, deleteTodoApi } from './todos.js';
import TodoList from './components/TodoList.vue';

export default {
  components: { TodoList },
  data() {
    return {
      todos: [],
      newTitle: '',
      newDescription: ''
    };
  },
  methods: {
    async loadTodos() {
      this.todos = await fetchTodos();
    },
    async handleCreate() {
      const todo = await createTodoApi({
        title: this.newTitle,
        description: this.newDescription || '',
        completed: false
      });
      this.todos.unshift(todo); // nuevo al inicio
      this.newTitle = '';
      this.newDescription = '';
    },
    async handleUpdate(todo) {
      await updateTodoApi(todo);
    },
    async handleDelete(id) {
      await deleteTodoApi(id);
      this.todos = this.todos.filter(t => t.id !== id);
    }
  },
  mounted() {
    this.loadTodos();
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

body {
  background: #1e1e1e;
  color: #f0f0f0;
  font-family: 'Poppins', sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

.container {
  width: 500px;
  height: 80vh;
  padding: 20px;
  background: #2c2c2c;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.5);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

h1 {
  text-align: center;
  margin: 0;
}

form {
  display: flex;
  gap: 10px;
}

form input {
  flex: 1;
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #444;
  background: #1e1e1e;
  color: #f0f0f0;
}

/* Botones */
.button {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  color: white;
  cursor: pointer;
  background-color: gray;
  transition: background 0.2s;
}

.button-primary {
  background-color: #4caf50;
}

.button-primary:hover {
  background-color: #45a049;
}
</style>