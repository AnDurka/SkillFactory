#!/usr/bin/env python
# coding: utf-8

# In[42]:


import numpy as np
import math # Импортируем math для метода .ceil который окгругляет вверх


def game_core_v3(number):
    count = 1 # Кол-во попыток
    previous_predict = 100 # Сдесь мы будем записывать прошлые угадывания 
    predict = 50 # Начнём наше угадывание с 'золотой' середины
    while number != predict: # Цикл который завершится когда мы угадаем число
        count += 1 # Увеличиваем 
        if number > predict: 
            # Сдесь к predict мы будем добавлять половину от оставшегося сверху расстояния 
            predict, previous_predict = predict + math.ceil(abs(previous_predict-predict)/2), predict
        elif number < predict: 
            # Сдесь из predict мы будем вычитать половину от оствшегося расстояния снизу
            predict, previous_predict = predict - math.ceil(abs(previous_predict-predict)/2), predict
    return(count) # выход из цикла, если угадали


# P.S. Оствшееся расстояние это разность между 100 и прошлым predict-ом, расстояние от 0 до прошлого predict-а  
# сверху и снизу соответственно 


# In[ ]:





# In[43]:


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[ ]:





# In[52]:


score_game(game_core_v3)


# In[ ]:





# In[ ]:




