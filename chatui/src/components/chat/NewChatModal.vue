<template>
  <div class="contact--model" :class="showModal?'open':''">
    <div class="drop-shadow"></div>
    <div class="contact--model--body">
      <div class="contact--model--body--toolbar">
        <button class="toolbar-close" @click="$emit('modalHidden')">
          <i class="fa fa-close fa-fw" aria-hidden="true"></i>
        </button>
        <div class="toolbar-title">
          Available Contacts
        </div>

      </div>
      <div class="new-contact-list">
        <div class="new-contact-list-contacts">
          <new-chat-contact-item
              v-for="contact in contacts"
              :key="contact.id"
              :user="contact"
              @contactSelected="contactSelect"
          ></new-chat-contact-item>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {mapActions, mapGetters} from 'vuex'
import NewChatContactItem from "./NewChatContactItem";

export default {
  name: "NewChatModal",
  components: {NewChatContactItem},
  props: {
    showModal: {
      type: Boolean,
      required: true,
      default: false
    }
  },
  data: () => ({
    selectedUser: null
  }),
  computed: {
    modalVisibility: {
      set(newVal) {
        if (!newVal) {
          this.$emit('closePopup')
        }
      },
      get() {
        if (this.showModal) {
        }
        return this.showModal
      }
    },
    ...mapGetters('chat', {
      contacts: 'availableContacts'
    })
  },
  mounted() {
    this.fetchContacts()
  },
  methods: {
    ...mapActions('chat', {
      fetchContacts: "fetchAvailableContacts",
      createContact: "setNewContact"
    }),
    modalHidden() {
      this.$emit('modalHidden')
      this.selectedUser = null
    },
    contactSelect(user) {
      this.selectedUser = user
      this.createContact(user).then(_=>{
        this.fetchContacts()
        this.$emit('modalHidden')
      })
    },
  }
}
</script>

<style lang="scss">
.contact--model {
  visibility: hidden;
  opacity: 0;
  z-index: 10000;
  transition: opacity .1s;

  &.open {
    opacity: 1;
    visibility: visible;
  }

  &--body {
    position: fixed;
    top: 50%;
    transform: translate(-50%, -50%);
    left: 50%;
    width: 500px;
    height: 500px;
    background: #2c3e50;

    &--toolbar {
      font-size: 2rem;
      text-align: center;
      margin: .5rem auto;
      display: flex;
      margin-left: 10px;

      .toolbar-title {
        flex-grow: 1;
      }

      .toolbar-close {
        background: transparent;
        box-shadow: none;
        outline: none;
        border: none;
        color: white;
      }
    }
  }
}

.drop-shadow {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(35, 29, 31, 0.92);
}
</style>
