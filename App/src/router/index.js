import { createRouter, createWebHistory } from "vue-router";

import loginForm from "../components/loginForm.vue"; // Adjust the path as necessary
import Register from "../components/Register.vue"; // Adjust the path as necessary

const routes = [
  {
    path: "/",
    name: "loginForm",
    component: loginForm,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
