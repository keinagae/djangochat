import WebSocketService from "@/utils/websockets";

export default {
    activeConversion:null,
    chat_token:"",
    availableContacts:[],
    chatSocket:new WebSocketService(),
    notifySocket:new WebSocketService(),
    conversions:[],
    messages:[]
}
