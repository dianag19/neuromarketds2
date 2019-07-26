<template lang="html">
  <div class="container login" id="content">
      
      <div class="row p-4">
        <div class="col-md-8  col-lg-4 mx-auto">
          <div class="card shadow-lg bg-white">
            <div class="card-header">
              <h2>Login</h2>
            </div>
            <div class="card-body">
              <form v-on:submit.prevent="login">
                <div class="input-group form-group">
                  
                  <input v-model="valida.cedula" type="text" class="form-control" id="inlineFormInputGroupUsername" placeholder="cedula">
                </div>
                <div class="form-group">
                  <input v-model="valida.password" type="password" name="pass" value="" class="form-control" placeholder="Password">
                </div>
                <div class="form-group">
                  <button class="btn btn-success btn-block">Entrar</button>
                </div>
               
              </form>
              <form>
                <div class="form-group">
                   <div class="form-group">
                  <button class="btn btn-primary btn-block">Facebook</button>
                </div>
                <div class="form-group">
                  <button class="btn btn-danger btn-block">Google</button>
                </div>
                  </div>
                </form>
            </div>
          </div>
        </div>

      </div>
    </div>
</template>

<script>
import sawl from 'sweetalert'
import { mapGetteres, mapMutations} from 'vuex'

export default {
  data(){
    return {

      valida: {
        cedula: null,
        password: null

      },
      err: false
    }
  },
  methods: {
     
    ...mapMutations([
      'setFieldProfilename'
    ]),
     Username(nombre){
      this.setFieldProfilename(this.user.nombre)
      alert('funciono')
    },
    login(){
      this.$store.dispatch('api_login', this.valida)
        .then(response => {
          let data = response.data
           
            if(this.valida.cedula == data.cedula){
               sawl('Bienvenido a NUEROMARKET','','success')
               this.setFieldProfilename(data.nombre)
               this.$router.push({path: '/'});
              

            }else{
                   sawl('Debe registrarse primero para poder acceder','','error')
            }
          
          //console.log(this.$store.getters.token);
        })
        .catch(err => {
          console.log(this.err);
          this.err = true;
       

        });
    }
  
 
}}
</script>

<style lang="css">
@import 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css';
  .login{
    margin-top: 100px;
  }
</style>