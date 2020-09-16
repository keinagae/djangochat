<template>
  <div >
<!--    <div v-if="typingData">-->
<!--      <span v-text="typingData.name + ' is typing...'"></span>-->
<!--    </div>-->
    <div class="chat-box-chat-footer">
      <!--            <div class="input" data-ph="Write your message" contenteditable="true">-->
      <!--            </div>-->
      <textarea rows="1" v-model="message" @keypress.enter="send"
                placeholder="Write your message...">
            </textarea>
      <button class="submit" @click="send"><i class="far fa-paper-plane" aria-hidden="true"></i></button>
    </div>
  </div>
</template>

<script>
import Form from '../../utils/form'
import {mapActions, mapGetters, mapMutations} from 'vuex'

export default {
  name: "CreateMessage",
  props: {
    recipient: {
      type: Object,
      required: false
    }
  },
  data: () => ({
    form: new Form({
      content: null,
      recipient_id: null,
      sender_id: null,
    }),
    message:"",
    typingData: null,
    typingTimer: null
  }),
  computed: {
    ...mapGetters('auth', {
      authUser: 'authUser',
    }),
    ...mapGetters('chat', {
      activeConversion: 'activeConversion'
    })
  },
  mounted() {
  },
  methods: {
    send() {
      if(this.message!==""){
        this.$store.getters['chat/chatSocket'].sendMessage({message:this.message})
        this.message=""
      }

    },
    subscribePusherPrivateChannel() {
      return this.channel
          .listen('MessageSent', e => {
            this.pushMessage(e.message)
            this.typingData = false
            this.scrollPageToLast()
          })
          .listenForWhisper('typing', this.whisperTypingUser)
    },
    whisperTypingUser(data) {
      this.typingData = data

      if (this.typingData) clearTimeout(this.typingTimer)

      this.typingTimer = setTimeout(() => {
        this.typingData = false
      }, 3000)
    },
    userStartedTyping() {
      this.channel
          .whisper('typing', {
            name: this.authUser.name
          })
    },
    scrollPageToLast() {
      console.log(document.querySelector('.chat-box-chat-messages').scrollHeight)
      console.log(document.querySelector('.chat-box-chat-messages .message:last-child'))
      document.querySelector('.chat-box-chat-messages .message:last-child').scrollIntoView({
        behavior: "smooth",
        block: "end",
        inline: "end"
      });
    },
  }
}
</script>

<style scoped>

</style>
