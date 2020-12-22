<template>
  <div ref="messages" class="chat-box-chat-messages">
    <message-item
        v-for="message in conversion.messages"
        :key="conversion.id+'chat'+message.id"
        :message="message"
    ></message-item>
  </div>
</template>

<script>
import MessageItem from "./MessageItem";
import {mapGetters} from 'vuex'

export default {
  name: "MessageList",
  components: {MessageItem},
  props: {},
  data() {
    return {
      shouldScroll: false
    }
  },
  computed: {
    ...mapGetters('chat', {
      messages: 'messages',conversion: 'activeConversion'
    })
  },
  beforeUpdate() {
    // console.log(this.$refs.messages.scrollTop)
    // console.log((this.$refs.messages.scrollHeight - this.$refs.messages.offsetHeight))
    // console.log(this.$refs.messages.scrollTop === (this.$refs.messages.scrollHeight - this.$refs.messages.offsetHeight))
    this.shouldScroll = Math.abs(this.$refs.messages.scrollTop - (this.$refs.messages.scrollHeight - this.$refs.messages.offsetHeight))<100
  },
  updated() {
    if (this.shouldScroll) {
      document.querySelector('.chat-box-chat-messages .message:last-child').scrollIntoView({
      behavior: "smooth",
      block: "end",
      inline: "end"
    });
    }
  },
  mounted() {
  }
}
</script>

<style scoped lang="scss">
.chat-box-chat-messages {
  --scroll-bar-color-dark: rgba(234, 231, 227, 0.9);
  --scroll-bar-color-light: rgba(27, 27, 27, 0.9);
}

.chat-box-chat-messages ::-webkit-scrollbar {
  height: 8px;
  width: 14px;
}

.chat-box-chat-messages ::-webkit-scrollbar-corner {
  background: transparent;
}

.chat-box-chat-messages ::-webkit-scrollbar-thumb {
  background: rgba(27, 27, 27, 0.9);
  border-radius: 14px;
}
</style>
