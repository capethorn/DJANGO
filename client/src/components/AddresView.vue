<script setup>
import { ref, onBeforeMount } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie';

const items = ref([]);
const itemToAdd = ref({});
const itemToEdit = ref({});

async function fetchItems() {
  const r = await axios.get("/api/addres/");
  items.value = r.data;
}

onBeforeMount(() => {
  axios.defaults.headers.common['X-CSRFToken'] = Cookies.get("csrftoken");
  fetchItems();
});

async function onAdd() {
  await axios.post("/api/addres/", { ...itemToAdd.value });
  await fetchItems();
  itemToAdd.value = {};
}

async function onRemoveClick(item) {
  await axios.delete(`/api/addres/${item.id}/`);
  await fetchItems();
}

async function onEditClick(item) {
  itemToEdit.value = { ...item };
}

async function onUpdate() {
  await axios.put(`/api/addres/${itemToEdit.value.id}/`, { ...itemToEdit.value });
  await fetchItems();
}
</script>

<template>
  <div>
    <h2>Адреса</h2>
    <form @submit.prevent.stop="onAdd" class="mb-4">
      <div class="row">
        <div class="col"><div class="form-floating"><input type="text" class="form-control" v-model="itemToAdd.addres" required /><label>Адрес</label></div></div>
        <div class="col-auto"><button class="btn btn-primary h-100">Добавить</button></div>
      </div>
    </form>
    <div v-for="item in items" :key="item.id" class="d-flex align-items-center mb-2">
      <div class="flex-grow-1">{{ item.addres }}</div>
      <button class="btn btn-success me-2" @click="onEditClick(item)" data-bs-toggle="modal" data-bs-target="#editAdrModal"><i class="bi bi-pen-fill"></i></button>
      <button class="btn btn-danger" @click="onRemoveClick(item)"><i class="bi bi-x"></i></button>
    </div>
    <div class="modal fade" id="editAdrModal" tabindex="-1">
      <div class="modal-dialog"><div class="modal-content">
        <div class="modal-header"><h1 class="modal-title fs-5">Редактировать</h1><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
        <div class="modal-body">
          <div class="form-floating mb-3"><input type="text" class="form-control" v-model="itemToEdit.addres" required /><label>Адрес</label></div>
        </div>
        <div class="modal-footer"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button><button data-bs-dismiss="modal" type="button" class="btn btn-primary" @click="onUpdate">Сохранить</button></div>
      </div></div>
    </div>
  </div>
</template>