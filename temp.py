from uagents import Agent, Context, Model

from samp import generate_summary
 
class Message(Model):
    message: str
 
# First generate a secure seed phrase (e.g. https://pypi.org/project/mnemonic/)
SEED_PHRASE = "abc"
 
# Copy the address shown below
print(f"Your agent's address is: {Agent(seed=SEED_PHRASE).address}")
 
# Then go to https://agentverse.ai, register your agent in the Mailroom
# and copy the agent's mailbox key
AGENT_MAILBOX_KEY = "15699a3a-ea30-4b0d-9969-bb3178dcc840"
 
# Now your agent is ready to join the agentverse!
agent = Agent(
    name="alice",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)
 
story = "he Golden Egg. Once upon a time, a farmer had a goose that laid a golden egg every day. The farmer used to sell that egg and earn enough money to meet their family's day-to-day needs. One day, the farmer thought that if he could get more such golden eggs and make a lot of money and become a wealthy person."

prompt = generate_summary(story)


@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
 
    # send the response
    ctx.logger.info("Sending message to bob")
    await ctx.send(sender, Message(message=prompt))
 
if _name_ == "_main_":
    agent.run()