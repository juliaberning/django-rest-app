<template>
  <section class="mt-5 text-center mx-auto">
    <h1 class="text-danger">Panadería y Rotisería</h1>
    <!-- Image -->
    <img
      class="img-fluid"
      :src="require('@/assets/img/supermarket.png')"
      alt=""
    />
    <!-- Buttons for Categories -->
    <div class="mt-3">
      <button
        type="button"
        class="btn btn-info"
        v-for="category in categories"
        :key="category.id"
        @click="getCategory(category.id, category.name)"
      >
        {{ category.name }}
      </button>
    </div>
  </section>
</template>
<script setup>
import axios from "axios";
import { ref, defineEmits, onMounted } from "vue";

const categories = ref([]);

const emit = defineEmits(["getCategoryID"]);

const getCategory = (id, name) => {
  emit("getCategoryID", id, name);
};

onMounted(() => {
  axios
    .get("http://127.0.0.1:8000/api/categories/")
    .then((response) => {
      categories.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>
