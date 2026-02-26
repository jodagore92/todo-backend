<template>
  <ul>
    <template v-if="todos.length > 0">
      <TodoItem
        v-for="todo in todos"
        :key="todo.id"
        :todo="todo"
        @update="$emit('update', $event)"
        @delete="$emit('delete', $event)"
      />
    </template>

    <template v-else>
      <li class="todo-empty">
        <div class="empty-content">
          <span>¡Momento de organizar tu día!</span>
          <small>Cuando agregues tus tareas aquí, todo empezará a brillar.</small>
        </div>
      </li>
    </template>
  </ul>
</template>

<script>
import TodoItem from './TodoItem.vue';

export default {
  props: {
    todos: { type: Array, required: true }
  },
  components: { TodoItem }
}
</script>

<style scoped>
ul {
  flex: 1;
  overflow-y: auto;
  padding: 0;
  margin: 0;
  list-style: none;
  border-top: 1px solid #444;
}

.todo-empty {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 60px;
  text-align: center;
  color: #666;
  background: #333;
  border-radius: 4px;
}

.empty-content span {
  display: block;
  font-size: 24px;
  margin-bottom: 8px;
}

.empty-content small {
  display: block;
  font-size: 18px;
  color: #555;
}

/* Scroll elegante */
ul::-webkit-scrollbar {
  width: 6px;
}

ul::-webkit-scrollbar-thumb {
  background-color: #555;
  border-radius: 3px;
}

ul::-webkit-scrollbar-track {
  background-color: #2c2c2c;
}
</style>