local speaker = peripheral.find("speaker")
local ws, err = http.websocket("ws://localhost:8080")

if not ws then
    print("Failed to connect:", err)
    return
end

print("Connected! Receiving audio...")

while true do
    local event, url, message = os.pullEvent("websocket_message")  -- Wait for WebSocket data
    if message and speaker then
        local success = speaker.playAudio(message)  -- Attempt to play the received audio
        if not success then
            print("Failed to play audio!")
        end
    end
end
