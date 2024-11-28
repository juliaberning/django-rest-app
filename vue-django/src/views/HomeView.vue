<template>
  <navigation-component-vue @getCategoryID="categoryID" />
  <div class="mb-3" v-if="categoryReceived">
    <h3>
      Productos de la categoría <strong> {{ categoryReceived }}</strong>
    </h3>
    <button class="btn btn-lg btn-warning" @click="resetFilter">
      Mostrar todos los productos
    </button>
    <div
      class="alert alert-warning mt-3"
      role="alert"
      v-if="filteredProducts.length === 0"
    >
      No hay productos en la categoría: {{ categoryReceived }}
    </div>
  </div>

  <div>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col" v-for="product in filteredProducts" :key="product.id">
        <div class="card" style="width: 18rem">
          <img
            class="card-img-top"
            :src="product.image"
            alt="Imagen de {{ product.name }}"
          />
          <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <p class="card-text">Categoría: {{ product.category_name }}</p>
            <p class="card-text">
              {{ product.description }}
            </p>
            <p class="card-text">
              ${{ product.price }} ({{ product.price_type_description }})
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import NavigationComponentVue from "@/components/NavigationComponent.vue";
import { ref, onMounted } from "vue";

const products = ref([]);
const categoryReceived = ref(null);
const filteredProducts = ref([]);

const categoryID = (categoryID, categoryName) => {
  categoryReceived.value = categoryName;
  if (categoryID) {
    filteredProducts.value = products.value.filter(
      (product) => product.category === categoryID
    );
  } else {
    filteredProducts.value = products.value;
  }
};
const resetFilter = () => {
  categoryReceived.value = null;
  filteredProducts.value = products.value;
};

onMounted(() => {
  axios
    .get("http://127.0.0.1:8000/api/products/")
    .then((response) => {
      products.value = response.data;
      filteredProducts.value = products.value;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>
