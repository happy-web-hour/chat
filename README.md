# Chat
## APIs
- GET /chat/{roomId} - retorna todas as mensagens da sala 

**Request**	

**Response**
200
```json 
[
	{
		"messageId": "string",
		"userId": "string",
		"message": "string",
		"timestamp": "string",
		"type": "string"
	}
]
```

- GET /chat/{roomId}/{messageId} - retorna todas as mensagens a partir do messageId

**Request**	

**Response**
200
```json 
[
	{
		"messageId": "string",
		"userId": "string",
		"message": "string",
		"timestamp": "string",
		"type": "string"
	}
]
```	
- POST /chat/{roomId}/{userId} - envia mensagem

**Request**	
```json 
{
	"userId": "string",
	"message": "string"
}
```

**Response**
200
```json 
{
	"messageId": "string",
	"userId": "string",
	"message": "string",
	"timestamp": "string",
	"type": "string"
}
```

- UPDATE /chat/{roomId}/{userId} - adiciona usuário na sala  

**Request**	

**Response**
200

- DELETE /chat/{roomId}/{userId} - remove usuário na sala  

**Request**	

**Response**
200

- DELETE /chat/{roomId}/ - apaga a sala

**Request**	

**Response**
200

## Database
```json
[
	{
		"roomId":"string",
		"messages": [
			{
				"messageId": "string",
				"userId": "string",
				"message": "string",
				"timestamp": "string",
				"systemMessage": "boolean"
			}	
		]
	}
]
```