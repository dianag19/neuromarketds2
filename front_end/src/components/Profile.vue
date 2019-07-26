
<template>
    <div class="container">
        <div class="row text-left">
            <div class="col-md-6">
                <h1>Nombre de usuario:{{profile.first_name}}</h1>
            </div>
        </div>
        <form v-on:submit.prevent="deleteUser">
        <button class="btn btn-danger">Logout</button>
        
        </form>

    </div>
</template>

<script>
import { mapGetters, mapMutations, mapState} from 'vuex'
import sawl from 'sweetalert'

export default {
    computed:{
        ...mapGetters([
            'profile'
        ]),
    },
    methods:{
        ...mapMutations([
            'setFieldProfilename'
        ]),
        deleteUser: function(){
            this.setFieldProfilename("");
            sawl('Usted cerro su sesion','','success')
             this.$router.push({path: '/'});
        }
    }
}
</script>
<style>

</style>