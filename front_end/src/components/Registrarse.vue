const newLocal=this;
<template lang="html">
  <div class="container signup" id="content">
    
      <div class="row p-4">
        <div class="col-md-10 col-lg-5 mx-auto">
          <div class="card shadow-lg bg-white">
            <div class="card-header">
              <h2>Sign Up</h2>
            </div>
            <div class="card-body">
              <form v-on:submit.prevent="register">
             
                <div class="form-group">
                  <input type="text" v-model="user.nombre" class="form-control" placeholder="First Name">
                </div>
                <div class="form-group">
                  <input type="text" v-model="user.lastname" class="form-control" placeholder="Last Name">
                </div>
                
                <div class="form-group">
                  <input type="text" v-model="user.email" class="form-control" placeholder="Email">
                </div>
              
                <div class="form-group">
                  <input type="password" v-model="user.passw" class="form-control" placeholder="Password">
                </div>
                <div class="form-group">
                  <input type="password" v-model="user.passConf" class="form-control" placeholder="Password Confirmation">
                </div>
                <div class="form-group">
                  <button class="btn btn-success btn-block">Register</button>
                </div>
              </form>
            </div>
          </div>
        </div>

      </div>
    </div>
</template>

<script>
import Vue from 'vue';
import Vuex from 'vuex';
import Home from '@/components/Home.vue'
import sawl from 'sweetalert'
import { mapGetters, mapMutations} from 'vuex'


export default {

  data(){
    return{
      user: {
       
        nombre: null,
        lastname: null,
      
         passw: null,
        passConf: null,
        email: null,
       
        
       
        
      },
      err: false
    }
  },computed:{
      ...mapGetters([
        'profile'
      ])
  },
  methods: {
    ...mapMutations([
      'setFieldProfilename'
    ]),
    addUser: function(){
      this.setFieldProfilename(this.user.nombre)
    },
    register(){
       if(this.validacampos()){
      this.$store.dispatch('api_register', this.user)
      .then(response => {
        this.setFieldProfilename(this.user.nombre)
        this.$router.push({path: '/'});
        sawl('Registrado de forma correcta','','success')
        
      })
      .catch(err => {
        this.err = true;
        
      })
    }},
    validacampos(){
      
      if(this.user.nombre==null || this.user.lastname==null || this.user.passw==null || this.user.email==null){

               sawl('Error Llena todos los campos por favor','','error')

        return false;
      }else{ return true;}
    },
    
  }
}


</script>

<style lang="css">
  .signup{
    margin-top: 50px;
  }
</style>