world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI

def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o) # 충돌 객체도 제거
            return

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()




def clear():
    for layer in world:
        layer.clear()

def collide(a,b):
    left_a,bottom_a,right_a,top_a = a.get_bb()
    left_b,bottom_b,right_b,top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

collision_pairs={}
def add_collision_pair(group, a, b):
    if group not in collision_pairs: # 처음 등록되는 충돌 그룹이면, 충돌 그룹을 생성하고, a와 b를 등록
        collision_pairs[group] = [[], []]  #a와 b를 담을 리스트를 생성
    if a is not None: # if a: 이렇게 해도 됨
        collision_pairs[group][0].append(a)
    if b is not None:
        collision_pairs[group][1].append(b)
   
def handle_collision():
    for group, pairs in collision_pairs.items():
        for a in pairs[0][:]:      # 검사 도중 리스트에서 제거될 수 있으므로 복사본으로 순회
            for b in pairs[1][:]:
                if collide(a,b):
                    a.handle_collision(group, b) # a가 충돌이 났으면 누구와 충돌인지 알기 위해(b)를 해서 누구랑 충돌인지 확인하고 충돌체크를 한다.
                    b.handle_collision(group, a)

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)