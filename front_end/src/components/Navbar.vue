<template >
<div id="navbarx">
  

<nav class="navbar navbar-expand-lg navbar-dark bg-danger">
  <div class="container">
  <a class="navbar-brand" href="/">NEUROMARKET</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="#">Opciones</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Categorias
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">

          
          <div class="container">
            <div class="row">
              <div class="col-md-4">
                <span class="text-uppercase text-black danger">Categorias</span>
                <ul class="nav flex-column">
                <li class="nav-item">
                  <a class="nav-link active" href="#">Categoria 1</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link text-black" href="#">Categoria 2</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="#">Categoria 3</a>
                </li>
              </ul>
              </div>>
              <!-- /.col-md-4  -->
              <div class="col-md-4">
                <a href="">
                  <img src="https://dummyimage.com/200x100/ccc/000&text=image+link" alt="" class="img-fluid">
                </a>
                <p class="text-white">Espacio para imagen</p>

              </div>
              <!-- /.col-md-4  -->
            </div>
          </div>
          <!--  /.container  -->


        </div>
      </li>
       <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Que estas buscando?" aria-label="">
      <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Buscar</button>
    </form>
     
       <li class="nav-item">
        
        
      </li>
       <li class="nav-item right" >
        
        <a type="b-button" class="btn btn-dark my-2 my-sm-0 text-white" href="r" >Registrarse</a>
      </li>
     
     
       <li class="nav-item right" v-if="this.TraeNombre">
        
        <a class="nav-link" href="profile" >{{profile.first_name}}</a>
      </li>
      <li class="nav-item" v-else>
        <a class="nav-link" href="login" >Login</a>
      </li>
     
    </ul>
   
  </div>
    
</div>
</nav>
  

</div>
</template>

<script>


import Cartas from '@/components/Cartas.vue'

import { mapGetters, mapMutations} from 'vuex'
export default {

  data(){
    return{

    }
  },
components:{
  Cartas,
 
},
computed:{
...mapGetters([
  'profile'
]),
  TraeNombre(){
    if(this.profile.first_name==""){
      return false
    }else{return true}
    
}
}}

</script>

<style scoped>

#navbarx{
    position: fixed;
    top: 0%;
    left: 0;
    width: 100%;
}
/* adds some margin below the link sets  */
.navbar .dropdown-menu div[class*="col"] {
   margin-bottom:1rem;
}

.navbar .dropdown-menu {
  border:none;
  background-color: #343a40!important;
}

/* breakpoint and up - mega dropdown styles */
@media screen and (min-width: 600px) {
  
  /* remove the padding from the navbar so the dropdown hover state is not broken */
.navbar {
  padding-top:0px;
  padding-bottom:0px;
}

/* remove the padding from the nav-item and add some margin to give some breathing room on hovers */
.navbar .nav-item {
  padding:.5rem .5rem;
  margin:0 .25rem;
  color:blue
}

/* makes the dropdown full width  */
.navbar .dropdown {position:static;}

.navbar .dropdown-menu {
  width:100%;
  left:0;
  right:0;
/*  height of nav-item  */
  top:45px;
  
  display:block;
  visibility: hidden;
  opacity: 0.9;
  transition: visibility 0s, opacity 0.3s linear;
  
}
  
 

  
  /* shows the dropdown menu on hover */
.navbar .dropdown:hover .dropdown-menu, .navbar .dropdown .dropdown-menu:hover {
  display:block;
  visibility: visible;
  opacity: 2;
  transition: visibility 0s, opacity 0.3s linear;
}
  
  .navbar .dropdown-menu {
    border: 1px solid rgba(0,0,0,.15);
    background-color: #fff;
  }

}

a{
color:blue
}



</style>
