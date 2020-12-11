<template>
  <v-footer
    class="justify-center"
    color="#ffffff"
    height="156"
    inset
  >
    <div class="text-center">
      <v-btn
        class="ma-1"
        icon
        text
        color="primary"
        href="https://www.instagram.com/unialike"
      >
        <v-icon>mdi-instagram</v-icon>
      </v-btn>
      <v-btn
        class="ma-1"
        icon
        text
        color="primary"
     >
        <v-icon>mdi-twitter</v-icon>
      </v-btn>
     <v-btn
        class="ma-1"
        icon
        text
        color="primary"
      >
        <v-icon>mdi-facebook</v-icon>
      </v-btn>
      <div class="my-3" />

      <div>
        Copyright &copy; {{ date }}&nbsp;<strong>Kang Donghoon</strong>
      </div>
    </div>
  </v-footer>
</template>

<script>
  export default {
    name: 'CoreFooter',

    data: () => ({
      date: (new Date()).getFullYear(),
    }),
  }
</script>
