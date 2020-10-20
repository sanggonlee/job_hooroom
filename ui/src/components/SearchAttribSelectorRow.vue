<template>
  <div
    class="search-attrib-selector-row"
    @click.stop="$emit('attrib-selected', attrib)"
  >{{POSTING_ATTRIBUTE_LABELS[this.attrib]}}</div>
</template>

<script>
import { POSTING_ATTRIBUTE_LABELS } from "../constants";

export default {
  name: "SearchAttribSelectorRow",
  props: ["attrib"],
  data() {
    return {
      POSTING_ATTRIBUTE_LABELS,
    };
  },
  methods: {
    onSelect: function () {},
  },
};
</script>

<style scoped>
.search-attrib-selector-row {
  padding: 10px;
}

.search-attrib-selector-row:hover {
  background-color: aliceblue;
}
</style>
