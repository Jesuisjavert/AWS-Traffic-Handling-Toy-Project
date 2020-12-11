
<script>
  // Extensions
  import View from '@/views/View'

  // Mixins
  import LoadSections from '@/mixins/load-sections'

  export default {
    name: 'Analysis',

    metaInfo: { title: 'Analysis' },

    extends: View,

    mixins: [
      LoadSections([
        'Analysis',
      ]),
    ],

    props: {
      id: {
        type: String,
        default: 'analysis',
      },
    },
  }
</script>
