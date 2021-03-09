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
          :src="require('@/assets/sli0.png')"
          style="height = 100"
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
           Architecture<br>
          </h1>

          <p>
           제가 구현한 웹 어플리케이션 아키텍쳐의 구조는 다음과 같습니다.<br>
           <br>기본적으론 대용량 트래픽에 대응하기 위해 이렇게 설계했습니다.<br>
           1) EC2, WEB서버, WAS , S3 , CloudFront 를 이용해 시스템을 구축했습니다.<br>
           Django - Backend API WAS / Vue(Vuetify) -  Frontend Web Server / Nginx / Gunicorn 배포<br> 
           2) AWS Route 53을 이용해, jesuisjavert.com 이라는 도메인을 구입하고, 하위 서브넷을 지정해 awstest.jesuisjavert.com 으로 포트를 연결했습니다. <br>
           3) Auto Scaling 기능과, Loadbalancing 기능 그리고 CDN 을 위해 cloudfront 를 도입하고, CloudWatch 대시보드 기능을 이용해 트래픽을 분석할 수 있는 시스템도 만들었습니다. <br>
          </p>
        </v-responsive>
      </v-col>
    </v-row>
     <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      >
        <VueSlickCarousel v-bind="settings">
          <div>
            <v-img
          :src="require('@/assets/sl0.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/sl3.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/sl4.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/slide123.png')"
          />
          </div>
        </VueSlickCarousel>
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
            Backend & Frontend<br>
          </h1>

          <p>
            <h3>옆의 사진은 슬라이드 입니다.</h3>
           Django Backend 의 Modeling과 Logic을 담당하는 views.py<br> (다중이미지 업로드 및 기본 이력서 CRUD)<br>
           Django REST API와 Section & Component 하여 체계적으로 구성한 Vue (Vuetify library) 기반 Frontend 입니다. (모바일 반응형)<br>
           후에, Django 는 Gunicorn을 통해 배포했고, Vue는 Nginx 포트 설정을 통해 배포했습니다.<br>
          </p>

        </v-responsive>
      </v-col>
    </v-row>
    <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      >
        <VueSlickCarousel v-bind="settings">
          <div>
            <v-img
          :src="require('@/assets/sli10.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/sli11.png')"
          />
          </div>
        </VueSlickCarousel>
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
            Route 53<br>
          </h1>

          <p>
            <h3>옆의 사진은 슬라이드 입니다.</h3>
           AWS의 Route 53 기능을 이용해 DNS 서버와 EC2 인스턴스를 연결했습니다.<br>
           제 아이디인 jesuisjavert.com 을 구매했고, 그 DNS 밑에 awstest.jesuisjavert.com 레코드를 연결했습니다 <br>
           Route 53 기능을 통해, jesuisjavert.com 밑에 xxxx.jesuisjavert.com 과 같은 서브넷을 두는 것이 가능해집니다. <br>
          </p>

          
        </v-responsive>
      </v-col>
    </v-row>
    <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      >
         <VueSlickCarousel v-bind="settings">
          <div>
            <v-img
          :src="require('@/assets/newsl1.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/newsl3.png')"
          />
          </div>
        </VueSlickCarousel>
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
            Load Balancing<br>
          </h1>
          <p>
            <h3>옆의 사진은 슬라이드 입니다.</h3>
            AWS LoadBalancer 설정입니다. <br>프로세스 하중이 낮은 웹서버로 트래픽을 분산 시켜, 서버 다운를 미연에 방지하고자 하는 방식입니다.
          </p>

        </v-responsive>
      </v-col>
    </v-row>
    <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      >
        <VueSlickCarousel v-bind="settings">
          <div>
            <v-img
          :src="require('@/assets/newsl4.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/newsl5.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/newsl6.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/newsl8.png')"
          />
          </div>
          <div>
            <v-img
          :src="require('@/assets/newsl9.png')"
          />
          </div>
        </VueSlickCarousel>
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
            Auto Scaling<br>
          </h1>

          <p>
            <h3>옆의 사진은 슬라이드 입니다.</h3>
           트래픽이 증가할 것으로 예상되면, WEB서버 or WAS서버를 자동적으로 Scale Out 하여 트래픽을 감당해주는 서비스입니다.<br>
           이를 이용하면, 트래픽 급증에 대비하여 큰 인프라를 구비할 필요 없고,<br>
           채용 시즌이후 트래픽이 떨어졌을때는 자동으로 Scale이 줄어들어 관리 및 비용의 효율성을 높일 수 있는 기술입니다. <br>
           이를 통해 클라우드 시스템이 가진 확장성과 유연성의 장점을 극대화 할 수 있습니다.<br>
           Auto Scaling 조정 정책은 평균 PC 사용률이 80 이상일 경우에 새로운 EC2 서버를 Scale Out 하도록 설정했습니다.<br>
          </p>
        </v-responsive>
      </v-col>
    </v-row>
    <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      >
        <v-img
          :src="require('@/assets/slide.png')"
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
            CloudWatch.<br>
          </h1>

          <p>
            AWS CloudWatch 기능을 이용해, 트래픽, CPU 사용률 등을 감시하고 분석할 수 있도록 했습니다.<br>
          </p>

        </v-responsive>
      </v-col>
    </v-row>
    <v-row
      class="ma-0"
      no-gutters
    >
      <v-col
        cols="12"
        md="6"
      >
        <v-img
          :src="require('@/assets/slifi.png')"
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
            총평<br>
          </h1>

          <p>
            대용량 트래픽을 염두에 둔 시스템 아키텍처를 직접 내 손으로 구현해보는 것은 굉장히 흥미로운 작업이었습니다. <br>
            실제로 이 기술들을 구현하기 위해, AWS의 공식 문서를 참조하며 내 스스로도 많은 지식을 얻은 것 같아 뿌듯하고,<br>
            추가적으로 아직 구현하지 못한 Elastic Cache나 Serverless 방식을 도입한 AWS Lambda도 도입해보고 싶습니다.<br>
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
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

  export default {
    name: 'Analysis',
    components: { VueSlickCarousel},
    data() {
    return {
      settings: {
        "infinite": true,
        "slidesToScroll": 1,
        "pauseOnDotsHover": true,
        "pauseOnFocus": true,
        "pauseOnHover": true,
      }
    }
  },
  }
  
</script>

<style lang="sass">
  .signature
    font-family: 'Cedarville Cursive', cursive !important
    font-size: 2rem
    font-style: italic
</style>
