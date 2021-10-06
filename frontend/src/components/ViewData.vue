<template>
<div >
  <b-navbar toggleable type="dark" variant="dark">
    <b-navbar-brand class="nav-bar">LinkedIn DataSet</b-navbar-brand>
    <b-navbar-nav class=ml-auto>
        <b-nav-item class="link" href="/">Add</b-nav-item>
    </b-navbar-nav>
  </b-navbar>

    <div id="first">
      <table class="table table-hover">
                <tr>
                  <th scope="col">Company</th>
                  <th scope="col">Designation</th>
                  <th scope="col">Review</th>
                </tr>
              <tbody>
               
                  <tr v-for="(data, index) in data" :key="index">
                  <td class="td1">{{ data.company }}</td>
                  <td class="td2">{{ data.designation }}</td>
                  <td class="td2">{{ data.review }}</td>
                  <td>
                  <b-button pill class="ibutton" variant="outline-danger"  @click="onDeleteData(data)">Delete</b-button>
                  </td>   
                  <td>               
                  <b-button pill class="ibutton" variant="outline-success"  v-b-modal.edit-update-modal @click="editData(data)">Update</b-button>
                  </td>
                
                </tr>
              </tbody>
    </table>
    <b-modal ref="editDataModal" id="edit-update-modal" title="Update" hide-footer>
      <div class="updateContainer">
       <b-form @submit.prevent="updatesubmit">
        <b-form-group 
        id="input-12"
        label="Enter the Name"
        label-for="input-1"
        
       >
      <b-form-input
          id="input-1"
          type="String"
          v-model="editentry.name[0]"
          placeholder="Name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-12" label="About" label-for="input-2">
        <b-form-textarea
          id="input-2"
          type="text"
          v-model="editentry.about"
          placeholder="Type About"
          rows=8
        ></b-form-textarea>
      </b-form-group>
    <b-button pill v-on:Click.stop="updatesubmit" id="button-2" type="submit" variant="dark">Update</b-button>
     
  </b-form>
  </div>
    </b-modal>
    
    
    
  </div>    
    </div>
    
</template>


<script>
import axios from 'axios';
export default {
    data(){
        return{
            
            data: [],
            editentry:{
              _id:"",
              name:"",
              about:"",

            },
        };
        

    },
    
    methods:{
     
        getData(){
          
           const path = 'http://127.0.0.1:5000/view';
            axios.get(path)
             .then((res) => {
                 this.data = res.data;
                 
             })
             .catch((error) => {
                 console.error(error);
             });
        },
        onDeleteData(data){
          
          const finalData = JSON.parse(JSON.stringify(data));
          this.removeData(finalData._id)
        },
        removeData(dataid){
         
         const path = 'http://127.0.0.1:5000/view/'+dataid.$oid;
         console.log(path)
         axios.delete(path).then(()=>{
           console.log("deleted")
           this.getData();
         })
         .catch(error => {
           console.log(error);
           this.getData();
         })
        },
        editData(data){
          this.editentry = data;
        
        },
        updatesubmit(){
          const finalData = JSON.parse(JSON.stringify(this.editentry));
          console.log(this.editentry)
          const id=finalData._id.$oid
         
          const path = 'http://127.0.0.1:5000/dataview/'+id;
          axios.put(path,{
            name:this.editentry.name[0],
            about:this.editentry.about,
          })
          .then(()=>{
            this.getData();
          })
          .catch(error =>{
            console.error(error);
            this.getData();
          })
        }
       
    },
    created(){
           
            this.getData();
        },
    
}
</script>

<style>

#first{
margin-right: 25px;
margin-left: 25px;
}


#input-12{
 align-content: center;
 width:100%;
 padding-left:20px;
 font-weight:bold;
  
}
#button-2{
  align-content: center;
  margin-left:40%;
}

.nav-bar{
  padding-left: 50px;;
}
.link{
  padding-right:100px;
  font-size: 20px;
 
}
.td1{
  width:15%;
}
.td2{
  width:70%;
  
}
</style>
