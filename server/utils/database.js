import mysql from 'mysql'

const connection = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "",
    database: "company_employee_data"
})

connection.connect(function(err){
    if(err){
        console.log("connection error")
    } else {
        console.log("Connected")
    }
})