<template>
  <span class="search-token-pill">{{POSTING_ATTRIBUTE_LABELS[attrib]}}:{{term}}</span>
</template>

<script>
import { POSTING_ATTRIBUTE_LABELS } from "../constants";

export default {
  name: "SearchTokenPill",
  props: ["attrib", "term"],
  data() {
    return {
      POSTING_ATTRIBUTE_LABELS,
    };
  },
};
</script>

<style scoped>
.search-token-pill {
  display: inline-block;
  padding: 6px;
  margin: 4px;
  border-radius: 3px;
  background-color: lightsteelblue;
}
</style>
