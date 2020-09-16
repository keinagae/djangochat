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

export default {
  name: "MessageWrapper",
  props: [
    'user'
  ],

  components: {MessageView, ContactList, CreateMessage},
  computed: {
    ...mapGetters('chat', {
      activeConversion: 'activeConversion'
    })
  },
  methods: {
    ...mapActions('chat', {
      fetchToken: 'fetchToken',
      setNotifySocket:"setNotifySocket"
    }),
  },
  mounted() {
    this.fetchToken().then(_=>{
      this.setNotifySocket()
    })

  }
}
</script>

<style lang="scss">

</style>
