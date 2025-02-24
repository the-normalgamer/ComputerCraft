local speaker = peripheral.find("speaker")
if not speaker then
    print("❌ No speaker found! Connect one to play audio.")
    return
end

print("🔌 Connecting to Python WebSocket server...")
local ws, err = http.websocket("ws://YOUR_PC_IP:8080")  -- Replace with your PC's IP!

if not ws then
    print("❌ Connection failed:", err)
    return
end

print("✅ Connected! Receiving audio...")

while true do
    local event, url, message = os.pullEvent("websocket_message")
    if message then
        speaker.playAudio(message)
    end
end
