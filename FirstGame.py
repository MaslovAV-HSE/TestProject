import arcade, random, os


class MyGame(arcade.Window):
    def __init__(self, width,height,caption):
        super().__init__(width, height, caption, resizable=True, fullscreen=True)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        width, height = self.get_size()
        self.set_viewport(0, width, 0, height)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 0
        if symbol == arcade.key.UP:
            self.player.change_y = 0
        if symbol == arcade.key.DOWN:
            self.player.change_y = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player.change_x = -5
            self.player.texture = self.player_left.image
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 5
            self.player.texture = self.player_right.image
        if symbol == arcade.key.UP:
            self.player.change_y = 5
            self.player.texture = self.player_up.image
        if symbol == arcade.key.DOWN:
            self.player.change_y = -5
            self.player.texture = self.player_down.image
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_update(self, delta_time: float):
        if self.player.center_x > self.width:
            self.player.center_x = 50
        if self.player.center_x < 0:
            self.player.center_x = self.width
        if self.player.center_y > self.height:
            self.player.center_y = 50
        if self.player.center_y < 0:
            self.player.center_y = self.height

        self.clear()
        collizion = arcade.check_for_collision_with_list(self.player, self.listobjects)
        for i in collizion:
            self.points += 1
            i.kill()
            self.player.scale += 0.01
            self.object = arcade.Sprite("Pics/mariohat.png", 0.05)
            self.object.center_x = random.randint(50, self.width - 50)
            self.object.center_y = random.randint(100, self.height - 100)
            self.listobjects.append(self.object)

        self.player.update()
        self.listobjects.update()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            self.width, self.height,
                                            self.background)

        arcade.draw_text(f"Points: {self.points}",
                         self.width - 550,
                         self.height - 800,
                         arcade.color.BLACK,
                         15 * 2,
                         width=800,
                         align="center")

    def on_draw(self):
        self.player.draw()
        self.listobjects.draw()

    def setup(self):


        #bacground
        self.background = arcade.load_texture('Pics/map.png')

        #player
        self.player_right = arcade.load_texture("Pics/0.png", 2)
        self.player_left = arcade.load_texture("Pics/1.jpg", 2)
        self.player_up = arcade.load_texture("Pics/2.jpg", 2)
        self.player_down = arcade.load_texture("Pics/0.png", 2)

        self.player = arcade.Sprite("Pics/0.png", 2)
        self.player.center_x = 400
        self.player.center_y = 150
        self.points = 0

        #objects
        self.listobjects = arcade.SpriteList()
        for i in range(10):
            self.object = arcade.Sprite("Pics/mariohat.png", 0.05)
            self.object.center_x = random.randint(100, self.width - 100)
            self.object.center_y = random.randint(100, self.height - 100)
            self.listobjects.append(self.object)


def main():
    game = MyGame(1920, 600, "FirstGame")
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
