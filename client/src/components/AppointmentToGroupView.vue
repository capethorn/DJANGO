<script setup>
import { ref, onBeforeMount, computed } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie';

const items = ref([]);
const groups = ref([]); // Список групповых тренировок для выпадающего списка
const itemToAdd = ref({});
const itemToEdit = ref({});

// Словарик для красивого вывода названия группы по её ID
const groupsById = computed(() => {
  let r = {};
  for (let g of groups.value) r[g.id] = g;
  return r;
});

async function fetchAll() {
  const rItems = await axios.get("/api/appointment-to-group/");
  items.value = rItems.data;
  
  const rGroups = await axios.get("/api/appointment-group/");
  groups.value = rGroups.data;
}

onBeforeMount(() => {
  axios.defaults.headers.common['X-CSRFToken'] = Cookies.get("csrftoken");
  fetchAll();
});

async function onAdd() {
  await axios.post("/api/appointment-to-group/", { ...itemToAdd.value });
  await fetchAll();
  itemToAdd.value = {};
}

async function onRemoveClick(item) {
  await axios.delete(`/api/appointment-to-group/${item.id}/`);
  await fetchAll();
}

async function onEditClick(item) {
  const dataCopy = { ...item };
  if (dataCopy.data) dataCopy.data = dataCopy.data.substring(0, 16);
  itemToEdit.value = dataCopy;
}

async function onUpdate() {
  await axios.put(`/api/appointment-to-group/${itemToEdit.value.id}/`, { ...itemToEdit.value });
  await fetchAll();
}
</script>

<template>
  <div>
    <h2>Записи клиентов на групповые</h2>
    <form @submit.prevent.stop="onAdd" class="mb-4">
      <div class="row">
        <div class="col-auto">
          <div class="form-floating">
            <input type="number" class="form-control" v-model="itemToAdd.user" required />
            <label>ID Пользователя</label>
          </div>
        </div>
        <div class="col-auto">
          <div class="form-floating">
            <select class="form-select" v-model="itemToAdd.group" required>
              <option :value="g.id" v-for="g in groups" :key="g.id">{{ g.name }}</option>
            </select>
            <label>Групповая тренировка</label>
          </div>
        </div>
        <div class="col-auto">
          <div class="form-floating">
            <input type="datetime-local" class="form-control" v-model="itemToAdd.data" required />
            <label>Дата и время</label>
          </div>
        </div>
        <div class="col-auto"><button class="btn btn-primary h-100">Добавить</button></div>
      </div>
    </form>

    <div v-for="item in items" :key="item.id" class="d-flex align-items-center mb-2">
      <div class="flex-grow-1">
        Юзер ID: {{ item.user }} | Группа: {{ groupsById[item.group]?.name }} | Дата: {{ item.data }}
      </div>
      <button class="btn btn-success me-2" @click="onEditClick(item)" data-bs-toggle="modal" data-bs-target="#editGroupBookingModal"><i class="bi bi-pen-fill"></i></button>
      <button class="btn btn-danger" @click="onRemoveClick(item)"><i class="bi bi-x"></i></button>
    </div>

    <div class="modal fade" id="editGroupBookingModal" tabindex="-1">
      <div class="modal-dialog"><div class="modal-content">
        <div class="modal-header"><h1 class="modal-title fs-5">Редактировать</h1><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
        <div class="modal-body">
          <div class="form-floating mb-3">
            <input type="number" class="form-control" v-model="itemToEdit.user" required />
            <label>ID Пользователя</label>
          </div>
          <div class="form-floating mb-3">
            <select class="form-select" v-model="itemToEdit.group" required>
              <option :value="g.id" v-for="g in groups" :key="g.id">{{ g.name }}</option>
            </select>
            <label>Групповая тренировка</label>
          </div>
          <div class="form-floating mb-3">
            <input type="datetime-local" class="form-control" v-model="itemToEdit.data" required />
            <label>Дата и время</label>
          </div>
        </div>
        <div class="modal-footer"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button><button data-bs-dismiss="modal" type="button" class="btn btn-primary" @click="onUpdate">Сохранить</button></div>
      </div></div>
    </div>
  </div>
</template>