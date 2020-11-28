var express = require("express");  
var path = require("path");     
var bodyParser = require('body-parser');   
var morgan = require("morgan");  
  
  
var app = express();  
var port = 8000;  
app.use(express.static('public'));  
app.use(bodyParser.json({limit:'500mb'}));    
app.use(bodyParser.urlencoded({extended:true, limit:'5mb'}));
var mongoose = require('mongoose');

var mongoDB = 'mongodb://127.0.0.1/vendor_medicine_data';
mongoose.connect(mongoDB, {useNewUrlParser: true, useUnifiedTopology: true});

var db = mongoose.connection;

db.on('error', console.error.bind(console, 'MongoDB connection error:'));
 
   
var Schema = mongoose.Schema;
var medicine_record = new Schema({      
    medicine_name: { type: String   }                
}); 

  
var model = mongoose.model('medicine_records',medicine_record);

app.get("/api/getdata",function(req,res){   
    output = model.aggregate([
    { '$match':{"medicine_name" : "Azithral 500 Tablet"}}
    ]);


    console.log(output.output)
   });





app.listen(port,function(){   
    console.log("server start on port"+ port);  
}); 