## Forge Support UI (React)

A Next.js frontend for the Forge Customer Support Agent. Pairs with the Python backend (`agent.py`) to provide a real-time voice support experience.

### Features
- Real-time voice interaction with LiveKit Agents
- Chat, media tiles, device controls
- Theming and branding via `app-config.ts`

### Project Structure
```
agent-starter-react/
├── app/
│   ├── (app)/
│   ├── api/               # issues tokens via LiveKit server credentials
│   ├── components/
│   ├── globals.css
│   └── layout.tsx
├── components/
├── hooks/
├── lib/
├── public/
└── package.json
```

### Setup
1) Create `.env.local`:
```env
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-livekit-server-url
LIVEKIT_ROOM=forge-support-room
```
2) Install and run (use npm on Windows):
```powershell
npm install
npm run dev
```
Open `http://localhost:3000`.

### Troubleshooting (Frontend)
- “pnpm not found”: use npm (`npm install`, `npm run dev`).
- Server Component dynamic import error: already fixed by rendering `App` directly in `app/(app)/page.tsx`.
- Token errors: verify `.env.local` LiveKit keys and URL, and that your LiveKit server is reachable.

### Git: Commit and Push This Folder
From the repository root (one level above this folder):
```powershell
git add agent-starter-react/*
git commit -m "docs(ui): update frontend README and config instructions"
git push origin master
```