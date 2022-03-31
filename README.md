# Тестовое задание для отбора на кафедру 1С

Сначала, не надеясь на то, что что-то получится обучить, я завёл бейзлайн на голом open-cv, код которого
представлен в этом репозитории. За полтора часа до дедлайна от скуки начал трансфер лёрнить маленький ResNet.
Демо ResNet'а завести не успею, но процесс обучения и бенчмарки модели можно посмотреть в [ноутбуке](https://colab.research.google.com/drive/1-nXQWD_4uewYs9JlOonwjbhcNRzi6ITd?usp=sharing).

## Результаты ResNet

ResNet чуть хуже попадает в вершины листков, но лучше работает, когда лист бумаги лежит на белом фоне.
Больше результатов можно посмотреть в [колабе](https://colab.research.google.com/drive/1-nXQWD_4uewYs9JlOonwjbhcNRzi6ITd?usp=sharing).

![image](https://user-images.githubusercontent.com/22542643/161119810-6bbdb781-0a51-4943-8932-7a65ad106465.png)

## Результаты CV2

CV2 точнее предсказывает границы, но иногда плохо справляется с пёстрым фоном.

![image](https://user-images.githubusercontent.com/22542643/161120250-a73d5f9d-3d13-45b5-9837-682841a667b3.png)

![image](https://user-images.githubusercontent.com/22542643/161120424-698d14ea-2d33-466a-96a6-b994acc4a40f.png)


## Пример использования

`python main.py --input_path=image/1.jpg`
