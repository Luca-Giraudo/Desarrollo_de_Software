<template>
  <div id="app">
    <Lanzamientos/>
  </div>
</template>

<script>
import Formulario from './components/Formulario.vue'
import Lanzamientos from './components/Lanzamientos.vue'
import PedirDatos from './components/PedirDatos.vue'

export default {
  name: 'App',
  components: {
    Lanzamientos,
    PedirDatos,
    Formulario
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
