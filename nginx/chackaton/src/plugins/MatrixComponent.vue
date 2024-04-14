<script setup lang="ts">
import { ref, onMounted } from 'vue';



const width = document.documentElement.clientWidth;
const height = document.documentElement.clientHeight;


const yPositions = Array(300).fill(0);
const canvas = ref<HTMLCanvasElement | null>(null);

onMounted(() => {

  if (!canvas.value) return;

  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  const ctx = canvas.value.getContext('2d')!;

  const draw = () => {
    ctx.fillStyle = 'rgba(0,0,0,.1)';
    ctx.fillRect(0, 0, width, height);
    ctx.fillStyle = '#0F0';
    ctx.font = '10pt Georgia';
    yPositions.forEach((y, index) => {
      const text = String.fromCharCode(1e2 + Math.random() * 33);
      const x = (index * 10) + 10;
      ctx.fillText(text, x, y);
      if (y > 100 + Math.random() * 1e4) {
        yPositions[index] = 0;
      } else {
        yPositions[index] = y + 10;
      }
    });
  };

  let Game_Interval: ReturnType<typeof setInterval>;

  const runMatrix = () => {
    if (Game_Interval) clearInterval(Game_Interval);
    Game_Interval = setInterval(draw, 70);
  };


  runMatrix();

  setInterval(draw, 200);
});


</script>

<template>

  <canvas class="canvas" ref="canvas" :width="width" :height="height" />


</template>

