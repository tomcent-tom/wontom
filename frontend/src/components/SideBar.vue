<template>
  <div id="SideBar">
    <ul id="slide-out" class="sidenav sidenav-fixed">
      <li class="center-align">
        <img class="responsive-img" src="../assets/logo.png" />
        <h5>Wontom</h5>
        <div class="divider"></div>
      </li>
      <li>
        <router-link to="/">Home</router-link>
      </li>
      <li>
        <router-link to="/tennis">Tennis</router-link>
      </li>
      <li>
        <router-link to="/about">About</router-link>
      </li>
    </ul>
    <a href="#" data-target="slide-out" class="sidenav-trigger">
      <i class="material-icons">menu</i>
    </a>
  </div>
</template>

<script>
export default {
  name: "SideBar"
};
</script>
