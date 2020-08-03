<template>
  <div class="ui container">
    <h2 class="ui center aligned header">Job Hooroom</h2>
      <SearchBar />
      <div v-if="this.graphData" class="flex-box">
        <GraphCard v-for="(value, index) in this.graphData" :key="index" :graphProp="value.buckets" :title="index" />
      </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import SearchBar from './components/SearchBar';
import GraphCard from './components/GraphCard';

export default {
  name: 'App',
  components: {
    SearchBar,
    GraphCard
  },
  computed: {
    ...mapGetters([
      'graphData'
    ])
  },
  beforeCreate() {
    this.$store.dispatch('setAnalytics');
  }
}
</script>

<style scoped>
  .ui.header:first-child {
    margin-top: 10px;
  }
  .flex-box {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
    align-content: space-around;
  }
</style>>