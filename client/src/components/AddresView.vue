<script setup>
import { ref, onBeforeMount } from 'vue';
  import axios from 'axios';
import Cookies from 'js-cookie';

  const items = ref([]);
 const itemToAdd = ref({});
    const itemToEdit = ref({});

const AddresPictureRef = ref();
  const addresAddImageUrl = ref();
 const EditPictureRef = ref();
const editImageUrl = ref();
   const viewImageUrl = ref();

 async function fetchItems() {
   const r = await axios.get("/api/addres/");
    items.value = r.data;
  }

   onBeforeMount(() => {
 axios.defaults.headers.common['X-CSRFToken'] = Cookies.get("csrftoken");
  fetchItems();
});

   async function addresAddPictureChange() {
  addresAddImageUrl.value = URL.createObjectURL(AddresPictureRef.value.files[0]);
    }

async function editPictureChange() {
     editImageUrl.value = URL.createObjectURL(EditPictureRef.value.files[0]);
}

  async function onAdd() {
  const formData = new FormData();
    if (AddresPictureRef.value && AddresPictureRef.value.files[0]) {
       formData.append('image', AddresPictureRef.value.files[0]);
  }
 formData.set('addres', itemToAdd.value.addres);

    await axios.post("/api/addres/", formData, {
     headers: { 'Content-Type': 'multipart/form-data' }
   });

   await fetchItems();
    itemToAdd.value = {};
  addresAddImageUrl.value = null;
}

   async function onRemoveClick(item) {
    await axios.delete(`/api/addres/${item.id}/`);
  await fetchItems();
 }

 async function onEditClick(item) {
    itemToEdit.value = { ...item };
     editImageUrl.value = item.image;
}

   async function onUpdate() {
    const formData = new FormData();
  if (EditPictureRef.value && EditPictureRef.value.files[0]) {
      formData.append('image', EditPictureRef.value.files[0]);
   }
   formData.set('addres', itemToEdit.value.addres);

    await axios.put(`/api/addres/${itemToEdit.value.id}/`, formData, {
       headers: { 'Content-Type': 'multipart/form-data' }
  });
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
         <div class="col-auto" v-if="addresAddImageUrl">
          <img :src="addresAddImageUrl" style="max-height: 60px;" alt="">
        </div>
         <div class="col-auto"><button class="btn btn-primary h-100">Добавить</button></div>
      </div>
    </form>
     <div v-for="item in items" :key="item.id" class="d-flex align-items-center mb-2">
        <div class="flex-grow-1">{{ item.addres }}</div>
       <div v-show="item.image" class="me-3">
          <img :src="item.image" style="max-height: 60px; cursor: pointer;" 
             data-bs-toggle="modal" data-bs-target="#imageModal" 
             @click="viewImageUrl = item.image">
       </div>
        <button class="btn btn-success me-2" @click="onEditClick(item)" data-bs-toggle="modal" data-bs-target="#editAdrModal"><i class="bi bi-pen-fill"></i></button>
       <button class="btn btn-danger" @click="onRemoveClick(item)"><i class="bi bi-x"></i></button>
      </div>
    <div class="modal fade" id="editAdrModal" tabindex="-1">
       <div class="modal-dialog"><div class="modal-content">
         <div class="modal-header"><h1 class="modal-title fs-5">Редактировать</h1><button type="button" class="btn-close" data-bs-dismiss="modal"></button></div>
         <div class="modal-body">
           <div class="form-floating mb-3"><input type="text" class="form-control" v-model="itemToEdit.addres" required /><label>Адрес</label></div>
           <div class="mb-3">
             <input class="form-control" type="file" ref="EditPictureRef" @change="editPictureChange">
           </div>
           <div v-if="editImageUrl">
             <img :src="editImageUrl" style="max-height: 80px;" alt="">
           </div>
         </div>
         <div class="modal-footer"><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button><button data-bs-dismiss="modal" type="button" class="btn btn-primary" @click="onUpdate">Сохранить</button></div>
       </div></div>
     </div>
     <div class="modal fade" id="imageModal" tabindex="-1">
       <div class="modal-dialog modal-dialog-centered">
         <div class="modal-content">
           <div class="modal-header">
             <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
           </div>
           <div class="modal-body text-center">
             <img :src="viewImageUrl" class="img-fluid" alt="Увеличенное изображение">
           </div>
         </div>
       </div>
     </div>
   </div>
</template>