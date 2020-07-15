import axios from 'axios';

const mockAPI = process.env.VUE_APP_MOCK_API;

const state = {
    data: []
}

const actions = {
    setAnalytics: ({ commit }) => {
        axios.get(mockAPI)
        .then(response => {
            commit('SET_ANALYTICS_DATA', response.data);
        })
    }
}

const getters = {
    getGraphData: function(state) {
        return state;
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