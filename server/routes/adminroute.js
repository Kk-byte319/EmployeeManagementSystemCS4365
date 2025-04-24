import express from 'express'

const router = express.Router()

router.post('/adminlogin', (request, response) => {
    console.log(request.body)
})

export {router as adminroute}