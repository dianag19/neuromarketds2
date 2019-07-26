<template>
    <div class="home">
      
            <Cartas></Cartas>
      
           <router-view/>
       
         
    </div>
   
</template>
<script>

import { mapGetters} from 'vuex'
import Cartas from '@/components/Cartas.vue'
import Navbar from '@/components/Navbar.vue'
export default {
    
    name: 'home',
    components: {
        Cartas,Navbar
    },
    computed:{
        ...mapGetters([
            'getProducts'
        ]),
        traerProducts(){
            return this.getProducts
        }
    }
}
</script>
<style>

</style>
