<template>
  <v-navigation-drawer
    v-model="drawer"
    right
    fixed
    temporary
  >
    <v-list>
      <v-list-item
        v-for="(link, i) in links"
        :key="i"
        :to="{
          name: link
        }"
        active-class="primary--text font-weight-bold"
        class="subtitle-1"
        exact
        min-width="128"
        text
      >
        <v-list-item-content>
          <v-list-item-title v-text="link" />
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <template v-slot:append>
      <div class="py-8">
        <v-img
          :src="require('@/assets/logo.png')"
          class="mx-auto mb-8"
          max-width="128"
        />

        <div class="text-center title">
          <span class="primary--text">AWS Test</span><br><span class="display-1 font-weight-bold">Jesuisjavert</span>
        </div>
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
  // Utilities
  import { mapState } from 'vuex'

  export default {
    name: 'CoreDrawer',

    computed: {
      ...mapState(['links']),
      drawer: {
        get () {
          return this.$store.state.drawer
        },
        set (val) {
          this.$store.commit('SET_DRAWER', val)
        },
      },
    },
  }
</script>
