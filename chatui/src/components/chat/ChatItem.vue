<template>
  <div class="contact" @click="chatSelected(conversion)">
    <span class="contact-status online"></span>
    <img src="https://picsum.photos/200/300" alt=""/>
    <div class="meta">
      <span v-if="conversion.is_group" class="name">{{ conversion.name }}</span>
      <span v-else class="name">{{ conversion.user.username }}</span>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: "ContactItem",
  props: {
    conversion: {
      type: Object,
      required: true
    },
  },
  data() {
    return {

    }
  },
  methods: {
    chatSelected(conversion) {
      this.changeActiveConversions(conversion).then(_ => {
        this.setConversionSocket()
      })
      this.fetchMessage(conversion.id)
    },
    ...mapActions('chat', {
      changeActiveConversions: 'changeActiveConversions',
      setConversionSocket: 'setConversionSocket',
      fetchMessage:"fetchMessages"
    })
  }
}
</script>

<style scoped>

</style>
