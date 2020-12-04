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

var mongoDB = 'mongodb://127.0.0.1/vendor_medicine_data';
mongoose.connect(mongoDB, {useNewUrlParser: true, useUnifiedTopology: true});
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

var model = require('./models/medicine_record')
app.get("/api/getdata/:query",function(req,res){
  //console.log(req.params.query)     
  
  model.aggregate([
  {'$match':    {'medicine_name' :  {'$regex': req.params.query , '$options' : 'i'} }},
  {'$sort' : {'time_of_insertion':-1}},
  {'$group' : { '_id' : {'medicine_name':'$medicine_name','vendor_name' : '$vendor_name'},
    'medicine_price' : {'$first': '$medicine_price'} ,
    'time_of_insertion' : {'$first': '$time_of_insertion'},
    'medicine_manufacturer' : {'$first': '$medicine_manufacturer'},
    'medicine_composition' : {'$first': '$medicine_composition'},
    'medicine_number_of_strips' : {'$first': '$medicine_number_of_strips'},
    'medicine_url' : {'$first': '$medicine_url'}
  }}

  ]
  ,function(err,out){

      if(err){
          console.log(err);
          res.send(err);
      }
      else{
          console.log(out);
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
