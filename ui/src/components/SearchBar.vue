<template>
  <div class="search-bar-root">
    <div class="search-bar-main">
      <span class="search-bar-input">
        <input ref="textbox" v-on:focus="onSearchFocus" />
        <search-token-pill
          v-for="(value, index) in searchComponents"
          :key="index"
          :attrib="value.attrib"
          :term="value.term"
        />
      </span>
      <button class="btn btn-secondary" v-on:click="onInput">Search</button>
    </div>
    <div
      v-show="currentSearchState === SEARCH_STATE.selectAttrib"
      class="search-bar-attrib-selector"
    >
      <search-attrib-selector-row
        v-for="(value, index) in Object.values(POSTING_ATTRIBUTES)"
        :key="index"
        :attrib="value"
        v-on:attrib-selected="onSearchAttribSelected"
      />
    </div>
    <search-token-pill-editable
      v-if="!!currentSearchAttrib"
      :attrib="currentSearchAttrib"
      @on-complete="onSearchComponentEntered"
      @on-removed="onSearchComponentDeleted"
    />
  </div>
</template>

<script>
import { POSTING_ATTRIBUTES, POSTING_ATTRIBUTE_LABELS, SEARCH_STATE } from '../constants';
import SearchAttribSelectorRow from './SearchAttribSelectorRow';
import SearchTokenPill from './SearchTokenPill';
import SearchTokenPillEditable from './SearchTokenPillEditable';
export default {
  name: 'SearchBar',
  components: {
    SearchAttribSelectorRow,
    SearchTokenPillEditable,
    SearchTokenPill,
  },
  data() {
    return {
      SEARCH_STATE,
      POSTING_ATTRIBUTES,
      POSTING_ATTRIBUTE_LABELS,

      currentSearchState: SEARCH_STATE.unfocused,
      currentSearchAttrib: undefined,
      searchComponents: [],
    };
  },
  methods: {
    onInput: function() {
      this.$emit('term-submit', '');
    },
    onSearchFocus: function() {
      this.currentSearchState = SEARCH_STATE.selectAttrib;
    },
    onSearchAttribSelected: function(attrib) {
      this.currentSearchState = SEARCH_STATE.searchTerm;
      this.currentSearchAttrib = attrib;
    },
    onSearchComponentEntered: function(searchComponent) {
      this.searchComponents.push(searchComponent);

      this.currentSearchAttrib = undefined;
      this.focusInput();
    },
    onSearchComponentDeleted: function() {
      this.currentSearchAttrib = undefined;
    },
    focusInput() {
      this.$refs.textbox.focus();
    },
  },
};
</script>

<style scoped>
.search-bar-root {
  position: relative;
  margin: 20px 0;
}
.search-bar-main {
  display: flex;
}
.search-bar-input {
  flex: 1;
  border: solid 1px black;
  border-radius: 3px;
}
.search-bar-input > input {
  display: block;
  border: none;
  width: 100%;
  padding: 6px;
}
.search-bar-main > button {
  flex: 0 0 100px;
}
.search-bar-attrib-selector {
  position: absolute;
  width: 100%;
  text-align: left;
  z-index: 100;
  background-color: white;
  border: solid black 1px;
  border-radius: 3px;
}
</style>
