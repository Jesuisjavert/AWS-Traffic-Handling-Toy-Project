<template>
  <div v-if="!isLogined">
    <base-info-card
      :title="title"
      :subtitle="subtitle"
      space="4"
      color="primary"
    />

    <base-text-field
      id="username"
      v-model="username"
      label="Username"
      required
    />

    <base-text-field
      id="password"
      v-model="password"
      type="password"
      label="Password"
      required
    />
    <base-btn
      :color="!theme.isDark ? 'accent' : 'white'"
      outlined
      target="_blank"
      type="submit"
      @click="login"
    >
      Login
    </base-btn>
    <v-dialog v-model="dialog" persistent max-width="450">
      <template v-slot:activator="{ on, $attrs }">
        <base-btn
          :color="!theme.isDark ? 'accent' : 'white'"
          outlined
          type="submit"
          v-bind="$attrs"
          v-on="on"
        >
          Sign up
        </base-btn>
      </template>
      <v-card>
        <v-card-title class="headline"> Signup </v-card-title>
        <base-text-field
          id="username"
          v-model="username"
          label="Username"
          space="4"
          required
          class="mx-4"
        />
        <base-text-field
          id="password1"
          v-model="password1"
          type="password"
          label="Password1"
          class="mx-4"
          required
        />
        <base-text-field
          id="password2"
          v-model="password2"
          type="password"
          label="Password2"
          class="mx-4"
          required
        />
        <v-card-actions>
          <v-spacer />
          <v-btn color="green darken-1" text @click="signup"> Signup </v-btn>
          <v-btn color="green darken-1" text @click="dialog = false">
            Exit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
  <div v-else>
    <v-container>
      <h4>로그인 되었습니다.</h4>
      <a @click="logout"> logout </a>
      <br /><br />
      <h4>지원하기</h4>
      <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">
              Open Dialog
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">User Profile</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      v-model="name"
                      required
                      label="지원자 이름"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field
                      label="지원동기"
                      v-model="motivation"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select
                      v-model="select"
                      :items="items"
                      item-text="name"
                      label="Task"
                      return-object
                      single-line
                    ></v-select>
                  </v-col>
                </v-row>
              </v-container>
              <small>*표시는 필수항목입니다.</small>
              <br /><br />
              <v-container>
                <v-col cols="8">
                  <span class="mr-2">포트폴리오 사진 :</span>
                  <input
                    ref="imageInput"
                    type="file"
                    @change="uploadImg"
                    accept="image/*"
                  />
                </v-col>
                <v-row>
                  <v-col
                    v-for="reviewImg in reviewImgs"
                    :key="reviewImg"
                    cols="auto"
                  >
                    <v-img
                      v-if="reviewImg"
                      :src="reviewImg"
                      class=""
                      width="200px"
                      height="200px"
                    ></v-img>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="dialog = false">
                Close
              </v-btn>
              <v-btn color="blue darken-1" text @click="submit"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
      <br /><br />
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

// const API_URL = "http://127.0.0.1:8000";
const API_URL = "http://awstest.jesuisjavert.com:8000";


export default {
  name: "BaseLoginForm",
  // Injected from the Vuetify Themeable mixin
  inject: ["theme"],

  props: {
    subtitle: String,
    title: {
      type: String,
      default: "Login"
    }
  },
  data() {
    return {
      select: { name: null },
      items: [
        { name: "경영솔루션 운영" },
        { name: "영업/마케팅" },
        { name: "SW 개발" },
        { name: "UI / UX 디자인" },
        { name: "경영지원" }
      ],
      username: null,
      email: null,
      password: null,
      dialog: false,
      password1: null,
      password2: null,
      name: null,
      motivation: null,
      reviewImgs: [],
      reviewImgsFile: [],
    };
  },
  created() {
    this.logincheck();
  },
  methods: {
    uploadImg(e) {
      const file = e.target.files[0];
      console.log(file);
      this.reviewImgs.push(URL.createObjectURL(file));
      console.log(this.reviewImgs);
      this.reviewImgsFile.push(file);
    },
    async submit() {
      let formdata = new FormData();
      if (!this.reviewImgsFile) {
        formdata.append("name", this.name);
        formdata.append("motivation", this.motivation);
        formdata.append("taskname", this.select.name);
      } else {
        formdata.append("name", this.name);
        formdata.append("motivation", this.motivation);
        for (var i = 0; i < this.reviewImgsFile.length; i++) {
          formdata.append("image", this.reviewImgsFile[i]);
        }
        formdata.append("taskname", this.select.name);
      }
      const headers = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      for (let i = 0; i < 10; i++) {
        await axios
          .post(API_URL + "/api/resume/", formdata, headers)
          .then(res => {
            console.log(res);
          })
          .catch(err => {
            console.log(err.response);
          });
      }
    alert('이력서 작성이 완료되었습니다. 트래픽 테스트 용으로 10번 저장했습니다 !')
    },
    cookies_set(key) {
      this.$cookies.set("auth-token", key);
      this.isLogined = true;
    },
    login() {
      const loginData = {
        username: this.username,
        password: this.password
      };
      axios
        .post(API_URL + "/rest-auth/login/", loginData)
        .then(res => {
          this.cookies_set(res.data.key);
          this.$router.push("/");
        })
        .catch(err => {
          console.log(err.response);
        });
    },
    logincheck() {
      if (this.$cookies.isKey("auth-token")) {
        this.isLogined = true;
      }
    },
    logout() {
      const RequestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios.post(API_URL + "/rest-auth/logout/", RequestHeader).then(res => {
        this.isLogined = false;
        this.$cookies.remove("auth-token");
        this.$router.push("/");
      });
    },
    signup() {
      const signupData = {
        username: this.username,
        password1: this.password1,
        password2: this.password2
      };
      axios
        .post(API_URL + "/rest-auth/signup/", signupData)
        .then(res => {
          this.cookies_set(res.data.key);
          this.$router.push("/");
        })
        .catch(err => {
          console.log(err.response);
        });
    }
  }
};
</script>
