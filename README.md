# qr
Генератор QR кода 
Проблема: лектору трудно отметить людей, в большом количестве, которые пришли на лекцию.
 
Цель: создать генератор QR кода (уникальная ссылка) на каждый день лекции с возможностью отметить присутствие слушателя.
 
Решение: создать специальный интерфейс (веб или мобильное приложение) который позволяет генерировать и выводить QR код. В интерфейс должна быть включена возможность выбрать точное количество слушателей которые пришли на лекцию.
Сам QR код должен содержать в себе ссылку на страницу, где слушатель выбирает из списка свою фамилию (или вводит номер телефона), и нажимает «Подтвердить». Второй раз тот же слушатель свое присутствие в тот день подтвердить не может.
На стороне сервера должна быть соответствующая БД которая содержит в себе лекции который посетил каждый из слушателей курса.
