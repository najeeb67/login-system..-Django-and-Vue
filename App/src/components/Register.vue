<template>
  <div class="container">
    <div class="Register-form">
      <h1>Register Form</h1>
      <form @submit.prevent="submitForm">
        <input type="name" v-model="formData.name" name="name" placeholder="Enter Your Name" required>
        <input type="email" v-model="formData.email" name="email" placeholder="Enter Your Email" required>
        <input type="password" v-model="formData.password" name="password" placeholder="Enter Your Password" required>
        <input type="password" v-model="formData.confirmPassword" name="confirmPassword" placeholder="Confirm Password" required>
        <button type="submit">Register</button>
      </form>
      <p>Already have an account? <router-link to="/">Login</router-link></p>
      <p v-if="RegisterError" class="error-message">{{ RegisterError }}</p>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Register',
    data() {
        return {
            formData: {
                name: '',
                email: '',
                password: '',
                confirmPassword:''
            },
            RegisterError: ''
        };
    },
    methods: {
        submitForm() {
            if (this.formData.password !== this.formData.confirmPassword) {
                this.RegisterError = "password do not match.";
                return;
            }
            this.RegisterError = '';
            console.log('From data:', this.formData)
            this.resetForm()
        },
        resetForm() {
            this.formData.name = '';
            this.formData.email = '';
            this.formData.password = '';
            this.formData.confirmPassword = '';
        }
    }
}
</script>

<style scoped>

.container{
  display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
    margin: 0;
    padding: 0;
}

.Register-form{
  background-color: rgb(231, 226, 226);
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    width: 100%;
    text-align: center; 
}

.Register-form h1{
    color: #333;
    margin-bottom: 20px;
}

.Register-form form{
    text-align: center;
}

.Register-form input[type='name'],
.Register-form input[type='email'],
.Register-form input[type='password'],
.Register-form input[type='confirmPassword'],
.Register-form button{
    width: calc(100% - 30px); 
    margin-bottom: 20px;
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
    font-size: 16px;
}
.Register-form input[type='name'],
.Register-form input[type='email'],
.Register-form input[type='password'],
.Register-form input[type='confirmPassword']{
    background-color: #f5f5f5;
}

.Register-form button{
   background-color: #007bff;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.Register-form button:hover{
    background-color: #b8b5b5;
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