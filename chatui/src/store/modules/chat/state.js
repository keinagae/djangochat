import WebSocketService from "@/utils/websockets";

export default {
    activeConversion:null,
    chat_token:"",
    availableContacts:[],
    notifySocket:new WebSocketService(),
    conversions:[],
}
