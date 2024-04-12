

from samp import generate_summary
from uagents import Agent, Context, Model


class Message(Model):
    message: str

SEED_PHRASE = "abc"

AGENT_MAILBOX_KEY = "15699a3a-ea30-4b0d-9969-bb3178dcc840"

agent = Agent(
    name="alice",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)

@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    
    # Extract the story from the incoming message
    story = msg.message

    # Generate summary based on the received story
    summary = generate_summary(story)

    # Log the summary
    ctx.logger.info(f"Generated summary: {summary}")

    # Send the summary as a response
    ctx.logger.info("Sending summary to sender")
    await ctx.send(sender, Message(message=summary))

if _name_     == "main":
    agent.run()