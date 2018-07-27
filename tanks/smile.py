import arcade
#Draws a smiley face

#Set windows
SCREEN_WIDTH=600
SCREEN_HEIGHT=600
class Smiley:
    def draw(self):
        # Smiley drawing goes here
        #Open the window and set window title
        
        x = 300
        y = 300
        radius = 200
        arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
        x = 210
        y = 400
        radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE_SMOKE)
        x = 400
        y = 400
        radius = 20
        arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE_SMOKE)
        # Draw the smile
        x = 300
        y = 280
        width = 120
        height = 100
        start_angle = 190
        end_angle = 350
        arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)
        #arcade.finish_render()

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        Smiley.draw(self)
    def setup(self):
        # Set up your game here
        pass
    def on_draw(self):
        # Render the screen
        arcade.start_render()

    def on_key_press(self, key, modifiers):
        # Called whenever key is pressed
        if key == arcade.key.UP:
            self.smiley.change_y = 5
    def update(self, delta_time):
        """ All the logic to move, and game logic goes here """
        pass

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
if __name__ == '__main__':
    main()




