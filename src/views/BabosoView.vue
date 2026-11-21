<template>
  <div class="view">
    <LogoComponent />
    <QuestionsComponent v-if="!result" @finish="result = $event" />

    <div v-else class="card">
      <p class="percentage">{{ result.percentage }}%</p>
      <h2>{{ result.title }}</h2>
      <p class="message">{{ result.description }}</p>
      <button type="button" class="btn" @click="result = null">
        Repetir
      </button>
    </div>
  </div>
</template>

<script>
import LogoComponent from '@/components/LogoComponent.vue';
import QuestionsComponent from '@/components/QuestionsComponent.vue';

export default {
  name: "BabosoView",
  components: {
    QuestionsComponent,
    LogoComponent
  },
  data() {
    return {
      result: null
    };
  }
};
</script>

<style lang="scss" scoped>
.view {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 12px;
  min-height: 100vh;
  padding: 2vh 0;
}

.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 14px;
  width: 30%;
  min-height: 30vh;
  padding: 32px 24px;
  border: 1px solid darkred;
  border-radius: 8px;
  background: #2a2a2a;
  color: #f0f0f0;
  text-align: center;
}

.percentage {
  font-size: 56px;
  font-weight: 700;
  color: #ff6b6b;
}

.message {
  max-width: 380px;
  font-size: 15px;
  line-height: 1.5;
  color: #bbb;
}

.btn {
  min-width: 160px;
  padding: 10px 18px;
  border: 1px solid darkred;
  border-radius: 6px;
  background: darkred;
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;

  &:hover {
    background: #a80000;
  }
}

@media (max-width: 768px) {
  .card {
    width: 92%;
    padding: 24px 18px;
  }

  .percentage {
    font-size: 44px;
  }

  .message {
    max-width: 100%;
  }
}

@media (max-width: 480px) {
  .card {
    width: 96%;
    padding: 20px 14px;
    gap: 12px;
  }

  .percentage {
    font-size: 38px;
  }

  .btn {
    width: 100%;
    min-width: 0;
  }
}
</style>
