import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import PrimeVue from "primevue/config";

import "primeflex/primeflex.scss";
import "primeflex/themes/saga-blue.scss";

import "primeicons/primeicons.css";

/*eslint newline-per-chained-call: ["error", { "ignoreChainWithDepth": 2 }]*/
createApp(App)
    .use(router)
    .use(PrimeVue)
    .mount("#app");
