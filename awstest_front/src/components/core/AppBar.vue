<template>
  <v-app-bar
    id="core-app-bar"
    app
    color="secondary"
    elevate-on-scroll
    height="96"
  >
    <v-container>
      <v-row>
        <div class="d-flex align-center">
          <v-img
            :src="require('@/assets/logo2.png')"
            contain
            class="shrink mr-2"
            height="90"
            width="200"
            to="home"
            @click="gohome"
            style="cursor: pointer"
          />
        </div>

        <v-spacer />

        <v-toolbar-items
          v-if="$vuetify.breakpoint.smAndUp"
          class="shrink"
        >
          <v-btn
            v-for="(link, i) in links"
            :key="i"
            :to="{
              name: link
            }"
            active-class="primary--text"
            class="subtitle-1 ml-1"
            exact
            min-width="128"
            text
            color
          >
            <span>{{ link }}</span>
          </v-btn>
        </v-toolbar-items>

        <v-app-bar-nav-icon
          v-else
          @click="setDrawer(true)"
        />
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script>
  // Utilities
  import { mapMutations, mapState } from 'vuex'

  export default {
    name: 'CoreAppBar',

    computed: {
      ...mapState(['links']),
    },

    methods: {
      ...mapMutations({
        setDrawer: 'SET_DRAWER',
      }),
      gohome() {
        this.$router.push('/')
      },
    },
  }
</script>
<style lang="sass">
  .signature
    font-family: 'Cedarville Cursive', cursive !important
    font-size: 2rem
    font-style: italic
</style>
