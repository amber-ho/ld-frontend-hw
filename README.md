# Lightdance Frontend Homeworks

## Environment setup

1. Install [uv](https://docs.astral.sh/uv/), a python project manager.

2. Setup venv

```bash
uv venv
```

3. Install dependencies

```bash
uv sync
```

To run your script, use:
```bash
uv run <script_name>
```

## HW1
#### Goal
Learn how to use asyncio and aiohttp to fetch remote resources asynchronously.

#### Tutorials
[Python asyncio 從不會到上路](https://myapollo.com.tw/blog/begin-to-asyncio/) (recommended)

[Asyncio in Python - Full Tutorial](https://youtu.be/Qb9s3UiMSTA?si=VDx9KZ7kcWxArxSK) (optional)

[Intro to async Python | Writing a Web Crawler](https://youtu.be/ftmdDlwMwwQ?si=M6CicFzyT14TadTT)(~5:58)(optional)

#### Requirements
Fetch the content of the following URLs asynchronously and save them locally in `HW1/main.py`.
- https://example.com -> example.html
- https://github.com/NTUEELightDance/LightDance-Editor/releases/latest/download/editor-blender-linux.zip -> editor-blender-linux.zip

#### Examples in lightdance editor

- Simple example: `editor-blender/client/__init__.py`
- Complicated example: `editor-blender/operators/async_core/__init__.py`.   

## HW2
#### Goal
Learn how to use async for loops and websockets to interact with websocket servers.

#### Tutorials
[Websockets](https://superfastpython.com/asyncio-websocket-clients/#websockets_Client_Library) ("websockets Client Library" section)

[Iterables and Generators](https://myapollo.com.tw/blog/python-iterable-iterator-generator/) (Optional)

[Async for Loops in Python](https://youtu.be/dEZKySL3M9c?si=VJC-iKiG2mtWbpww) (Optional)



#### Requirements
Before doing anything, update the dependencies with `uv sync`.

Start the server in `HW2/server.py` with 
```
uv run HW2/server.py
```
and complete the TODO in `HW2/client.py`, run it with 
```
uv run HW2/client.py
```

#### Examples in lightdance editor
We use async for loops to handle GraphQL subscriptions.
- `editor-blender/client/__init__.py`:  `Clients.subscribe()`

## HW3
#### Goal
Learn how to use GraphQL to interact with a GraphQL server.

#### Tutorials

[Learn GraphQL in 7 Minutes For Beginners](https://youtu.be/Zg4XIpnLWQg?si=qPQNS2Box_VlYSA8)

[Official GraphQL Tutorial](https://graphql.org/learn/)

After you understand the concepts, you can start to play with our minimal example. Run the server (after `uv sync`) in `HW3/server.py` with 
```
uv run HW3/server.py
```

The resolvers are implemented in `HW3/server.py`, but also provided in `HW3/schema.graphql` for reference. You can connect to the GraphQL server's playground at `http://localhost:5000/graphql`, you can test your queries and mutations there. For example, to say hello to server, use the query
```graphql
query {
  hello
}
```
without any variables. Or if you want to increment the counter in server, use the mutation
```graphql
mutation($increment: Int) {
  count(increment: $increment)
}
```
with variables
```json
{
  "increment": 1
}
```
The variables will be plugged into the query/mutation at runtime, where there is a doller sign ($) before the variable name.
#### Requirements

Complete the TODO in `HW3/client.py`, run it with 
```bash
uv run HW3/client.py
```

#### Examples in lightdance editor

Almost all the interactions with the server are done with GraphQL queries and mutations. You can start from `editor-blender/schemas/[queries | mutations | subscriptions].py`, and see how these gql(...) objects are used throughout the entire project. Also you might want to check out the backend schemas in `editor-server/schema.graphql` and the resolvers written in _**Rust**_  in `editor-server/src/graphql`.
