<template>
  <div class="Detalles-relative">
    <div class="container">
      <b-row no-gutters>
          <b-col md="6">
            <b-card-img style="max-height:600px;" v-bind:src="getDetails.images" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6" class="text-left">
            <br />
            <br />
            <br />
            <b-card-title>
              <h2>{{getDetails.nombre_producto}}</h2>
            </b-card-title>
              <h3 class="text-danger">
                <strong>${{getDetails.precio_unidad}}</strong>
              </h3>
            <br />
              <h4>{{getDetails.descripcion}}</h4>
            <b-button href="#" variant="danger">Agregar al carrito</b-button>
          </b-col>
        </b-row>
    </div>
  </div>
</template>
<script>
import { mapGetters, mapMutations } from "vuex";
import Cartas from "@/components/Cartas.vue";
export default {
  methods: {},
  computed: {
    ...mapGetters(["getDetails"])
  },
  name: "Detalles",
  components: {
    Cartas
  }
};
</script>
<style>
</style>
