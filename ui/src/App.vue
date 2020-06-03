<template>
  <div class="container">
    <SearchBar @termSubmit="onSubmit"></SearchBar>
    <div class="row">
      <CardListItem></CardListItem>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

import SearchBar from './components/SearchBar';
// import CardList from './components/CardList';
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
      isRemote: {},
      employmentTypes: {},
      locations: {},
      skills: {}
    }
  },
  methods: {
    onSubmit() {
      axios.get(mockAPI)
        .then(response => {
          console.log(response);
          // this.isRemote = response.isRemote;
        })
    }
  }
}
</script>

<style>

</style>
