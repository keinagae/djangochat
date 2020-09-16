import WebSocketInstance from "@/utils/websockets";

export function fetchConversions({commit}) {
    return axios.get('chat/').then((response) => {
        commit('setConversions', response.data)
        return response.data;
    }).finally(() => {

    })
}
export function fetchMessages({commit},conversion) {
    return axios.get('chat/messages/'+conversion).then((response) => {
        commit('setMessages', response.data)
        return response.data;
    }).finally(() => {

    })
}
export function fetchToken({commit}) {
    return axios.post('chat/token').then((response) => {
        commit('setToken', response.data.key)
        return response.data;
    }).finally(() => {

    })
}

export function setConversionSocket({commit,state,dispatch}) {
    let url=`ws://127.0.0.1:8000/ws/chat/${state.activeConversion.user.id}/?key=${state.chat_token}`
    state.chatSocket.disconnect()
    state.chatSocket.connect(url,dispatch)
}

export function setNotifySocket({commit,state,dispatch}) {
    let url=`ws://127.0.0.1:8000/ws/chat/notify?key=${state.chat_token}`
    state.notifySocket.disconnect()
    state.notifySocket.connect(url,dispatch)
}


export function receiveMessage({commit},message){
    commit('receiveMessage',message)
}

export function changeActiveConversions({commit},payload) {
    commit('setActiveConversion', payload)
}


export function fetchAvailableContacts({commit}) {
    return axios.get('chat/contacts/').then((response) => {
        commit('setAvailableContacts', response.data)
        return response.data;
    }).finally(() => {

    })
}

export function setNewContact({commit,state,dispatch},user) {
    return axios.post('chat/',{participants_id:[user.id]}).then((response) => {
        console.log(response)
        commit('setNewConversion',response.data)
        commit('setActiveConversion', response.data)
        return response.data;
    }).finally(() => {

    })
}