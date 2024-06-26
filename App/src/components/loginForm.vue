<template>
  <div class="container">
    <div class="login-form">
      <h1>Login</h1>
      <form @submit.prevent="submitForm">
        <input v-model="name" type="name" name="name" placeholder="Enter Your Name" />
        <input
          type="email"
          v-model="email"
          name="email"
          placeholder="Enter Your email"
          required
        />
        <input
          type="password"
          v-model="password"
          name="password"
          placeholder="Enter Your Password"
          required
        />
        <button type="submit">Login</button>
      </form>
      <p>Don't have an account? <router-link to="/register">Register</router-link></p>
      <p v-if="loginError" class="error-message">{{ loginError }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      email: "",
      password: "",
      loginError: "",
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await fetch("http://localhost:8000//login/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || "Login failed");
        }

        alert("Login Successful!");
        this.loginError = "";
      } catch (error) {
        this.loginError = error.message;
      }
    },
  },
};
</script>
<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  margin: 0;
  padding: 0;
}

.login-form {
  background-color: rgb(231, 226, 226);
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
  text-align: center;
}

.login-form h1 {
  color: #333;
  margin-bottom: 20px;
}

.login-form form {
  text-align: center;
}
.login-form input[type="name"],
.login-form input[type="email"],
.login-form input[type="password"],
.login-form button {
  width: calc(100% - 30px);
  margin-bottom: 20px;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
  font-size: 16px;
}
.login-form input[type="name"],
.login-form input[type="email"],
.login-form input[type="password"] {
  background-color: #f5f5f5;
}

.login-form button {
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-form button:hover {
  background-color: #0056b3;
}

p {
  margin-top: 20px;
  font-size: 14px;
  color: #666;
}

p a {
  color: #007bff;
  text-decoration: none;
  transition: color 0.3s ease;
}

p a:hover {
  color: #0056b3;
}

.error-message {
  color: red;
}
</style>
