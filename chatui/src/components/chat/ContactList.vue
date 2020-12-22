<template>
    <div class="chat-box-sidepanel">
        <div class="chat-box-sidepanel-header">
            <div class="wrapper online">
                <img class="profile-img" src="https://picsum.photos/200/300" alt=""/>
            </div>
            <div class="name">{{ user.username }}</div>
        </div>
        <div class="chat-box-sidepanel-search">
            <label for=""><i class="fa fa-search" aria-hidden="true"></i></label>
            <input type="text" placeholder="Search contacts..."/>
        </div>
        <div class="chat-box-sidepanel-contacts">
            <chat-item v-for="conversion in conversions"
                          :key="conversion.id"
                          :chat="conversion"
                          :conversion="conversion"

            >
            </chat-item>
        </div>
        <new-chat-modal
            :show-modal="showNewContactModal"
            @modalHidden="modalHidden"
            @contactSelected="contactSelected"
        ></new-chat-modal>
        <div class="chat-box-sidepanel-footer">
            <button @click="selectContacts">
                <i class="fa fa-user-plus fa-fw" aria-hidden="true"></i>
                <span>
                    New Chat
                </span>
            </button>
            <button>
                <i class="fa fa-cog fa-fw" aria-hidden="true"></i>
                <span>
                    Settings
                </span>
            </button>
        </div>
        <!--        <div id="contacts">-->
        <!--            <ul>-->
        <!--                <contact-item-->
        <!--                    v-for="userItem in users"-->
        <!--                    :key="userItem.id"-->
        <!--                    :user="userItem"-->
        <!--                ></contact-item>-->
        <!--            </ul>-->
        <!--        </div>-->
        <!--&lt;!&ndash;        <div id="bottom-bar">&ndash;&gt;-->
        <!--&lt;!&ndash;            <button id="addcontact"><i class="fa fa-user-plus fa-fw" aria-hidden="true"></i> <span>Add contact</span>&ndash;&gt;-->
        <!--&lt;!&ndash;            </button>&ndash;&gt;-->
        <!--&lt;!&ndash;            <button id="settings"><i class="fa fa-cog fa-fw" aria-hidden="true"></i> <span>Settings</span></button>&ndash;&gt;-->
        <!--&lt;!&ndash;        </div>&ndash;&gt;-->
    </div>
</template>

<script>
    import ChatItem from "./ChatItem";
    import NewChatModal from "./NewChatModal";
    import {mapActions, mapGetters, mapMutations} from 'vuex';

    export default {
        name: "UsersList",
        props: {

        },
        components: {NewChatModal, ChatItem},
        data: () => ({
            users: [],
            showNewContactModal: false
        }),
        computed: {

          ...mapGetters('auth', {
                user: 'authUser'
            }),
          ...mapGetters('chat', {
                conversions: 'conversions',
            }),
        },
        watch: {
            user: function (newVal) {
                if (newVal) {
                    this.listenForUserChatNotifications()
                }
            }
        },
        methods: {
            modalHidden() {
                this.showNewContactModal = false
            },
            contactSelected(selectedContact) {
                axios.post('/api/chats', {
                    sender_id: this.user.id,
                    recipient_id: selectedContact.id
                }).then((response) => {
                    window.bus.$emit('selectedChatChanged')
                })
            },
            selectContacts() {
                this.showNewContactModal = true
            },
          ...mapActions('chat', {
                fetchConversions: 'fetchConversions',
            })
        },
        mounted() {
            this.fetchConversions()
        }
    }
</script>

<style scoped>

</style>
