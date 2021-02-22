################################################################
import pygame
import os

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang") # 게임 이름

# FTP
clock = pygame.time.Clock()
################################################################

# 1. 사용자 게임 초기화
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") #images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height - stage_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값

# 공들
balls = []

# 최초 발생하는 큰공 추가
balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50,
    "img_idx" : 0, # 공의 이미지 인덱스(제일 큰 공)
    "to_x" : 3, # 공의 이동방향 (-3 : 왼쪽, 3 : 오른쪽)
    "to_y" : -6, # y축 이동방향
    "init_spd_y" : ball_speed_y[0] # y 최초 속도
})

# 사라질 무기 , 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# Font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()

# 게임 종료 메시지
# TimeOut (시간 초과 실패), Mission Complete, 
game_result = "Game Over"

# 무기 이동 방향
weapon_x_pos = 0
weapon_y_pos = 0

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) #  게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                character_to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: 
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: 
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
 
        if event.type == pygame.KEYUP: #  방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_to_y = 0       
    
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width    
        
    #무기 위치 조정
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 올리기
    weapons = [ [w[0], w[1] ] for w in weapons if w[1] > 0]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls) : # 공의 몇번째 인덱스인지 가져옴
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을 때 공 이동 위치 변경
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
        
        # 세로 위치
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 속도를 증가시킴
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls) : # 공의 몇번째 인덱스인지 가져옴
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        if character_rect.colliderect(ball_rect):
            running = False
            break
        
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx # 해당 공 없애기 위한 값 설정
                
                # 가장 작은 크기의 공이 아니라면 다음단계의 공으로 나눠주기
                if ball_img_idx < 3:
                    # 현재 공 크기의 정보를 가지고 옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]  
                    small_ball_height = small_ball_rect.size[1]

                    # 왼쪽으로 튕겨나가는 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1, 
                        "to_x" : -3, # 공의 이동방향 (-3 : 왼쪽, 3 : 오른쪽)
                        "to_y" : -6, # y축 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})
                    
                    # 오른쪽으로 튕겨나가는 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx" : ball_img_idx + 1, 
                        "to_x" : 3, # 공의 이동방향 (-3 : 왼쪽, 3 : 오른쪽)
                        "to_y" : -6, # y축 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]})
                break
        else: # 계속 게임을 진행
            continue # 안쪽 for문 조건이 맞지 않으면 continue
        break # 안쪽 for문에서 break를 만나면 여기로 진입가능
    
    # 충돌된 공 / 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    #if len(balls) == 0:

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    for idx, val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    
    screen.blit(stage, (0, screen_height - stage_height)) # 스테이지 그리기    
    screen.blit(character, (character_x_pos,  character_y_pos)) 

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks()- start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255, 255, 0))
    screen.blit(timer, (10, 10))

    # 시간 초과 계산
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    pygame.display.update() # 게임화면을 다시 그리기

# 게임 오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기

# pygame 종료
pygame.quit()

