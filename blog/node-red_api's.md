# Node-red API: Sprach-Emoji-Übersetzer

[Node-RED Flow API](https://node-red-gl9r.onrender.com/#flow/319ad89a013c2850)

Die Aufgabe ist es, eine Node-RED Api zu erstellen, die Text in Emojis umwandeln kann.

## Zuerst machst man auf Node-RED folgenden Flow:

![image](https://user-images.githubusercontent.com/111581501/227553920-0d4e83f5-94e9-4616-b93c-a512dff5f93b.png)


- Die Einstellungen für den *https in*-Block muss so aussehen:

![image](https://user-images.githubusercontent.com/111581501/227555202-ea923f19-0bc8-4196-a393-616bc721a920.png)

Es ist eine **GET**-Request: Die API soll also dem Client etwas rausgeben.



- Im Funktionsblock kommt das Programm, dass der Text, der der Client der API weitergibt, in ein vordefiniertes Emoji austauscht.

```
let emoji = msg.payload.text;

emoji = emoji.replace(/hello/, '👋');

msg.payload = {
    msg: emoji
};

return msg;
```

## Postman: Anfrage schicken

Dazu musst du eine **GET**-Request an die http-Seite schicken. Das muss dann so aussehen:

![image](https://user-images.githubusercontent.com/111581501/227559454-59aa19ea-33a4-4dc7-a9ae-f134bec3a3b9.png)

