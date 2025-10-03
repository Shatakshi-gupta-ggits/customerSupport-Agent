from dotenv import load_dotenv
import os
import sys
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, RoomOutputOptions
# Ensure we only import the Silero VAD plugin; remove any references to 'hedra'
from livekit.plugins import silero
from PIL import Image

from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

# Load environment variables
load_dotenv(".env")

# Check if required environment variables are set
required_env_vars = ["PINECONE_API_KEY", "ASSISTANT_NAME", "OPENAI_API_KEY"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    print(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
    print("Available environment variables:")
    for var in required_env_vars:
        value = os.getenv(var)
        if value:
            print(f"  {var}: {'*' * 10} (set)")
        else:
            print(f"  {var}: NOT SET")
    sys.exit(1)

try:
    pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
    assistant = pc.assistant.Assistant(assistant_name=os.environ["ASSISTANT_NAME"])
    print("✅ Pinecone Assistant initialized successfully")
except Exception as e:
    print(f"❌ Failed to initialize Pinecone Assistant: {e}")
    sys.exit(1)

from livekit.agents.llm import function_tool

@function_tool
async def ask_knowledge_base(question: str) -> str:
    """Query the Pinecone Assistant knowledge base for information."""
    try:
        msg = Message(role="user", content=question)
        resp = assistant.chat(messages=[msg])
        return resp.message.content
    except Exception as e:
        return f"Sorry, I encountered an error accessing the knowledge base: {str(e)}"


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a helpful voice AI assistant.
            You eagerly assist users with their questions by providing information from your extensive knowledge.
            Your responses are concise, to the point, and without any complex formatting or punctuation including emojis, asterisks, or other symbols.
            You are curious, friendly, and have a sense of humor.""",
            tools=[ask_knowledge_base]
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        stt="assemblyai/universal-streaming:en",
        llm="openai/gpt-4.1-mini",
        tts="cartesia/sonic-2:9626c31c-bec5-4cca-baa8-f8ba9e84c8bc",
        vad=silero.VAD.load(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(),
        room_output_options=RoomOutputOptions(
            audio_enabled=True,   # Changed to True since no avatar
        )
    )

    # Send initial greeting
    await session.say("Hello! I'm your helpful assistant. How can I help you today?")
    
    print("✅ Agent is ready! Listening for user responses...")
    
    # Continuously handle user responses
    async for event in session:
        if event.type == "user_spoke":
            user_text = event.transcript
            print(f"👤 User said: {user_text}")
            
            # Generate response to user input
            await session.generate_reply(
                user_input=user_text,
                instructions="Respond naturally to the user's message."
            )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
