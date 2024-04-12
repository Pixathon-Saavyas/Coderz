from uagents import Agent, Context, Model
from samp import generate_summary

class Message(Model):
    message: str

# First generate a secure seed phrase (e.g. https://pypi.org/project/mnemonic/)
SEED_PHRASE = "mnop"

# Copy the address shown below
print(f"Your agent's address is: {Agent(seed=SEED_PHRASE).address}")

# Then go to https://agentverse.ai, register your agent in the Mailroom
# and copy the agent's mailbox key
AGENT_MAILBOX_KEY = "2276a66f-5ad9-4e6b-82cf-1207de85423c"

# Now your agent is ready to join the agentverse!
agent = Agent(
    name="alice",
    seed=SEED_PHRASE,
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)

story = "The Golden Egg. Once upon a time, a farmer had a goose that laid a golden egg every day. The farmer used to sell that egg and earn enough money to meet their family's day-to-day needs. One day, the farmer thought that if he could get more such golden eggs and make a lot of money and become a wealthy person."

prompt = generate_summary(story)

@agent.on_message(model=Message, replies={Message})
async def handle_message(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

    # send the response
    ctx.logger.info("Sending message to bob")
    await ctx.send(sender, Message(message=prompt))

if __name__ == "__main__":
    print("Attempting to establish connection...")
    agent.run()
    print("Connection established successfully.")
