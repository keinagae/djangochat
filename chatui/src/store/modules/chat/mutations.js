export function setConversions (state, data) {
    state.conversions = data
}
export function setNewConversion (state, data) {
    state.conversions=[data,...state.conversions]
}

export function setMessages (state, data) {
    state.messages = data
}

export function setToken (state, data) {
    state.chat_token = data
}

export function setActiveConversion (state, data) {
    state.activeConversion = data
}
export function receiveMessage (state, data) {
    state.messages.push(data)
}

export function setAvailableContacts (state, data) {
    state.availableContacts = data
}


