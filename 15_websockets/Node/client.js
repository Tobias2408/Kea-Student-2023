import WebSocket from "ws";

const webSocketClient = new WebSocket("ws://localhost:8000");

webSocketClient.on("open", () => {
    console.log("Connected to the server");
    webSocketClient.send("this is the message from a client in Node.js")
})