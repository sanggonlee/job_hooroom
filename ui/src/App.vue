<template>
  <div class="ui container">
    <h2 class="ui center aligned header">Job Hooroom</h2>
      <SearchBar />
      <div class="flex-box">
        <GraphCard :locations="locations"></GraphCard>
        <GraphCard :employmentTypes="employmentTypes"></GraphCard>
        <GraphCard :skills="skills"></GraphCard>
        <GraphCard :isRemote="isRemote"></GraphCard>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

import SearchBar from './components/SearchBar';
import GraphCard from './components/GraphCard';

const mockAPI = process.env.VUE_APP_MOCK_API;

export default {
  name: 'App',
  components: {
    SearchBar,
    GraphCard
  },
  data() {
    return {
      isRemote: [],
      employmentTypes: [],
      locations: [],
      skills: []
    }
  },
  mounted() {
    axios.get(mockAPI)
        .then(response => {
          this.isRemote = response.data.is_remote.buckets;
          this.employmentTypes = response.data.employment_type.buckets;
          this.locations = response.data.location.buckets;
          this.skills = response.data.skills.buckets;
        })
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