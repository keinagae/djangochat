export function setUsers (state, data) {
    state.users = data
}

export function setOtherUsers (state, data) {
    state.otherUsers = data
}

export function setChats (state, data) {
    state.chats = data
}

export function pushChat (state, chat) {
    state.chats.unshift(chat)
}

export function setAuthUser (state, user) {
    state.authUser = user
}

export function setSelectedChat(state, chat) {
    state.selectedChat = chat
}

export function setMessages(state, messages) {
    state.messages = messages
}

export function pushMessage(state, message) {
    state.messages.push(message)
}
