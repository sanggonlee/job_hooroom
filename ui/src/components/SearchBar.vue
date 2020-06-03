<template>
    <div>
        <input v-model="searchTerm" />
        <button class="btn btn-secondary" v-on:click="onInput">Search</button>
    </div>
</template>

<script>

export default {
    name: 'SearchBar',
    data() {
        return {
            searchTerm: this.searchTerm
        }
    },
    methods: {
        onInput: function() {
            this.$emit('termSubmit', this.searchTerm);
            //console.log(this.searchTerm);
        }
    }
}
</script>

<style scoped>
    input {
        width: 75%;
    }
    div {
        text-align: center;
        margin: 20px;
    }
</style>