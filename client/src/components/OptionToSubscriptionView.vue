<script setup>
import { ref, onBeforeMount, computed } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie';

const links = ref([]);
const subscriptions = ref([]);
const options = ref([]);
const linkToAdd = ref({});
const linkToEdit = ref({});

const subsById = computed(() => {
  let r = {};
  for (let s of subscriptions.value) r[s.id] = s;
  return r;
});

const optsById = computed(() => {
  let r = {};
  for (let o of options.value) r[o.id] = o;
  return r;
});

async function fetchAll() {
  const rLinks = await axios.get("/api/option-to-subscription/");
  links.value = rLinks.data;
  const rSubs = await axios.get("/api/subscription/");
  subscriptions.value = rSubs.data;
  const rOpts = await axios.get("/api/option/");
  options.value = rOpts.data;
}

onBeforeMount(() => {
  axios.defaults.headers.common['X-CSRFToken'] = Cookies.get("csrftoken");
  fetchAll();
});

async function onAdd() {
  await axios.post("/api/option-to-subscription/", { ...linkToAdd.value });
  await fetchAll();
  linkToAdd.value = {};
}

async function onRemoveClick(link) {
  await axios.delete(`/api/option-to-subscription/${link.id}/`);
  await fetchAll();
}

async function onEditClick(link) {
  linkToEdit.value = { ...link };
}

async function onUpdate() {
  await axios.put(`/api/option-to-subscription/${linkToEdit.value.id}/`, { ...linkToEdit.value });
  await fetchAll();
}
</script>

<template>
  <div>
    <h2>Опции к подпискам</h2>
    <form @submit.prevent.stop="onAdd" class="mb-4">
      <div class="row">
        <div class="col-auto">
          <div class="form-floating">
            <select class="form-select" v-model="linkToAdd.subscription" required>
              <option :value="s.id" v-for="s in subscriptions">{{ s.name }}</option>
            </select><label>Подписка</label>
          </div>
        </div>
        <div class="col-auto">
          <div class="form-floating">
            <select class="form-select" v-model="linkToAdd.option" required>
              <option :value="o.id" v-for="o in options">{{ o.name }}</option>
            </select><label>Опция</label>
          </div>
        </div>
        <div class="col-auto"><button class="btn btn-primary h-100">Добавить</button></div>
      </div>
    </form>

    <div v-for="item in links" :key="item.id" class="d-flex align-items-center mb-2">
      <div class="flex-grow-1">{{ subsById[item.subscription]?.name }} — {{ optsById[item.option]?.name }}</div>
      <button class="btn btn-success me-2" @click="onEditClick(item)" data-bs-toggle="modal" data-bs-target="#editLinkModal"><i class="bi bi-pen-fill"></i></button>
      <button class="btn btn-danger" @click="onRemoveClick(item)"><i class="bi bi-x"></i></button>
    </div>

    <div class="modal fade" id="editLinkModal" tabindex="-1">
      <div class="modal-dialog"><div class="modal-content">
        <div class="modal-header"><h1 class="modal-title fs-5">Редактировать</h1><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
        <div class="modal-body">
          <div class="form-floating mb-3">
            <select class="form-select" v-model="linkToEdit.subscription" required><option :value="s.id" v-for="s in subscriptions">{{ s.name }}</option></select><label>Подписка</label>
          </div>
          <div class="form-floating mb-3">
            <select class="form-select" v-model="linkToEdit.option" required><option :value="o.id" v-for="o in options">{{ o.name }}</option></select><label>Опция</label>
          </div>
        </div>
        <div class="modal-footer"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button><button data-bs-dismiss="modal" type="button" class="btn btn-primary" @click="onUpdate">Сохранить</button></div>
      </div></div>
    </div>
  </div>
</template>