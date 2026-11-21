<template>
  <div class="logo">
    <img src="@/assets/Icon.png" alt="Logo">
  </div>
</template>

<script>
  export default {
    name: "LogoComponent",
  }
</script>

<style lang="scss" scoped>
.logo {
  display: flex;
  justify-content: center;
  margin-bottom: 0;
}

.logo img {
  max-height: 90px;
  width: auto;
}

@media (max-width: 480px) {
  .logo img {
    max-height: 70px;
  }
}
</style>
