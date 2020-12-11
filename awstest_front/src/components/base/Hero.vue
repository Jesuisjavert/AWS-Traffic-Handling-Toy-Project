<script>
  // Components
  import { VImg } from 'vuetify/lib'

  export default {
    name: 'Hero',

    extends: VImg,

    props: {
      height: {
        type: [Number, String],
        default: '45vh',
      },
    },
  }
</script>
