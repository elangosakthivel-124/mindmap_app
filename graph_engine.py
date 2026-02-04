from graphviz import Digraph
import uuid

def create_mindmap(topic, keywords):

    dot = Digraph()

    dot.node(topic, topic)

    for word in keywords:
        dot.node(word, word)
        dot.edge(topic, word)

    filename = f"static/maps/{uuid.uuid4()}"

    dot.render(filename, format="png")

    return filename + ".png"
