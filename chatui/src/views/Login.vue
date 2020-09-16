<template>
  <div class="vue-tempalte">
      <h3>Sign In</h3>

      <div class="form-group">
        <label>Email address</label>
        <input v-model="username"  class="form-control form-control-lg"/>
      </div>

      <div class="form-group">
        <label>Password</label>
        <input v-model="password" type="password" class="form-control form-control-lg"/>
      </div>

      <button type="btn" @click="login" class="btn btn-dark btn-lg btn-block">Sign In</button>

  </div>
</template>

<script>
export default {
  name: "Login",
  data(){
    return{
      username:"",
      password:""

    }
  },
  methods: {
    login(){
      let data = {
        username: this.username,
        password: this.password
      }
      axios.post('/auth/token/login',data).then(response => {
        localStorage.setItem('auth_token', response.data.auth_token)
        axios.defaults.headers.common['Authorization'] = "Token " +response.data.auth_token
        this.$store.dispatch('auth/me').then(
            response => {
              this.$router.replace(
                { name:"Home" }
              )
            }
        )
      })
    }
  }

}
</script>

<style scoped>

</style>