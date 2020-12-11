<template>
  <v-container
    id="about"
    class="pa-0"
    fluid
    tag="section"
  >
    <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      >
        <v-img
          height="calc(100vh - 96px - 156px)"
          src="/javert3.jpg"
        />
      </v-col>

      <v-col
        class="d-block d-md-flex align-center grey lighten-3 pa-6"
        cols="12"
        md="6"
      >
        <v-responsive
          class="mx-auto px-3 px-md-12"
          max-width="750"
        >
          <h1
            class="mb-6"
            :class="$vuetify.breakpoint.mdAndUp ? 'display-1' : 'display-1'"
          >
            안녕하십니까.<br>
          </h1>

          <p>
           저는 SSAFY 3기 출신 개발자, 강동훈입니다.<br>
           사전 과제로 주어졌던 시스템 아키텍쳐 설계 과제를 단순히 아키텍쳐 설계만으로 끝내는게 아니라,<br>
           실제로 구현해보고 그것을 어떻게 도입했는지 소개하는 페이지를 만들어 보았습니다. <br>
           개발자는 백마디 말보다 한줄의 코드로 소통합니다<br>
           한 줄의 코드, 하나의 예시페이지, 하나의 테이블을 통해,<br> 객관적으로 피드백 받으며 성장하는 개발자가 되는 것이 꿈입니다<br>

          </p>

          <div class="signature">
            jesuisjavert
          </div>
        </v-responsive>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'About',
  }
</script>

<style lang="sass">
  .signature
    font-family: 'Cedarville Cursive', cursive !important
    font-size: 2rem
    font-style: italic
</style>
