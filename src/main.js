import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import QuestionsComponent from './components/QuestionsComponent.vue'

import axios from 'axios';
import VueAxios from 'vue-axios';
import LogoComponent from './components/LogoComponent.vue';
const app = createApp(App).use(router)
app.use(VueAxios, axios);

app.mount('#app')


app.component(QuestionsComponent,"QuestionsComponent")
app.component(LogoComponent,"LogoComponent")
