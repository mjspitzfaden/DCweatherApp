import models

def forward ():
  models.DB.create_tables([models.WeatherApp])

if __name__ == '__main__':
  forward()
