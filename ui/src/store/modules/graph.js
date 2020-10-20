import axios from 'axios';

const apiUrl = process.env.VUE_APP_API;

const state = {
    data: {},
    searchParams: {},
}

const actions = {
    getAnalytics: async ({ commit, state }) => {
        let url = `${apiUrl}/analytics?`;
        const { searchParams = {} } = state;
        console.log('search params = ', searchParams);
        for (const attrib of Object.keys(searchParams)) {
            url += `${attrib}=${searchParams[attrib].join(',')}`
        }
        const response = await axios.get(url);
        commit('GET_ANALYTICS_DATA', response.data);
    },
    setSearchAttrib: async ({ commit }, searchComponent) => {
        console.log('search param added:', searchComponent);
        commit('ADD_SEARCH_PARAM', searchComponent);
    }
}

const getters = {
    graphData: state => {
        return state.data;
    }
}

const mutations = {
    GET_ANALYTICS_DATA: (state, data) => {
        state.data = data;
    },
    ADD_SEARCH_PARAM: (state, { attrib, term } = {}) => {
        if (!state.searchParams[attrib]) {
            state.searchParams[attrib] = [];
        }
        state.searchParams[attrib].push(term);
    }
}

export default {
    state,
    actions,
    getters,
    mutations
}