<template>
  <div>
    <div class="text-center pa-3">
      <v-btn
        icon
        @click="showTabs = !showTabs"
      >
        <v-icon>mdi-view-grid</v-icon>
      </v-btn>
    </div>

    <v-expand-transition>
      <v-tabs
        v-if="showTabs"
        v-model="filter"
        background-color="transparent"
        centered
        hide-slider
      >
        <v-tab
          v-for="(tab, i) in categories"
          :key="i"
          :href="`#${tab}`"
        >
          {{ tab }}
        </v-tab>
      </v-tabs>
    </v-expand-transition>
  </div>
</template>

<script>
  // Utilities
  import { sync } from 'vuex-pathify'

  export default {
    name: 'VFilter',

    data: () => ({
      showTabs: false,
    }),

    computed: {
      ...sync('photographs', [
        'categories',
        'filter',
      ]),
    },
  }
</script>
