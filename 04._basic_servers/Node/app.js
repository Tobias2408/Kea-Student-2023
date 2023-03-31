import express from "express";
import jsonData from "../../02._data_formats/me.json" assert {type: "json"};
import  {XMLParser}  from 'fast-xml-parser'; 
import {readFileSync, createReadStream}  from 'fs';
import yaml from 'yaml'
import csv from 'fast-csv'
   
const app = express();

// xml read
const xmlFile = readFileSync("../../02._data_formats/me.xml", 'utf8');
const parser = new XMLParser(); 
const xmlData = parser.parse(xmlFile);


// yaml read 
const yamlFile = readFileSync("../../02._data_formats/me.yaml", 'utf8');

const yamlData = yaml.parse(yamlFile);

// read text
const textFile = readFileSync("../../02._data_formats/me.txt", 'utf8');

// read csv
const csvData = []
createReadStream("../../02._data_formats/me.csv",)
  .pipe(csv.parse({ headers: true }))
  .on('error', error => console.error(error))
  .on('data', row => csvData.push(row));
  



app.get("/",async (req,res) => {
    res.send({message: "data"});
}); 


app.get("/json",async (req,res) => {
    res.send({message: jsonData});
}); 

app.get("/xml",async (req,res) => {

    res.send({message: xmlData});
}); 

app.get("/yaml",async (req,res) => {

    res.send({message: yamlData});
}); 


app.get("/text",async (req,res) => {

    res.send( textFile);
}); 

app.get("/csv",async (req,res) => {

    res.send({message: csvData});
}); 


app.get("/MeFromJsonStringPython", async (req, res) => {
    // task get the date from fastapi
    const response = await fetch("http://127.0.0.1:8000/json")
    const data = await response.json();
    res.send(data);
    
    
    });

app.listen(8080, () => console.log("Server is running on port", 8080));


