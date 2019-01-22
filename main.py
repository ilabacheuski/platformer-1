import pygame
from constants import*
pygame.init() # Инициализация pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создаем окно для отрисовки
pygame.display.set_caption(TITLE) # Устанавливает заголовок окна

running = True
# Игровой цикл
while running:
    # events()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            ''' 
                Если (if) тип(type) события (event)
                равен (==)
                нажатию клавиши на клавиатуре (pygame.KEYDOWN)
            '''
            if event.key == pygame.K_ESCAPE:
                running = False


    # update()
    pass

    # draw()
    screen.fill(BACKGROUND_COLOR) # Заполняем экран цветом
    
    pygame.display.flip() # Отображаем нарисованое в Double buffer

pygame.quit()