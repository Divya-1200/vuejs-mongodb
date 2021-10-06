import Vue from 'vue';
import VueRouter from 'vue-router';
import Frontview from '../components/Frontview.vue';
import ViewData from '../components/ViewData.vue';

Vue.use(VueRouter);

export default new VueRouter({
    mode:'history',
    routes:[
        {
            path:'/',
            name:'Frontview',
            component: Frontview,
        },
        {
            path:'/view',
            name:'ViewData',
            component: ViewData,
        },

            
    ],
})