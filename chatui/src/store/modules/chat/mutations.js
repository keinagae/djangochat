import Conversion from "@/utils/chat";
export function setConversions (state, data) {
    state.conversions=data.map(conversion=>{
        return new Conversion(conversion.id,conversion.name,conversion.participants,conversion.user,conversion.is_group)
    })
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
    if (state.activeConversion&&state.activeConversion.socket){
        state.activeConversion.socket.disconnect()
    }
    state.activeConversion = data
}
export function receiveMessage (state, data) {
    state.messages.push(data)
}

export function setAvailableContacts (state, data) {
    state.availableContacts = data
}


