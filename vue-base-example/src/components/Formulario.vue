<template>
    <div>
      <h2>Agregar Nuevo Lanzamiento</h2>
      <form @submit.prevent="agregarLanzamiento">
        <label>Nombre:</label>
        <input v-model="nuevoLanzamiento.name" required>

        <label>Fecha:</label>
        <input type="date" v-model="nuevoLanzamiento.date" required>

        <label>Plataforma:</label>
        <select v-model="nuevoLanzamiento.platform" required>
            <option value="">Seleccione una plataforma</option>
            <option v-for="plataforma in plataformas" :key="plataforma.id" :value="plataforma.id">{{ plataforma.name }}</option>
        </select>

        <label>Desarrolladora:</label>
        <select v-model="nuevoLanzamiento.developer" required>
            <option value="">Seleccione una desarrolladora</option>
            <option v-for="desarrolladora in desarrolladoras" :key="desarrolladora.id" :value="desarrolladora.id">{{ desarrolladora.name }}</option>
        </select>

        <label>Descripción:</label>
        <textarea v-model="nuevoLanzamiento.description" required></textarea>

        <button type="submit">Agregar</button>
      </form>
    </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
  data() {
    return {
      nuevoLanzamiento: {
        name: '',
        date: '',
        platform: '',
        developer: '',
        description: ''
      },
      plataformas: [],
      desarrolladoras: []
    };
  },
  mounted() {
    // Obtener la lista de plataformas desde la API
    axios.get('http://localhost:8000/platforms/')
      .then((response) => {
        this.plataformas = response.data;
      })
      .catch((error) => {
        console.error(error);
      });

      // Obtener la lista de desarrolladoras desde la API
    axios.get('http://localhost:8000/developers/')
      .then((response) => {
        this.desarrolladoras = response.data;
      })
      .catch((error) => {
        console.error(error);
      });
  },
  methods: {
    agregarLanzamiento() {
      axios.post('http://localhost:8000/lanzamientos/', this.nuevoLanzamiento)
        .then((response) => {
          // Lanzamiento agregado exitosamente, puedes redirigir o actualizar la lista de lanzamientos.
        })
        .catch((error) => {
          console.error(error);
        });
    }
  }
}
</script>
