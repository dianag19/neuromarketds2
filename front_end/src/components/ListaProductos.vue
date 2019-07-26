<template >
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado productos</h2>
                <div class="col-md-12">
                <b-table striped hover :items="productos" :fields="fields">
                    </b-table>
                </div>
                </div>
                </div>
                </div>
</template>

<script >
import axios from "axios";
import { mapGetters, mapMutations} from 'vuex'
export default{
data (){
    return{
        fields: [
            {key: 'nombre_producto', label:'Nombre'},
            {key: 'id_productos', label: 'Id_productos'},
            {key: 'cantidad_producto', label:'Cantidad'},
        ],
        productos :[]
    }
},computed:{
        ...mapGetters([
            'getProducts'
        ]),
        traeP(){
            return this.getProducts
        }
    },
methods:{
        ...mapMutations([
            'setProducts'
        ]),
        getProductos(){
            const path =  'http://localhost:8000/api/v1.0/producto/'
            axios.get(path).then((response)=>{
                this.productos = response.data
                alert(response.data[1])
                this.setProducts(response.data)
                console.log(this.getProducts[0].nombre_producto)
            }).catch((err)=>{
                console.log(err)
                
            })
        }
    }, created(){
        this.getProductos()
    },
    
}
</script>

<style>



</style>