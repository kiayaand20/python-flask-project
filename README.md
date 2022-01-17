# Project Overview

## Project Name

<h3>Python and Flask Project</h3>

## Description

This project consists of utilizing a dataset to create an API using Python, Flask, and SQL.

## API & Data Sample

The URL below was used as the sample dataset to create the API.

URL: https://api.imgflip.com/get_memes

```
"memes": [
    {
      "id": "181913649",
      "name": "Drake Hotline Bling",
      "url": "https://i.imgflip.com/30b1gx.jpg",
      "width": 1200,
      "height": 1200,
      "box_count": 2
    }
  ]
```

## MVP

- The API and Routes will run without errors
- The API will be built in Python and Flask, using a SQL database with PeeWee models
- Contain at least one model

## Code Snippet

```
{
  "box_count": 2,
  "height": 1200,
  "id": 1,
  "name": "Drake Hotline Bling",
  "url": "https://i.imgflip.com/30b1gx.jpg",
  "width": 1200
}
```

```
{
  "Error": "Name not found"
}
```

## Route List

Routes, or end points, were created to connect users to specific items in the API. For instance, when the user types '/memes/1', the browser will reflect the GET request, only providing the user with the item where the id = 1. The routes are home, id, name, width, height, and box count. See below:

<strong>List of Routes:</strong>

- Home Route - /memes
- ID Route - /memes/<<id>id>
- Name Route - /memes/name/<<name>name>
- Width Route - /memes/width/<<name>width>
- Height Route - /memes/height/<<height>height>
- Box count Route - /memes/box_count/<<name>box_count>
