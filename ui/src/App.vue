<template>
  <div class="ui container">
    <h2 class="ui center aligned header">Job Hooroom</h2>
    <!-- <SearchBar @termSubmit="onSubmit"></SearchBar> -->
      <SearchBar></SearchBar>
      <CardListItem :locations="locations"></CardListItem>
      <CardListItem :employmentTypes="employmentTypes"></CardListItem>
      <CardListItem :skills="skills"></CardListItem>
      <CardListItem :isRemote="isRemote"></CardListItem>

  </div>
</template>

<script>
import axios from 'axios';

import SearchBar from './components/SearchBar';
import CardListItem from './components/CardListItem';

const mockAPI = "https://5eb817ae5652960016785cf7.mockapi.io/api/v1/analytics" // analytics, postings

export default {
  name: 'App',
  components: {
    SearchBar,
    CardListItem
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
  },
  methods: {
    // onSubmit() {
    //   axios.get(mockAPI)
    //     .then(response => {
    //       console.log(response.data);
    //       this.isRemote = response.data.is_remote.buckets;
    //       this.employmentTypes = response.data.employment_type;
    //       this.locations = response.data.location.buckets;
    //       this.skills = response.data.skills;
    //       console.log(this.locations.buckets);
    //     })
    // }
  }
}
</script>

<style scoped>
  .header {
    margin: 20px !important;
  }
</style>>