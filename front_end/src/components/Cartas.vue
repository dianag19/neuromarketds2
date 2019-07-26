<template>
  <div>
    <div class="container">
      <b-card-group deck>
        <b-card
          v-for="i in this.trae"
          :key="i.id"
          border-variant="dark"
          text-variant="dark"
          header="NeuroMarket"
          header-bg-variant="dark"
          header-text-variant="white"
          class="text-center mb-2"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 25rem;"
        >
          <form v-on:submit.prevent="Getid(i)">
            
            <b-card-img class="fluid" v-bind:src="i.images"></b-card-img>
            <b-card-title>{{i.nombre_producto}}</b-card-title>
            <b-card-text>{{i.descripcion}}</b-card-text>
            <b-card-text><span><h3>${{i.precio_unidad}}</h3></span></b-card-text>
            <b-button type="submit" variant="danger">Detalles</b-button>
          </form>
        </b-card>
      </b-card-group>
    </div>
  </div>
</template>
<script>
import { mapGetters, mapMutations } from "vuex";
export default {
  methods: {
    ...mapMutations(["setDetalle"]),
    Getid(i) {
      this.setDetalle(i);
      this.$router.push({ path: "/Details" });
    }
  },
  computed: {
    ...mapGetters(["getProducts"]),
    trae() {
      return this.getProducts;
    }
  }
};
</script>
<style >
</style>
