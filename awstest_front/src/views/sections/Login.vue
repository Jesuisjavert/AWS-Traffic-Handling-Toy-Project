<template>
  <base-section
    id="info-alt"
    space="56"
  >
    <v-container>
      <v-row justify="center">
        <v-col
          cols="12"
          md="6"
        >
          <base-login-form title="Login" />
        </v-col>
      </v-row>
    </v-container>
  </base-section>
</template>

<script>
  export default {
    name: 'SectionLogin',
  }
</script>
