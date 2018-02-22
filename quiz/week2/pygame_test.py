"""
# -*- coding: utf-8 -*-
import pygame
import sys

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

for event in pygame.event.get():
    if not hasattr(event, 'key'):  # 키 관련 이벤트가 아닐 경우, 건너뛰도록 처리하는 부분
        continue
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            # 오른쪽 키에 대한 처리
            ...
        elif event.key == K_LEFT:
            # 왼쪽 키에 대한 처리
            ...
        elif event.key == K_UP:
            # 위쪽 키에 대한 처리
            ...
        elif event.key == K_DOWN:
            # 아래 키에 대한 처리
            ...
        elif event.key == K_ESCAPE:
    # ESC 키에 대한 처리

    BLACK = (0, 0, 0)  # R, G, B
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLUE_A = (0, 0, 255, 127)  # R, G, B, Alpha(투명도, 255 : 완전 불투명)
"""