var mongoose = require('mongoose');  


var Schema = mongoose.Schema;
var medicine_record = new Schema({      
    medicine_name: { type: String   }                
}); 

module.exports = mongoose.model('medicine_records',medicine_record);