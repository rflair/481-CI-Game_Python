# Alien Invasion
# Defend your house from attacking zombies!

import math, random
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Alien(games.Sprite):
    """ An alien attacker. """
    image = games.load_image("ship.bmp")
    SPEED = 0.5
    POINTS = 10
      
    def __init__(self, game, x, y = 90):
        """ Initialize alien. """
        self.game = game
        super(Alien, self).__init__(image = Alien.image,
                                    x = x, y = y,
                                    dy = Alien.SPEED)


    def update(self):
        """ Update alien sprite. """
        # If the alien gets to the bottom of the screen, GAME OVER
        if self.bottom > games.screen.height:
            self.end()
            self.destroy()

        # Call die() if aien is hit with missile
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """ Destroy alien """
        # create explosion
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)

        # add 10 to score for each alien hit
        self.game.score.value += 10
        self.game.score.right = games.screen.width - 10

        # delete sprite
        self.destroy()

    def end(self):
        """ Display GAME OVER and end game. """
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)  


class Tank(games.Sprite):
    """ Tank used to fight zombies! """
    image = games.load_image("tank.png")
    ROTATION_STEP = 3
    VELOCITY_STEP = 0.3
    MISSILE_DELAY = 20

    def __init__(self):
        """ Initialize tank. """
        super(Tank, self).__init__(image = Tank.image,
                                   x = games.screen.width/2,
                                   y = games.screen.height/1.1,
                                   is_collideable = False)
        self.missile_wait = 0

    def update(self):
        """ Move tank with keyboard. """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 2
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 2

        # update wait
        if self.missile_wait > 0:
            self.missile_wait -= 1

        # fire missiles with SPACE key
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Tank.MISSILE_DELAY

    def die(self):
        """ Destroy tank """
        self.destroy()
            
        

class Missile(games.Sprite):
    """ A missile launched by the player's ship. """
    image = games.load_image("bomb.png")
    BUFFER = 50
    VELOCITY_FACTOR = 7

    def __init__(self, tank_x, tank_y, tank_angle):
        """ Initialize missile sprite. """        
        # convert to radians
        angle = tank_angle * math.pi / 180  

        # calculate missile's starting position 
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = tank_x + buffer_x
        y = tank_y + buffer_y

        # calculate missile's velocity components
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # create the missile
        super(Missile, self).__init__(image = Missile.image,
                                      x = x, y = y,
                                      dx = dx, dy = dy)


    def die(self):
        """ Destroy the missile. """
        self.destroy()

class Explosion(games.Animation):
    """ Explosion animation """
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        """ Initialize explosion. """
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)

class Mothership(games.Sprite):
    """ A mothership that generates the alien ships. """
    image = games.load_image("Mothership.png");
    def __init__(self, game, y = 55, speed = 2, odds_change = 200):
        """ Initialize Mothership. """
        self.game = game
        super(Mothership, self).__init__(image = Mothership.image,
                                         x = games.screen.width / 2,
                                         y = y,
                                         dx = speed,
                                         is_collideable = False)
        self.odds_change = odds_change
        self.time_til_spawn = 0

    def update(self):
        """ Determine if direction needs to be reversed. """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_spawn()

    def check_spawn(self):
        """ Decrease countdown or spawn alien and reset countdown. """
        if self.time_til_spawn > 0:
            self.time_til_spawn -= 1
        else:
            new_alien = Alien(game = self.game, x = self.x)
            games.screen.add(new_alien)

            self.time_til_spawn = int(new_alien.height * 1.5 / Alien.SPEED) + 1

    

class Game(object):
    """ The game itself """
    def __init__(self):
        # create tank
        self.tank = Tank()
        games.screen.add(self.tank)

        # create score
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)


    def play(self):
        # load background
        ground_image = games.load_image("dirt.jpg")
        games.screen.background = ground_image

        # start play
        games.screen.mainloop()

        
def main():
    """ Main function. """

    # create game
    mygame = Game()
    
    # create mothership
    the_mothership = Mothership(game = mygame)
    games.screen.add(the_mothership)

    # play game
    mygame.play()

# call main
main ()
