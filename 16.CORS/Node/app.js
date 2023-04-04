import express from "express";
const app = express();

import cors from "cors";

app.use(cors());


app.get("/timestamp", (req,res) => {
    res.send(new Date());
});

app.listen(8080, () => console.log("sever is running on", 8080));