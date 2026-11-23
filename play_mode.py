from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

    global balls
    balls=[Ball(random.randint(100, 1500),60,0) for i in range(30)]  #객체를 생성하는거임
    game_world.add_objects(balls, 1) #생성된 객체들이 game_world에 등록하는거임

    # 생성된 객체들의 충돌 관계를 등록
    game_world.add_collision_pair("boy:ball", boy,None)
    for ball in balls:
        game_world.add_collision_pair("boy:ball", None,ball)  # boy와 ball의 충돌 관계를 등록

    global zombies
    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)
    for zombie in zombies:
        game_world.add_collision_pair("zombie:ball", zombie, None)  # 좀비와 발사한 공 충돌 관계 등록

def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()
    # for ball in balls[:]:  # for ball in balls.copy(): 이렇게 하는거 대신 사용가능
    #     if game_world.collide(boy,ball):
    #         print('공이랑 충돌')
    #         game_world.remove_object(ball)
    #         boy.ball_count += 1
    #         balls.remove(ball)
    game_world.handle_collision()  # 충돌체크를 하는거임. 충돌이 일어나면 handle_collision을 호출해서 처리하게 하는거임

def render():
    clear_canvas()
    game_world.render()
    update_canvas()









