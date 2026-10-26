<script setup>
import { ref, onBeforeMount } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie';

const items = ref([]);
const itemToAdd = ref({});
const itemToEdit = ref({});
const AddresPictureRef = ref();
const addresAddImageUrl = ref();

async function fetchItems() {
  const r = await axios.get("/api/addres/");
  items.value = r.data;
}

onBeforeMount(() => {
  axios.defaults.headers.common['X-CSRFToken'] = Cookies.get("csrftoken");
  fetchItems();
});

async function addresAddPictureChange() {
  addresAddImageUrl.value = URL.createObjectURL(AddresPictureRef.value.files[0])
}


async function onAdd() {
  const formData = new FormData();

  // вытаскиваем выбранный файл с формы через AddresPictureRef.value.files[0]
  formData.append('image', AddresPictureRef.value.files[0]);

  // явно привязываем поля из itemToAdd
  formData.set('addres', itemToAdd.value.addres);

  // ну и тут указываем в заголовке что отправляем данные с файлом
  await axios.post("/api/addres/", formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
      }
  });

  await fetchItems();
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
        <div class="col-auto">
        <input class="form-control" type="file" ref="AddresPictureRef" @change="addresAddPictureChange">
        </div>
        <div class="col-auto">
        <img :src="addresAddImageUrl" style="max-height: 60px;" alt="">
        </div>
        <div class="col-auto"><button class="btn btn-primary h-100">Добавить</button></div>
      </div>
    </form>
    <div v-for="item in items" :key="item.id" class="d-flex align-items-center mb-2">
      <div class="flex-grow-1">{{ item.addres }}</div>
      <div v-show="item.image" class="me-3">
        <img :src="item.image" style="max-height: 60px;">
      </div>
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