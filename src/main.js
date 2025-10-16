import { createApp } from 'vue'
import App from './App.vue'

console.log('🎯 Inicializando aplicación Vue 3...');

const app = createApp(App);

app.mount('#app');

console.log('✅ Aplicación Vue montada exitosamente');
