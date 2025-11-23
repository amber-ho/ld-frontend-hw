from flask import Flask
from graphql_server.flask import GraphQLView
import graphene

app = Flask(__name__)

i = 0

lightdanceGroups = {
    "software": ["frontend", "backend", "RPi", "Control"],
    "hardware": ["library", "PCB"],
    "dancers": ["dancers"],
}


class Query(graphene.ObjectType):
    hello = graphene.String(description="A simple hello world query")
    echo = graphene.String(description="A simple echo query", text=graphene.String())

    def resolve_hello(self, _):
        return "Hello world!!!"

    def resolve_echo(self, _, text: str):
        return f'I hear "{text}" from you!'

    lightdance_groups = graphene.List(
        graphene.String,
        description="Get lightdance groups by category",
        category=graphene.String(),
    )

    def resolve_lightdance_groups(self, _, category: str):
        print(f"Getting lightdance groups for category: {category}")
        return lightdanceGroups.get(category, [])


class Mutation(graphene.ObjectType):
    count = graphene.Int(
        description="A simple count mutation", increment=graphene.Int()
    )

    def resolve_count(self, _, increment: int):
        global i
        i += increment
        return i


schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    "/graphql", # entrypoint
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True
    ),
)

if __name__ == "__main__":
    app.run(debug=True) # watch for changes and restart server automatically
