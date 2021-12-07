<template>
  <div class="menubar card flex">
    <div
      class="flex-none flex align-items-center justify-content-center font-bold text-white bg-blue-500 m-2 px-5 py-3 border-round"
    >
      About
    </div>
    <div
      class="flex-none flex align-items-center justify-content-center font-bold text-white bg-blue-500 m-2 px-5 py-3 border-round"
    >
      About
    </div>
    <div
      class="flex-grow-1 flex align-items-center justify-content-center font-bold text-white bg-blue-500 m-2 px-5 py-3 border-round"
    >
      Welcome to the game
    </div>
    <div
      class="flex-none flex align-items-center justify-content-center font-bold text-white bg-blue-500 m-2 px-5 py-3 border-round"
    >
      Settings
    </div>
  </div>
  <div
    class="main-area"
  >
    <div class="flex flex-column card-container">
      <div
        class="flex align-items-center justify-content-center h-4rem
          bg-green-500 font-bold text-white border-round m-2"
      >
        1
      </div>
      <div
        class="flex align-items-center justify-content-center h-4rem
          bg-green-500 font-bold text-white border-round m-2"
      >
        2
      </div>
      <div
        class="flex align-items-center justify-content-center h-4rem
          bg-green-500 font-bold text-white border-round m-2"
      >
        3
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Menubar from "primevue/menubar";

@Options({
  components: { Menubar },
})
export default class App extends Vue {}
</script>

<style lang="scss">
@import "primeflex/primeflex.scss";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

html,
body {
  // FIXME I don't get why I can't use 100% here without a little scroll. A
  // read designer is necessary to solve problems like this.
  height: 95%;
}

#app, div.main-area {
  height: 100%;
}

div.main-area {
  @include styleclass("flex align-content-center justify-content-center flex-wrap card-container green-container");
}
</style>
