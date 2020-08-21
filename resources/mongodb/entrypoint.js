db.createCollection("chat");
db.chat.insertMany([
    {
        "roomId": "f50ec0b7-f960-400d-91f0-c42a6d44e3d0",
        "messages": [
            {
                "messageId": "bd65600d-8669-4903-8a14-af88203add38",
                "userId": "xpt5600d-8669-4903-8a14-af88203add38",
                "message": "hello world",
                "timestamp": "1597958593.263777",
                "systemMessage": false
            }
        ]
    },
    {
        "roomId": "123ec0b7-f960-400d-91f0-c42a6d44e3d0",
        "messages": []
    }
]);