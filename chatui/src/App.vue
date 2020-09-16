<template>
  <div>
    <router-view/>
  </div>
</template>
<script>

export default {
  name: "App",
  mounted() {
    console.log(this.$store.getters['auth/isLoggedIn'])
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
