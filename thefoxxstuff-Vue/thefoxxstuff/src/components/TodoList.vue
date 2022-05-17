<template>
    <div>
        <ul>
            <TodoItem
            v-for="(todo, index) in todos" :key="index"
            v-bind:todo="todo"
            />
            <Furry
            v-for="(fur, indexx) in furry" :key="indexx"
            v-bind:fur="fur"
            />
        </ul>
        
    </div>
</template>

<script>
import TodoItem from '@/components/TodoItem'
import Furry from '@/components/Furry'
export default {
    props: ['todos', 'furry'],
    components: {
        TodoItem,
        Furry,
    }
}
</script>

<style scoped>
ul {
    list-style: 0;
    margin: 0;
    padding: 0;
}
</style>