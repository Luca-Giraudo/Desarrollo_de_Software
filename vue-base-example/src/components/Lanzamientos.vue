<template>
    <div>
      <h2>Listado de Lanzamientos</h2>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Fecha</th>
            <th>Plataforma</th>
            <th>Desarrollador</th>
            <th>Descripción</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="lanzamiento in lanzamientos" :key="lanzamiento.id">
            <td>{{ lanzamiento.name }}</td>
            <td>{{ lanzamiento.date }}</td>
            <td>{{ lanzamiento.platform_name }}</td>
            <td>{{ lanzamiento.developer_name }}</td>
            <td>{{ lanzamiento.description }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
    data() {
    return {
        lanzamientos: [],
    };
},
methods: {
    cargarLanzamientos() {
        axios.get('http://localhost:8000/lanzamientos/')
        .then((response) => {
        // Ordenar los lanzamientos por fecha
            this.lanzamientos = response.data.sort((a, b) => new Date(a.date) - new Date(b.date));
        })
        .catch((error) => {
            console.error(error);
        });
    },
},
mounted() {
    this.cargarLanzamientos();
  },
};
</script>

