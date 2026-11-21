<template>
  <div v-if="loading" class="MainContainer">
    <p class="message">Cargando preguntas...</p>
  </div>

  <div v-else-if="questions.length" class="MainContainer">
    <h2 class="question">{{ questions[currentIndex].text }}</h2>

    <ul class="options">
      <li v-for="option in questions[currentIndex].options" :key="option.id">
        <label class="option" :class="{ selected: answers[currentIndex] === option.id }">
          <input
            type="radio"
            :name="'question-' + currentIndex"
            :value="option.id"
            v-model="answers[currentIndex]"
          >
          <span>{{ option.text }}</span>
        </label>
      </li>
    </ul>

    <footer class="quiz-footer">
      <button
        type="button"
        class="btn btn-ghost"
        :disabled="currentIndex === 0"
        @click="cambiarIndice(currentIndex - 1)"
      >
        Anterior
      </button>

      <button
        v-if="currentIndex < questions.length - 1"
        type="button"
        class="btn"
        :disabled="!answers[currentIndex]"
        @click="cambiarIndice(currentIndex + 1)"
      >
        Siguiente
      </button>

      <button
        v-else
        type="button"
        class="btn"
        :disabled="!answers[currentIndex] || calculating"
        @click="getResultado"
      >
        {{ calculating ? "Calculando..." : "Finalizar" }}
      </button>
    </footer>
  </div>
</template>

<script>
// GET  /api/quiz/questions -> [{ id, text, options: [{ id, text }] }]
// POST /api/quiz/result    <- { answers: [{ questionId, optionId }] }
//                          -> { percentage, title, description }

export default {
  name: "QuestionsComponent",
  emits: ["finish"],
  data() {
    return {
      questions: [],
      loading: true,
      calculating: false,
      currentIndex: 0,
      answers: []
    };
  },
  mounted() {
    this.getAllPreguntas();
  },
  methods: {
    getAllPreguntas: async function () {
      this.loading = true;
      await this.axios.get('http://127.0.0.1:8000/api/quiz/questions')
        .then(response => {
          this.questions = response.data;
          this.answers = new Array(response.data.length).fill(null);
              console.log("Preguntas",this.questions)

        })
        .catch(e => {
          console.error('Error al cargar las preguntas', e);
        })
        .finally(() => {
          this.loading = false;
        });
    },

    cambiarIndice: function (i) {
      if (i >= 0 && i < this.questions.length) {
        this.currentIndex = i;
      }
    },

    getResultado: async function () {
      this.calculating = true;
      await this.axios.post('http://127.0.0.1:8000/api/quiz/result', {
        answers: this.questions.map((question, i) => ({
          questionId: question.id,
          optionId: this.answers[i]
        }))
      })
        .then(response => {
          this.$emit('finish', response.data);
        })
        .catch(e => {
          console.error('Error al calcular el resultado', e);
        })
        .finally(() => {
          this.calculating = false;
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.MainContainer {
  display: flex;
  flex-direction: column;
  width: 30%;
  min-height: 30vh;
  margin: 0 auto;
  padding: 24px;
  border: 1px solid darkred;
  border-radius: 8px;
  background: #2a2a2a;
  color: #f0f0f0;
  text-align: left;
}

.message {
  margin: auto;
  font-size: 16px;
  color: #bbb;
  text-align: center;
}

.question {
  margin-bottom: 20px;
  font-size: 22px;
  line-height: 1.4;
  color: #f0f0f0;
}

.options {
  display: flex;
  flex-direction: column;
  gap: 10px;
  list-style: none;
}

.option {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 16px;
  padding: 12px 14px;
  border: 1px solid #555;
  border-radius: 6px;
  cursor: pointer;

  &:hover {
    border-color: #a85a5a;
  }

  &.selected {
    border-color: darkred;
    background: #3a2a2a;
  }

  input {
    appearance: none;
    flex: 0 0 auto;
    width: 18px;
    height: 18px;
    margin: 0;
    border: 2px solid #888;
    border-radius: 50%;
    cursor: pointer;

    &:checked {
      border-color: darkred;
      background: darkred;
      box-shadow: inset 0 0 0 3px #fff;
    }
  }
}

.quiz-footer {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  margin-top: auto;
  padding-top: 20px;
}

.btn {
  min-width: 120px;
  padding: 10px 18px;
  border: 1px solid darkred;
  border-radius: 6px;
  background: darkred;
  color: #fff;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;

  &:hover:not(:disabled) {
    background: #a80000;
  }

  &:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }
}

.btn-ghost {
  background: transparent;
  color: #ff6b6b;

  &:hover:not(:disabled) {
    background: #3a2a2a;
  }
}

@media (max-width: 768px) {
  .MainContainer {
    width: 92%;
    padding: 18px;
  }

  .question {
    font-size: 19px;
  }

  .option {
    font-size: 15px;
    padding: 10px 12px;
  }

  .btn {
    font-size: 15px;
    min-width: 100px;
  }
}

@media (max-width: 480px) {
  .MainContainer {
    width: 96%;
    padding: 14px;
  }

  .question {
    font-size: 17px;
    margin-bottom: 16px;
  }

  .options {
    gap: 8px;
  }

  .option {
    font-size: 14px;
    padding: 10px;
    gap: 10px;
  }

  .quiz-footer {
    flex-direction: column;
    gap: 8px;
  }

  .btn {
    width: 100%;
    min-width: 0;
  }
}
</style>
