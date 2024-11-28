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
        @click="getCategoryID(category.id, category.name)"
      >
        {{ category.name }}
      </button>
    </div>
  </section>
</template>
<script>
import axios from "axios";
export default {
  name: "NavigationComponent",

  data() {
    return {
      categories: [],
      categoryID: null,
      categoryName: null,
    };
  },
  methods: {
    getCategoryID(categoryID, categoryName) {
      this.$emit("getCategoryID", categoryID, categoryName);
    },
  },

  mounted() {
    axios
      .get("http://127.0.0.1:8000/api/categories/")
      .then((response) => {
        this.categories = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
