<template>
  <div id="app">
    <header>
    <div class="navbar-fixed">
      <nav>
        <div class="nav-wrapper" >
          <h5 class="heading">{{heading}}</h5>
          <ul class="right hide-on-med-and-down">
            <li>
              <a href="#">demo1</a>
            </li>
            <li>
              <a href="#">demo2</a>
            </li>
          </ul>
        </div>
      </nav>
    </div>
    </header>
    <aside>
    <SideBar></SideBar>
    </aside>
    <main>
    <router-view />
    </main>
  </div>
</template>

<script>
// @ is an alias to /src
import SideBar from "@/components/SideBar.vue";
export default {
  components: {
    SideBar
  },
  computed: {
  heading: function () {
    return this.$route.name
  }
}
};
</script>

<style>

.heading {
  padding-left: 30px;
  text-transform: capitalize;
}

header,
main,
footer {
  padding-left: 300px;
}

@media only screen and (max-width: 992px) {
  header,
  main,
  footer {
    padding-left: 0;
  }
}
</style>
