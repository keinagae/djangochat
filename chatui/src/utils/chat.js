import WebSocketService from "@/utils/websockets";
import {me} from "@/store/modules/auth/actions";

class Conversion {
    constructor(id, name, participants, user, is_group) {
        this.id = id
        this.name = name
        this.participants = participants;
        this.user = user
        this.is_group = is_group
        this.messages = []
        this.draft=""
        this.socket=null
    }
    setSocket(token){
        let url=`ws://127.0.0.1:8000/ws/chat/${this.user.id}/?key=${token}`
        this.socket =new WebSocketService()
        this.socket.connect(url,(message)=>this.onMessage(message))
    }
    onMessage(response){
         console.log(response)
        if(response.action==='message'){
            this.messages.push(response.data)
        }


    }
    sendMessage(){
        this.socket.sendMessage({action:"message",message:this.draft})
        this.draft=""
    }
    typing(){
        this.socket.sendMessage({action:"start_typing"})
    }
    stopTyping(){
        this.socket.sendMessage({action:"stop_typing"})
    }
    fetchMessages() {
        if (this.messages.length == 0) {
            return axios.get('chat/messages/' + this.id).then((response) => {
                this.messages = [ ...response.data];
            }).finally(() => {

            })
        }

    }

}

export default Conversion