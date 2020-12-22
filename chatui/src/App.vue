<template>
  <div>
    <router-view/>
  </div>
</template>
<script>
import Wazo from '@wazo/sdk/lib/simple';
export default {
  name: "App",
  methods:{
    async login(){
      let response= await Wazo.Auth.logIn("kei@kei.com","kei123")
      console.log(response)
      await Wazo.Room.connect({extension:12345,audio:true})
    }
  },
  mounted() {
    // console.log(this.$store.getters['auth/isLoggedIn'])
  },
  created() {

    this.$store.dispatch('auth/me').then((response) => {
      this.$router.replace(
          {name: "Home"}
      )
    }).catch((error) => {
      localStorage.removeItem('auth_token')
      delete axios.defaults.headers.common.Authorization
      this.$router.replace(
          {name: "Login"}
      )
    })
  }
}
</script>
<style lang="scss">
@import "assets/scss/main";
</style>
