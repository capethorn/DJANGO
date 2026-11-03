<template>
  <div class="container mt-3">
    <nav class="navbar navbar-expand-lg bg-body-tertiary mb-4">
  <div class="container-fluid">
     <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
           <li class="nav-item">
            <router-link class="nav-link" active-class="active" to="/subscription">Подписки</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" to="/option">Опции</router-link>
         </li>
          <li class="nav-item">
            <router-link class="nav-link" active-class="active" to="/option-to-subscription">Связи Подписка-Опция</router-link>
          </li>
          <li class="nav-item">
           <router-link class="nav-link" active-class="active" to="/appointment-coach">Тренеры</router-link>
         </li>
         <li class="nav-item">
            <router-link class="nav-link" active-class="active" to="/appointment-group">Групповые</router-link>
         </li>
          <li class="nav-item">
          <router-link class="nav-link" active-class="active" to="/additionally">Доп. услуги</router-link>
           </li>
          <li class="nav-item">
             <router-link class="nav-link" active-class="active" to="/addres">Адреса</router-link>
           </li>
          <li class="nav-item">
             <router-link class="nav-link" active-class="active" to="/appointment-to-group">Записи на групповые</router-link>
          </li>
        </ul>
         <ul class="navbar-nav">
           <li class="nav-item dropdown">
             <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
               Пользователь
             </a>
            <ul class="dropdown-menu dropdown-menu-end">
             <li><a class="dropdown-item" href="/admin">Админка</a></li>
          </ul>
        </li>
      </ul>
      </div>
    </div>
    </nav>
    
    <router-view></router-view>
  </div>
</template>