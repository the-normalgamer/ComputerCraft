Button = {}

Button.__index = Button

function Button.new(x, y, width, height, color, text)
    if height==0 then error("button can't have 0 height") end
    -- Create a new instance
    local self = setmetatable({}, Button)
    -- Default values
    self.x = x or 0
    self.y = y or 0
    self.width = width or 5
    self.height = height-1 or 2
    self.color = color or colors.lightGray
    return self
end


function Button:draw()
    term.setBackgroundColor(self.color)
    -- Draw the button background
    paintutils.drawFilledBox(self.x,self.y,self.x+self.width,self.y+self.height)
    -- Draw text if available
    if self.text then
        local textX = self.x + math.floor((self.width - #self.text) / 2) -- Center text horizontally
        local textY = self.y + math.floor(self.height / 2) -- Middle row
        term.setCursorPos(textX, textY)
        write(self.text)
    end
end


return Button