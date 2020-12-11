<template>
    <div>
        <button @click="click">
            like
        </button>
        <p>{{hearts.size()}}</p>
    </div>
</template>

<script>
    import axios from 'axios'

    const API_URL = 'http://localhost:4000'
    export default {

        name: 'Heart',
      
        data() {
            return {
                flag: true,
            }
        },
        methods: {
            click() {
                
            }
        }
    }
</script>

<style scoped>
</style>