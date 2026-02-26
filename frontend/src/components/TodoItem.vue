<template>
  <li class="todo-item">
    <div class="todo-content" :class="{ completed: todo.completed }">
      <input type="checkbox" v-model="todo.completed" @change="emitUpdate" />
      <span class="title" >{{ todo.title }}</span>
      <span v-if="todo.description" class="description">&nbsp;{{ todo.description }}</span>
    </div>
    <button class="button button-icon" @click="emitDelete">🗑️</button>
  </li>
</template>

<script>
export default {
  props: {
    todo: { type: Object, required: true }
  },
  methods: {
    emitUpdate() {
      this.$emit('update', this.todo);
    },
    emitDelete() {
      this.$emit('delete', this.todo.id);
    }
  }
}
</script>

<style scoped>
.todo-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 12px;
  margin-bottom: 8px;
  background: #3a3a3a;
  border-radius: 4px;
}

.todo-content {
  display: flex;
  align-items: center;
}

.title {
  font-weight: bold;
  color: #f0f0f0;
  margin-left:.5em;
}

.description {
  color: #bbb;
}

.completed .title,
.completed .description {
  text-decoration: line-through;
  color: #888;
}

.button-icon {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 18px;
  color: #f44336;
  transition: transform 0.2s, color 0.2s;
}

.button-icon:hover {
  color: #d32f2f;
  transform: scale(1.2);
}
</style>