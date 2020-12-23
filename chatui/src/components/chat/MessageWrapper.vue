<template>
  <div class="chat-box">
    <contact-list></contact-list>
    <message-view v-if="this.activeConversion"></message-view>
  </div>
</template>

<script>
import ContactList from "./ContactList";
import CreateMessage from "./CreateMessage";
import MessageView from "./MessageView";
import {mapActions, mapGetters, mapMutations} from 'vuex'
import WebSocketService from "@/utils/websockets";

export default {
  name: "MessageWrapper",
  props: [
    'user'
  ],
  data(){
    return {
      notify: null
    }

  },
  components: {MessageView, ContactList, CreateMessage},
  computed: {
    ...mapGetters('chat', {
      activeConversion: 'activeConversion',
      token:"chatToken"
    })
  },
  methods: {
    ...mapActions('chat', {
      fetchToken: 'fetchToken',
      setNotifySocket:"setNotifySocket"
    }),
    onNotify(message){
      console.log(message)
    }
  },
  mounted() {
    this.fetchToken().then(_=>{
      // this.setNotifySocket()
      // this.notify=new WebSocketService()
      // let url=`ws://127.0.0.1:8000/ws/chat/notify?key=${this.token}`
      // this.notify.connect(url,(message)=>this.onNotify(message))
    })

  }
}
</script>

<style lang="scss">

</style>
