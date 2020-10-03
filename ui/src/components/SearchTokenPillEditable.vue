<template>
  <span class="search-token-pill-editable">
    <span>{{ POSTING_ATTRIBUTE_LABELS[attrib] }}:</span>
    <input
      ref="term"
      class="search-token-pill-editable-term"
      v-model="term"
      @keyup.enter="$emit('on-complete', { attrib, term })"
      @keyup.delete="$emit('on-removed', attrib)"
    />
  </span>
</template>

<script>
import { POSTING_ATTRIBUTE_LABELS } from '../constants';

export default {
  name: 'SearchTokenPillEditable',
  props: ['attrib'],
  data() {
    return {
      POSTING_ATTRIBUTE_LABELS,

      term: '',
    };
  },
  mounted() {
    this.$nextTick(this.focusInput);
  },
  methods: {
    focusInput() {
      this.$refs.term.focus();
    },
  },
  watch: {
    attrib: function() {
      this.focusInput();
    },
  },
};
</script>

<style scoped>
.search-token-pill-editable {
  display: inline-block;
  padding: 6px;
  margin: 4px 0;
  border-radius: 3px;
  border: solid 2px black;
}

.search-token-pill-editable-term {
  border: none;
  background-color: transparent;
}
</style>
