from time import time
class Timer:

  prev_time = 0.0
  elapsed_time = 0.0

  def init():
    __class__.prev_time = time()

  @staticmethod
  def capture_time():
    prev_time = __class__.prev_time
    current_time = time()
    __class__.elapsed_time = current_time - prev_time
    __class__.prev_time = current_time

  @staticmethod
  def get_elapsed():
    return __class__.elapsed_time

class Render:
  accumulated_elapsed_time = 0.0
  def init():
    return

  @staticmethod
  def render_begin() -> bool:
    Timer.capture_time()
    __class__.accumulated_elapsed_time += Timer.elapsed_time 
    if __class__.accumulated_elapsed_time < 1.0:
      print(__class__.accumulated_elapsed_time)
      return True
    else:
      #__class__.accumulated_elapsed_time = 0.0
      return False 


def run():

  is_true = True
  while is_true:
    is_true = Render.render_begin()
  print("game over")

Timer.init()
Render.init()
run()