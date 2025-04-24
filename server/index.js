import express from "express";
import cors from 'cors'
import {adminroute} from "./routes/adminroute.js";

const app = express()
app.use(cors())
app.use(express.json())
app.use('/auth', adminroute)


app.listen(800, () => {
    console.log("The server is running")
})