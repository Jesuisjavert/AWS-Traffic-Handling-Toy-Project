import Vue from 'vue'
import Vuetify, { VRow } from 'vuetify/lib'
// import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify, {
  components: { VRow },
})
export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#ff6b87',
        secondary: '#FFFFFF',
        accent: '#3AAA1D',
        error: '#ffeaee', 
        info: '#eaf9ff',
        success: '#e0d1ff',
        warning: '#FFC107',
      },
    },
  },
})


// primary : 짙은 벚꽃
// secondary: 흰색
// accent: 월계수 초록
// Error : 연한벚꽃
// info : 연하늘색
// success: 연보라
// warning: 바나나노랑(안씀)