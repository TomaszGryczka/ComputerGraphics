from camera import Camera
import pygame

def handle_keyboard_input(camera: Camera, event):
    if event.type == pygame.QUIT:
            return False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            camera.move_forward()
        if event.key == pygame.K_s:
            camera.move_backward()
        if event.key == pygame.K_a:
            camera.move_left()
        if event.key == pygame.K_d:
            camera.move_right()
        if event.key == pygame.K_k:
            camera.move_up()
        if event.key == pygame.K_i:
            camera.move_down()
        if event.key == pygame.K_EQUALS:
            camera.scale(1)
        if event.key == pygame.K_MINUS:
            camera.scale(-1)
        if event.key == pygame.K_UP:
            camera.rotate_x(1)
        if event.key == pygame.K_DOWN:
            camera.rotate_x(-1)
        if event.key == pygame.K_LEFT:
            camera.rotate_y(1)
        if event.key == pygame.K_RIGHT:
            camera.rotate_y(-1)
        if event.key == pygame.K_q:
            camera.rotate_z(1)
        if event.key == pygame.K_e:
            camera.rotate_z(-1)
            
    return True