import ReconnectingWebSocket from "reconnecting-websocket";
class WebSocketService {
    static instance = null
    callbacks = {}

    static getInstance() {
        if (!WebSocketService.instance) {
            WebSocketService.instance = new WebSocketService();
        }
        return WebSocketService.instance;
    }

    constructor() {
        this.socketRef = null
    }

    connect(url,onMessage) {
        this.callbacks={
            onMessage: onMessage
        }
        this.socketRef = new ReconnectingWebSocket(url)
        this.socketRef.onopen = (e) => {
            console.log(e)
            console.log("socket open at" ,url)
        }
        this.socketRef.onmessage = e => {
            this.receiveMessage(e.data)
        }
        this.socketRef.onerror = e => {
            console.log(e.message);
        };
        this.socketRef.onclose = () => {
            console.log("WebSocket closed let's reopen");
            // this.connect();
        };
    }

    disconnect() {
        if(this.socketRef){
            this.socketRef.close()
        }

    }

    receiveMessage(data,dispatch) {
        const parsedData = JSON.parse(data)
        // dispatch("receiveMessage",parsedData)
        this.callbacks.onMessage(parsedData)
        return parsedData
    }

    sendMessage(data) {
        console.log(data)
        console.log("sent")
        try {
            this.socketRef.send(JSON.stringify({...data}))
        } catch (err) {
            console.log(err)
        }
    }
}

const WebSocketInstance = WebSocketService;

export default WebSocketInstance;