ДОРОЖНАЯ КАРТА ПРОЕКТА

✯ Основное задание

Уделите внимание EDA (разведывательному анализу данных). Найдите закономерности в данных, опишите их и предоставьте графическое или численное доказательство. Много интересных инсайтов, которые могут пригодиться в дальнейшей работе, вы получите именно здесь.
Объясните, почему найденные закономерности могут оказать влияние на бизнес. Помните, что задача дата-сайентиста состоит не в том, чтобы получить красивые цифры, а оказать воздействие на бизнес. 
Выполните предобработку данных и сгенерируйте новые фичи — это может очень серьёзно повлиять на ваше положение в лидерборде.
Начните с простой модели, которая могла бы давать рекомендации к item/user. Вы вольны выбрать любую библиотеку.
Подумайте как решить проблему cold start (холодного запуска) для пользователей, которых нет в тренировочной выборке.
Работайте с отзывами как с текстовыми данными.
Не зацикливайтесь на одном решении. Пробуйте разные подходы! 
Используйте разные метрики для оценки качества модели. Позиция на лидерборде в kaggle не всегда коррелирует с качеством вашей модели. 
В финальном отчёте укажите, как предлагаемая вами рекомендательная система отразится на показателях бизнеса, а также какими метриками и почему вы бы замеряли эффективность от внедрения модели. 
Вы можете столкнуться с ситуацией, когда при добавлении матрицы фичей score упадёт. Это нормально! Таковы особенности работы LightFM с матрицами item-features.
✯✯ Дополнительное задание. Прототип рекомендательной системы

Без демонстрации работы модели не обходится ни один хакатон. Мы тоже предлагаем вам попробовать свои силы в этом задании и создать работающий прототип рекомендательной системы c помощью Streamlit и Heroku. 

Внимание! Это задание для тех из вас, кто готов освоить новый инструмент самостоятельно (вы уже знаете, как это важно в работе любого дата сайентиста).

Инструкцию по работе со Streamlit и Heroku вы найдёте в модуле «*BONUS. Быстрое прототипирование». 

Не забудьте протестировать, насколько ваш прототип user-friendly! Например, по какому параметру лучше искать товары? Какие данные лучше выводить и в какой последовательности?

Ссылку на работающий прототип добавьте в финальный отчет и поделитесь результатами работы с одногруппниками!

1. Анализ датасета EDA	
Проведен визуальный и статистический анализ датасета
Из графиков можно понять закономерности
Даны комментарии и выводы
2. Обработка данных	
Удалены дублирующие записи, если они есть
Обоснован выбор фичей для обучения модели
Данные разделены на train/test
3. Создание модели	
Присутствует работоспособная модель/эмбеддинги
Присутствует score модели на тестовой выборке
Обоснован выбор модели, сравнение с другими моделями и проведён подбор гиперпараметров
4. Соревнование на Kaggle	
Предложенное решение улучшает показатели baseline
Место в итоговом групповом рейтинге
5. Интерфейс на Streamlit	
Присутствует User Interface (UI), сделанный через Streamlit
Прототип удобен в использовании
6. Деплой с помощью Heroku	
Модель загружена на heroku и доступна по веб-адресу
7. Заключение	
Сформулированы инсайты и основные выводы
Обоснован выбор метрик для оценивания влияния РС на бизнес
Описана работа в команде

## Как сдать работу:

1. Создайте папку в своем Git-репозитории skillfactory_rds по типу module_<номер модуля> и загрузите туда своё решение. 

2. Загрузите проект на github.

Отчет по проекту должен содержать два файла: краткое описание и ноутбук с решением.

В описании кратко укажите:

- основные цели и задачи проекта;

- краткую информацию о данных;

- этапы работы над проектом;

- ваш никнейм на Kaggle;

- **ссылку на прототип.

В описании ответьте на вопросы:

1. Какова была ваша роль в команде? Кратко опишите, что именно вы сделали в рамках командного проекта.

2. Как вы оцениваете свой вклад в командную работу?

3. Какой частью своей работы вы остались особенно довольны?

4. Что не получилось сделать так, как хотелось? Над чем ещё стоит поработать?

5. Что интересного и полезного вы узнали в этом модуле?

6. Что является вашим главным результатом при прохождении этого проекта?

Ноутбук с решением должен содержать:

- цели и задачи проекта;

- поэтапное описание работы;

- промежуточные выводы;

- основные итоги работы.

3. Прикрепите ссылку на github в поле ниже.
