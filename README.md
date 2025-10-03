<div align="center">
  <h2>Forge Customer Support Agent</h2>
  <p>Full-stack voice agent: Next.js UI + Python LiveKit Agent</p>
</div>

### Overview
- UI: Next.js app in `agent-starter-react/`
- Backend: Python worker in `agent.py`
- Real-time voice via LiveKit; knowledge via Pinecone; LLM via OpenAI

### Prerequisites
- Windows 10/11
- Node.js 18+ and npm
- Python 3.10+

### 1) Frontend Setup (UI)
1. Create `agent-starter-react/.env.local`:
```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-livekit-server-url
LIVEKIT_ROOM=forge-support-room
```
2. Install and run:
```powershell
cd C:\Users\HP\Desktop\customerSupportAgent\agent-starter-react
npm install
npm run dev
```
Open `http://localhost:3000`.

### 2) Backend Setup (Python Agent)
1. Create `.env` at project root:
```env
PINECONE_API_KEY=your_pinecone_api_key
ASSISTANT_NAME=your_pinecone_assistant_name
OPENAI_API_KEY=your_openai_api_key

LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-livekit-server-url

ASSEMBLYAI_API_KEY=your_assemblyai_api_key
CARTESIA_API_KEY=your_cartesia_api_key
```
2. Create/activate venv and install deps:
```powershell
cd C:\Users\HP\Desktop\customerSupportAgent
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -U livekit-agents livekit-plugins-silero pinecone pillow cartesia assemblyai python-dotenv
```
3. Start the agent and join the same room as the UI:
```powershell
python agent.py dev --room forge-support-room
# or
# python agent.py start --room forge-support-room
```
You should see: "✅ Pinecone Assistant initialized successfully" and the agent listening.

### Tools & Services Used
- LiveKit: real-time media + Agents runtime
- OpenAI: LLM (configurable)
- Pinecone: knowledge base assistant
- AssemblyAI: speech-to-text (STT)
- Cartesia: text-to-speech (TTS)
- Silero: voice activity detection (VAD)

### Troubleshooting
- pnpm not found: use npm (`npm install`, `npm run dev`).
- Server Components error (`next/dynamic ssr: false`): already fixed in `app/(app)/page.tsx` by directly rendering `App`.
- Hedra import error: ensure `agent.py` uses `from livekit.plugins import silero`.
- Pinecone package error: uninstall `pinecone-client`, install `pinecone`.
```powershell
pip uninstall -y pinecone-client
pip install pinecone
```
- Missing provider keys: either provide API keys in `.env` or change `stt`/`tts` in `agent.py`.
- Backend and UI not meeting: set `LIVEKIT_ROOM=forge-support-room` in UI `.env.local` and start backend with `--room forge-support-room`.

### Quick Commands
```powershell
# UI
cd agent-starter-react
npm install
npm run dev

# Backend
cd ..
./venv/Scripts/Activate.ps1
python agent.py dev --room forge-support-room
```


