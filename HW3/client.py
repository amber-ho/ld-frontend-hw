import asyncio
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

QUERY_HELLO = gql(
    """
    query {
        hello
    }
    """
)

QUERY_ECHO = gql(
    """
    query($text: String!) {
        echo(text: $text)
    }
    """
)

MUT_COUNT = gql(
    """
    mutation($increment: Int!) {
        count(increment: $increment)
    }
    """
)


async def main():
    transport = AIOHTTPTransport(url="http://localhost:5000/graphql")
    client = await Client(transport=transport).connect_async()

    # Example 1: query without variables
    result = await client.execute(QUERY_HELLO)
    print(result)

    # Example 2: query with variables
    result = await client.execute(
        QUERY_ECHO, variable_values={"text": "Hello again from client!"}
    )
    print(result)

    # Example 3: mutation
    result = await client.execute(MUT_COUNT, variable_values={"increment": 5})
    print(result)

    # TODO start
    # Try to get the subgroups of the "software" group defined in the server
    # Hint: This is more similar to example 2

    # end

    await client.client.close_async()


if __name__ == "__main__":
    asyncio.run(main())
