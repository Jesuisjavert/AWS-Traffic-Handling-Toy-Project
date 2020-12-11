<template>
  <base-hero
    :src="require('@/assets/hero8.jpg')"
    gradient="to top, #419B911F, transparent"
    v-bind="$attrs"
  >
    <slot />
  </base-hero>
</template>
