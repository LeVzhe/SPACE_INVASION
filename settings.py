class Settings():
    def __init__(self):
        #настройки окна
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #настройки корабля
        self.ship_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullet_speed_factor = 3
        self.ship_limit = 3
        #настройки флота пришельцов
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
