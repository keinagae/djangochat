<template>
    <div class="contact" @click="contactSelected" :class="selected?'active':''" >
        <span class="contact-status online"></span>
        <img  src="https://picsum.photos/200/300" alt=""/>
        <div class="meta">
            <span class="name">{{ user.username }}</span>
<!--                            <span class="preview">You just got LITT up, Mike.</span>-->
        </div>
    </div>
</template>

<script>
    export default {
        name: "NewChatContactItem",
        props: {
            user: {
                type: Object,
                required: true
            },
            selected: {
                type: Boolean,
                default: false
            }
        },
      methods:{
          contactSelected(){
            this.$emit("contactSelected",this.user)
          }
      }
    }
</script>

<style scoped>

</style>
