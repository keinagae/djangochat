<template>
  <div class="home">
      <message-wrapper></message-wrapper>
  </div>
</template>

<script>

import MessageWrapper from "@/components/chat/MessageWrapper";
export default {
  name: 'Home',
  components: {MessageWrapper},
}
</script>
