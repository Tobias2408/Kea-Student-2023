import { WebSocketServer } from "ws";

const server = new WebSocketServer({port: 8000});

server.on("connection", (ws) => {
    console.log("New connection", server.clients.size);

    ws.on("message", (message) => {
        console.log("recived message: " + message);
        server.clients.forEach(client => {
            client.send('a message was sent: '+ message)
        });
    })
});