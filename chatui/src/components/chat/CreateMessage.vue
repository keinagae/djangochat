<template>
  <div >
<!--    <div v-if="typingData">-->
<!--      <span v-text="typingData.name + ' is typing...'"></span>-->
<!--    </div>-->
    <div class="chat-box-chat-footer">
      <!--            <div class="input" data-ph="Write your message" contenteditable="true">-->
      <!--            </div>-->
      <textarea @blur="endTyping" @focus="typing"  rows="1" v-model="activeConversion.draft" @keypress.enter="send"
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
      console.log("sending")
      if(this.activeConversion.draft!==""){
        this.activeConversion.sendMessage()
        // this.$store.getters['chat/chatSocket'].sendMessage({message:this.activeConversion.draft})
        // this.activeConversion.draft=""
      }
    },
    typing(){
      this.activeConversion.typing()
    },
    endTyping(){
      console.log("stopping")
      this.activeConversion.stopTyping()
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
