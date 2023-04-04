import express from "express";
const app = express();

app.get("/date", (req,res) => { 
    res.send(new Date())
});

app.get("/datefromfastapi", async (req, res) => {
// task get the date from fastapi
const response = await fetch("http://127.0.0.1:8000/date")
const data = await response.json();
res.send(data);


});

const PORT = 8080;
app.listen(PORT, () => console.log("Server is runing on port", PORT))