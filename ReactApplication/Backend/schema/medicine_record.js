var mongoose = require('mongoose');  
var Schema = mongoose.Schema;  
var Medicine = new Schema({      
    name: { type: String   },       
    address: { type: String   },     
    email: { type: String },       
    contact: { type: String },       
},{ versionKey: false }); 