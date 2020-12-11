<template>
  <v-row>
    <v-col cols="auto">
      <v-avatar
        size="56"
        color="grey"
      >
        <v-img :src="comment.avatar" />
      </v-avatar>
    </v-col>

    <v-col :cols="nested ? 12 : 11">
      <v-row>
        <v-col
          class="body-1 font-weight-black"
          cols="12"
          md="6"
          v-text="comment.user"
        />

        <v-col
          class="text-right body-2 font-weight-bold text-uppercase text-no-wrap"
          cols="6"
          md="3"
          v-text="comment.date"
        />

        <v-col
          class="text-right body-2 font-weight-bold text-uppercase"
          cols="6"
          md="3"
        >
          Reply
        </v-col>

        <v-col
          class="grey--text text--darken-1 subtitle-1"
          cols="12"
          v-text="comment.text"
        />

        <template v-if="comment.replies && comment.replies.length">
          <template v-for="(reply, i) in comment.replies">
            <blog-post-comment
              :key="i"
              :comment="reply"
              class="mx-0 mx-md-12"
              nested
            />
          </template>
        </template>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    name: 'BlogPostComment',

    props: {
      comment: {
        type: Object,
        default: () => ({
          avatar: undefined,
          user: undefined,
          date: undefined,
          replies: [],
          text: undefined,
        }),
      },
      nested: {
        type: Boolean,
        default: false,
      },
    },
  }
</script>
