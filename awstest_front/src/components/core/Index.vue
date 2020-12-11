<template>
  <v-app>
    <core-app-bar />

    <core-drawer />

    <core-view />

    <core-footer />
  </v-app>
</template>

<script>
  export default {
    name: 'HomeLayout',

    components: {
      CoreAppBar: () => import('./AppBar'),
      CoreDrawer: () => import('./Drawer'),
      CoreView: () => import('./View'),
      CoreFooter: () => import('./Footer'),
    },
  }
</script>
