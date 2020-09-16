<template>
    <div class="message">
        <div class="spacer"></div>
        <div class="message-body" :class="message.user.id===user.id?'sent':'received'" >
            <div class="user-info">
                <img class="user-img" :src="senderAvatar" alt=""/>
                <span class="filler"></span>
                <span class="chat-item-username">{{ message.user.username }}</span>
            </div>
            <div class="message-content">{{ message.message }}</div>
        </div>
    </div>
    <!--    <li class="replies">-->
    <!--        <img src="http://emilcarlsson.se/assets/harveyspecter.png" alt=""/>-->
    <!--        <p>When you're backed against the wall, break the god damn thing down.</p>-->
    <!--    </li>-->
</template>

<script>
    import {mapGetters} from 'vuex'

    export default {
        name: "MessageItem",
        props: {
            message: {
                type: Object,
                required: true
            }
        },
        data:() => ({

        }),
        computed: {
            senderAvatar() {
                return 'https://picsum.photos/200/300'
            },
            sender() {
                return this.message.sender
            },
            ...mapGetters('auth', {
                user: 'authUser'
            }),
        },
    }
</script>

<style scoped>

</style>
