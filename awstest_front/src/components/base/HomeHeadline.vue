<template>
  <section
    id="intro"
    class="text-center mb-12"
  >
    <h1 class="display-2 font-weight-light mb-8">
      This is a TEST Page of Kang Donghoon
    </h1>

    <v-responsive
      class="mx-auto subtitle-1 grey--text"
      max-width="800"
    >
      이 곳은 가상의 회사에 간단히 지원서를 작성해 볼 수 있는 테스트 페이지 입니다.<br>
      Membership 페이지에서, 회원가입을 하시면 지원할 수 있습니다. <br>
      직무는 총 5가지로, 지원동기와 첨부사진을 보낼 수 있습니다. (여러 장 가능)<br><br>
      이 페이지는 테스트 용도로, 이력서에 여러장의 사진을 보낼시 (or 트래픽이 갑자기 증가할 시)<br>
      제가 설계한 아키텍처가 잘 작동하는지 확인해보기 위한 Test 페이지 입니다.<br>
      기본적으로 그래서 한번의 이력서 작성으로 총 10번 DB에 저장되도록 의도적으로 코드를 작성했으며,<br>
      업로드한 이미지는 Amazon EC2의 WEB서버 -> WAS -> DB -> S3 스토리지에 저장됩니다.<br>
      <br>
      자세한 코드는 이 곳에서 볼 수 있습니다<br>
      <a href="https://github.com/Jesuisjavert/awsTest">https://github.com/Jesuisjavert/awsTest</a>
    </v-responsive>
  </section>
</template>

<script>
  export default {
    name: 'HomeHeadline',
  }
</script>
