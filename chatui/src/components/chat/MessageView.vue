<template>
  <div class="chat-box-chat">
    <div class="chat-box-chat-header">
      <img class="profile-img" src="https://picsum.photos/200/300" alt=""/>
      <div class="name">{{ conversionName }}</div>
    </div>
    <message-list></message-list>

    <!--        <typing></typing>-->
    <create-message :recipient="conversion.user"></create-message>
  </div>
</template>

<script>
import MessageItem from "./MessageItem";
import MessageList from "./MessageList";

import {mapGetters} from 'vuex'
import CreateMessage from "./CreateMessage";
import WebSocketInstance from "@/utils/websockets";
// import Typing from "./Typing";

export default {
  name: "MessageView",
  props: {},
  components: {CreateMessage, MessageList, MessageItem},
  data: () => ({
    roomImage: '/img/chat-public.png',
    chatRoomName: 'Public Chat',
    chatSocket: WebSocketInstance
  }),
  computed: {
    headingUser() {
      if (!this.selectedChat) {
        return null
      }

      if (this.selectedChat.sender.data.id === this.authUser.id) {
        return this.selectedChat.recipient.data;
      } else {
        return this.selectedChat.sender.data;
      }
    },
    avatar() {
      if (!this.headingUser) {
        return null
      }

      return this.headingUser.avatar
    },
    conversionName() {
      if (!this.conversion) {
        return null
      }
      if (this.conversion.is_group) {
        return this.conversion.name
      }

      return this.conversion.user.username
    },
    ...mapGetters('chat', {
      conversion: 'activeConversion'
    })
  },
  updated() {
    // document.querySelector('.chat-box-chat-messages .message:last-child').scrollIntoView({
    //   behavior: "smooth",
    //   block: "end",
    //   inline: "end"
    // });

  },
  methods: {

    subscribePusherPublicChannel() {
      window.Echo.channel('public')
          .listen('MessageSent', e => {
            this.messages.push(e.message)
            // this.scrollPageToLast()
          })
    }
  }
}
</script>

<style scoped>

</style>
