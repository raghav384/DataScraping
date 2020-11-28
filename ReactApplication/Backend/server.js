var express = require("express");  
var bodyParser = require('body-parser');   
var morgan = require("morgan");  
var mongoose = require('mongoose');
var cors = require('cors');

var app = express();
app.use(cors());
var port = 8000;  
app.use(express.static('public'));  
app.use(bodyParser.json({limit:'500mb'}));    
app.use(bodyParser.urlencoded({extended:true, limit:'5mb'}));

var mongoDB = 'mongodb://127.0.0.1/pharmeasy_medicine_data';
mongoose.connect(mongoDB, {useNewUrlParser: true, useUnifiedTopology: true});
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
 
var Schema = mongoose.Schema;
var medicine_record = new Schema({      
    medicine_name: { type: String   }                
}); 

var model = mongoose.model('medicine_records',medicine_record);

app.get("/api/getdata",function(req,res){   
  model.find({},function(err,out){

      if(err){
          res.send(err);
      }
      else{
          res.send(out);
      }
  })
 });

app.get("/api/healthcheck",function(req,res){
    res.send("The backend server is working fine");
});

app.listen(port,function(){   
    console.log("server start on port "+ port);  
}); 