<script setup lang="ts">
import { ref } from 'vue';
import { useQuasar } from 'quasar';

defineOptions({
  name: 'IndexPage'
});

const $q = useQuasar();

const file = ref<File | null>(null);
const isLoading = ref<boolean>(false);
const resultFileUrl = ref<string>('');

const formSubmitHandler = async () => {
  if (!file.value) {
    $q.notify({
      message: 'Ошибка! Не удалось найти файл',
      color: 'negative'
    });
    return;
  }

  try {
    isLoading.value = true;

    const baseURL: string = import.meta.env.VITE_API_URL;

    const data = new FormData();
    data.append('file', file.value);

    $q.notify({
      message: 'Уже отправляем :)',
      color: 'info'
    });

    const response = await fetch(`${baseURL}/file/upload`, {
      method: 'POST',
      body: data
    });


    const resultData = await response.json();
    if (resultData?.url) {
      $q.notify({
        message: 'Братский успешный успех!',
        color: 'positive'
      });
      resultFileUrl.value = resultData.url;
      file.value = null;
    }
  } catch (e) {
    $q.notify({
      message: 'Братья потерпели неудачу... Извинитесь',
      color: 'negative'
    });
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <q-page class="main-page row items-center justify-evenly">
    <section class="result" v-if="resultFileUrl">
      <div>
        <q-btn
          :href="resultFileUrl"
          text-color="accent"
          label="Скачать результат"
          target="_blank"
          outline
          icon="download"
          color="primary"
        />
      </div>
      <q-btn
        label="Отправить ещё раз"
        icon="refresh"
        text-color="accent"
        dense
        color="secondary"
        outline
        @click="resultFileUrl = ''"
      />
    </section>
    <q-form class="form column" @submit.prevent="formSubmitHandler" v-else>
      <q-uploader
        class="my-text-green"
        label="Загрузите файл с датасетом"
        @added="(files) => (file = files[0])"
        accept=".csv"
        :disable="isLoading"
        color="black"
        text-color="accent"
        dark

      />
      <q-btn
        label="Отправить"
        text-color="accent"
        color="primary"
        :loading="isLoading"
        type="submit"
        :disable="!file"
        outline
        rounded
      />
    </q-form>
  </q-page>
</template>

<style lang="scss" scoped>
.form {
  padding: 2.5rem;
  background: #232323;
  border-radius: 15px;
  box-shadow: 5px 5px 10px #000;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.main-page {
  position: relative;
  z-index: 10;
}

.result {
  display: flex;
  flex-direction: column;
  gap: 15px;
  background: #232323;
  padding: 30px;
  border-radius: 30px;
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  border: 0;
  clip: rect(0 0 0 0);
}
</style>
