<template>
  <div class="contact" @click="chatSelected(conversion)">
    <span :class="getStatusClass" class="contact-status"></span>
    <img src="https://picsum.photos/200/300" alt=""/>
    <div class="meta">
      <span v-if="conversion.is_group" class="name">{{ conversion.name }}</span>
      <span v-else class="name">{{ conversion.user.username }}</span>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name: "ContactItem",
  props: {
    conversion: {
      type: Object,
      required: true
    },
  },
  computed: {
    ...mapGetters('chat', {
      token:"chatToken"
    }),
    getStatusClass(){
      if( this.conversion.user.status==='online'){
        return 'online'
      }else{
        return 'offline'
      }
    }
  },
  data() {
    return {}
  },
  methods: {
    chatSelected(conversion) {
      this.changeActiveConversions(conversion).then(_ => {
        conversion.setSocket(this.token)
        conversion.fetchMessages()
      })

      // this.fetchMessage(conversion.id)
    },
    ...mapActions('chat', {
      changeActiveConversions: 'changeActiveConversions',
      setConversionSocket: 'setConversionSocket',
      fetchMessage: "fetchMessages"
    })
  }
}
</script>

<style scoped>

</style>
