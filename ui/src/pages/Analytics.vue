<template>
  <div class="ui container">
    <SearchBar />
    <div v-if="this.graphData" class="flex-box">
      <GraphCard
        v-for="(value, index) in this.graphs"
        :key="index"
        :dataKey="value.key"
        :graphProp="value.buckets"
        :title="value.title"
      />
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import SearchBar from "../components/SearchBar";
import GraphCard from "../components/GraphCard";
import { POSTING_ATTRIBUTE_LABELS } from "../constants";
import { postingAttributes } from "../logic";

export default {
  name: "Analytics",
  components: {
    SearchBar,
    GraphCard,
  },
  computed: {
    ...mapGetters(["graphData"]),
    graphs: function () {
      return postingAttributes.map((attrib) => ({
        key: attrib,
        title: POSTING_ATTRIBUTE_LABELS[attrib],
        buckets: this.graphData[attrib]?.buckets,
      }));
    },
  },
  methods: {
    ...mapActions(["setAnalytics"]),
  },
  created() {
    this.setAnalytics();
  },
};
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
