"""
graph.py — Build and compile the Order Assistant LangGraph StateGraph.

Graph topology (conditional edges shown as dashed):
    START → orchestrator ─ ─ ─ ┬─ menu_agent_node ─ ─ ─ menu_tools_node ─┐
                                │       ↑________________________ ________┘
                                │       └─ ─ ─ ─ → synthesizer_node → END
                                │
                                └─ order_agent_node ─ ─ ─ order_tools_node ─┐
                                        ↑___________________________________┘
                                        └─ ─ ─ ─ → synthesizer_node → END

    Orchestrator dispatches agents conditionally via Send().
    Each agent uses a conditional edge to route to its tools node
    or directly to the synthesizer.

HITL:
    order_agent_node uses interrupt() to pause execution when the user
    query is missing an order ID / tracking ID / email.  The caller
    resumes with Command(resume=<user_input>).
"""

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from IPython.display import display, Image

from src.state import OrderState
from src.agents import (
    orchestrator_node,
    menu_agent_node,
    menu_tools_node,
    should_continue_menu,
    order_agent_node,
    order_tools_node,
    should_continue_order,
    synthesizer_node,
)
from src.logger import setup_logger

logger = setup_logger("order.graph")


def build_graph():
    """Construct, compile, and return the Order Assistant graph."""

    builder = StateGraph(OrderState)

    # ── Nodes ───────────────────────────────────────────────
    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("menu_agent_node", menu_agent_node)
    builder.add_node("menu_tools_node", menu_tools_node)
    builder.add_node("order_agent_node", order_agent_node)
    builder.add_node("order_tools_node", order_tools_node)
    builder.add_node("synthesizer_node", synthesizer_node)

    # ── Edges ───────────────────────────────────────────────

    # START → orchestrator (fixed)
    builder.add_edge(START, "orchestrator")
    # orchestrator → agent(s) routing handled via Command + Send()

    # LangGraph defaults to a recursion limit of 25
    
    # Menu agent: conditional → tools (loop) or synthesizer
    builder.add_conditional_edges(
        "menu_agent_node",
        should_continue_menu,
        {"menu_tools_node": "menu_tools_node", "synthesizer_node": "synthesizer_node"},
    )
    builder.add_edge("menu_tools_node", "menu_agent_node")

    # Order agent: conditional → tools (loop) or synthesizer
    builder.add_conditional_edges(
        "order_agent_node",
        should_continue_order,
        {"order_tools_node": "order_tools_node", "synthesizer_node": "synthesizer_node"},
    )
    builder.add_edge("order_tools_node", "order_agent_node")

    # Synthesizer → END (fixed)
    builder.add_edge("synthesizer_node", END)

    # ── Compile with memory ─────────────────────────────────
    memory = MemorySaver()
    graph = builder.compile(checkpointer=memory)

    logger.info("Order graph compiled")
    return graph

if __name__ == "__main__":
    agent = build_graph()
    # Generate the PNG data
    png_data = agent.get_graph().draw_mermaid_png()

    # Save it to a file
    with open("graph.png", "wb") as f:
        f.write(png_data)

    # Optionally display it in a notebook
    display(Image(filename="graph.png"))