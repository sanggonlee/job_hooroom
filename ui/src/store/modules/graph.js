import axios from 'axios';

const apiUrl = process.env.VUE_APP_API;

const state = {
    data: {}
}

const actions = {
    setAnalytics: async ({ commit }) => {
        const response = await axios.get(apiUrl);
        commit('SET_ANALYTICS_DATA', response.data);
    }
}

const getters = {
    graphData: state => {
        return state.data;
    }
}

const mutations = {
    SET_ANALYTICS_DATA: (state, data) => {
        state.data = data;
    }
}

export default {
    state,
    actions,
    getters,
    mutations
}