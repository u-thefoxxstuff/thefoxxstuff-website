<template>
  <div id="app">
    <h1>To do</h1>
    <hr>
    <TodoList 
    v-bind:todos="todos"
    v-bind:furry="furry"
    />
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
export default {
  name: 'App',
  data() {
    return {
      todos: [ 
        {id: 1, title: 'куптть хлеб', complete: false},
        {id: 2, title: 'куптть хлеб', complete: false},
        {id: 3, title: 'куптть хлеб', complete: false},
        {id: 4, title: 'куптть хлеб', complete: false},
        ],
      furry: [ 
        {id: 1, title: 'Shark', complete: false},
        {id: 2, title: 'Fox', complete: false},
        ]
    }
  },
  components: {
    TodoList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
