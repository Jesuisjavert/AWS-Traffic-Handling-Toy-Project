<template>
  <v-container
    id="home"
    class="pt-12 pb-0 px-0"
    fluid
    tag="section"
  >
    <home-headline />

</v-container>
</template>

<script>
  export default {
    name: 'Home',

    components: {
      HomeHeadline: () => import('@/components/base/HomeHeadline'),
    },
  }
</script>

<style lang="sass">
  .signature
    font-family: 'Cedarville Cursive', cursive !important
    font-size: 2rem
    font-style: italic
</style>
