<template>
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <div class="col" v-for="product in products" :key="product.id">
      <div class="card" style="width: 18rem">
        <img
          class="card-img-top"
          :src="product.image"
          alt="Imagen de {{ product.name }}"
        />
        <div class="card-body">
          <h5 class="card-title">{{ product.name }}</h5>
          <p class="card-text">
            {{ product.category }}
          </p>
          <p class="card-text">
            {{ product.description }}
          </p>
          <p class="card-text">
            ${{ product.price }} ({{ product.price_type }})
          </p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HomeView",
  data() {
    return {
      products: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/products/")
      .then((response) => {
        this.products = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
