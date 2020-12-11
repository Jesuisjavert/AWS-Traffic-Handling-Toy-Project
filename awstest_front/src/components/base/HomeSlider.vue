<template>
  <div>
    <VueSlickCarousel v-bind="settings">
      <div><HomeHero1 /></div>
      <div><HomeHero2 /></div>
      <div><HomeHero3 /></div>
    </VueSlickCarousel>
  </div>
</template>
 
<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  import 'vue-slick-carousel/dist/vue-slick-carousel.css'
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'
  
  import HomeHero1 from '@/components/base/HomeHero1'
  import HomeHero2 from '@/components/base/HomeHero2'
  import HomeHero3 from '@/components/base/HomeHero3'

  export default {
    name: 'MyComponent',
    components: { VueSlickCarousel, HomeHero1, HomeHero2, HomeHero3},
    data() {
        return {
          settings: {
            "infinite": true,
            "slidesToScroll": 1,
            "autoplay": true,
            "autoplaySpeed": 2000,
            "pauseOnDotsHover": true,
            "pauseOnFocus": true,
            "pauseOnHover": true,
          }
        }
      },
  }
</script> 