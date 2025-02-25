Button = {}

Button.__index = Button

function Button.new(x, y, width, height, color, text)
    -- Create a new instance
    local self = setmetatable({}, Button)
    -- Default values
    self.x = x or 0
    self.y = y or 0
    self.width = width or 5
    self.height = height or 3
    self.color = color or colors.lightGray
    return self
end


function Button:draw()
    -- Draw the button background
    drawFilledBox(self.x,self.y,self.x+self.width,self.y+self.height)
    -- Draw text if available
    if self.text then
        setBackgroundColor(self.color)
        local textX = self.x + math.floor((self.width - #self.text) / 2) -- Center text horizontally
        local textY = self.y + math.floor(self.height / 2) -- Middle row
        setCursorPosition(textX, textY)
        write(self.text)
    end
end


return Button

