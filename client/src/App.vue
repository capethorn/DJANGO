<template>
  <div class="container mt-3">
    <div class="mb-4 d-flex flex-wrap gap-2">
    </div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#"></a>
    
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Переключатель навигации">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarNav">
      <router-link class="btn btn-outline-primary" to="/subscription">Подписки</router-link>
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link class="btn btn-outline-primary" to="/option">Опции</router-link>
        </li>
        <li class="nav-item">
          <router-link class="btn btn-outline-primary" to="/option-to-subscription">Связи Подписка-Опция</router-link>
        </li>
        <li class="nav-item">
          <router-link class="btn btn-outline-primary" to="/appointment-coach">Тренеры</router-link>
        </li>
        <li class="nav-item">
         <router-link class="btn btn-outline-primary" to="/appointment-group">Групповые</router-link>
        </li>
        <li class="nav-item">
         <router-link class="btn btn-outline-primary" to="/additionally">Доп. услуги</router-link>
        </li>
         <li class="nav-item">
         <router-link class="btn btn-outline-primary" to="/addres">Адреса</router-link>
        </li>
        <li class="nav-item">
         <router-link class="btn btn-outline-primary" to="/appointment-to-group">Записи на групповые занятия</router-link>
        </li>
      </ul>

      <ul class="navbar-nav">
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Пользователь
            </a>
            <ul class="dropdown-menu">
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