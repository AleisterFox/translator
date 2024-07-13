# Documentación de la API de Traducción

## Descripción General

Esta API permite traducir texto de un idioma a otro utilizando el servicio de Google Translate.

## Endpoints

### POST /traducir

Traduce el texto enviado en la solicitud de un idioma de origen a un idioma de destino.

#### URL

`/traducir`

#### Método HTTP

`POST`

# Solicitud

##### Cuerpo de la Solicitud (JSON)

```json
{
  "idioma_origen": "codigo_idioma_origen",
  "idioma_destino": "codigo_idioma_destino",
  "texto": "texto_a_traducir"
}
```

#### Parámetros de la solicitud

- `idioma_origen` (string): Código del idioma de origen (por ejemplo, "en" para inglés, "es" para español).
- `idioma_destino` (string): Código del idioma de destino.
- `texto` (string): El texto que se desea traducir.

# Respuesta

#### Cuerpo de la respuesta (JSON)

```json
{
  "texto_traducido": "texto_traducido"
}
```

#### Parámetros de la respuesta

- `texto_traducido` (string): El texto traducido al idioma de destino

#### Ejemplo de solicitud

````
curl -X POST http://<tu-dominio>/traducir -H "Content-Type: application/json" -d '{
  "idioma_origen": "en",
  "idioma_destino": "es",
  "texto": "Hello, world!"
}'

```

#### Ejemplo de respuesta 

````json
{
  "texto_traducido": "Hola, mundo!"
}

````

