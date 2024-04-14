<script setup lang="ts">
import MatrixComponent from 'src/plugins/MatrixComponent.vue';

defineOptions({
  name: 'MainLayout'
});

</script>

<template>
  <q-layout view="lHh Lpr lFf" class="page">
    <q-header elevated class="bg-black">
      <q-toolbar >
        <q-toolbar-title class="my-text-green">
          Исследование и прогнозирование динамики лояльности участников НПО
        </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-page-container class="page__inner">
      <router-view />


    <MatrixComponent class="page__matrix"/>
    </q-page-container>

    <q-footer>
      <q-toolbar class="bg-black">
        <q-toolbar-title class="text-right my-text-green">
          "Братья навсегда", 2024
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>


<style lang="scss" scoped>
.page {
  font-family: "Pixelify Sans", Arial, sans-serif;

  &__matrix {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
  }

  &__inner {
    background: #232323;
  }
}
</style>
