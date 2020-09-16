export function fetchUsers({commit}) {
    return axios.get('api/users').then((response) => {
        commit('setUsers', response.data.data)
        return response.data.data;
    }).finally(() => {

    })
}

export function fetchOtherUsers({commit}) {
    return axios.get('api/users/other').then((response) => {
        commit('setOtherUsers', response.data.data)
        return response.data.data;
    }).finally(() => {

    })
}

export function fetchChats({commit}) {
    return axios.get('/api/users/chats').then((response) => {
        commit('setChats', response.data.data)
        return response.data.data;
    }).finally(() => {

    })
}

export function pushChat({commit}, chat) {
    commit('pushChat', chat)
}

export function selectChat({commit, state}, chat) {
    commit('setSelectedChat', chat)
}

export function fetchSelectedChatMessages({commit, state}) {
    return axios.get('/api/chats/'+ state.selectedChat.id + '/messages').then(response => {
        commit('setMessages', response.data.data)
        return response.data.data
    })
}
