﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define gg = Character('[ggname]', color="#66cc00", image = "gg")
define boss = Character('Начальство', color="#ffffff", image = "boss")
define emily = Character('Эмили', color="#ffffff", image = "emily")
define michael = Character('Майкл', color="#ffffff", image = "michael")
define sarah = Character('Сара', color="#ffffff", image = "sarah")
define robert = Character('Роберт', color="#ffffff", image = "robert")

# Варианты концовок
define communication = False
define productivity = False
define skills = False

# Музыка и звуки
define audio.bgmusic = "audio/music/Cool Blast.mp3"
define audio.office = "audio/music/office.mp3"
define audio.sadend = "audio/music/The Lost Song.mp3"
define audio.bell = "audio/sounds/elevator ball.mp3"
define audio.steps = "audio/sounds/steps.ogg"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
init:
    $ left = Position(xalign = 0.2)
    $ right = Position(xalign = 0.8)

# Игра начинается здесь:
label start:

    # Акт 1

    scene bg room
    show gg

    play music bgmusic

    $ ggname = renpy.input("Введите мужское имя главного героя:", default="Джейсон", length=10, allow="абвгдеёжзийклмнопрстуфхцчшщъыьэюя-АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ").strip()

    if ggname == "":
        $ ggname = "Джейсон"

    "[ggname], молодой и талантливый программист, получает повышение и переходит на должность тимлида в технологической компании \"ФьючерТек\"."

    "Он с нетерпением ждет новых вызовов и возможностей, которые предоставляет эта новая роль."

    gg "Так, сегодня у меня первая встреча с начальством. Надеюсь, что они доверят мне интересный проект."

    scene bg office with fade
    show boss at left

    "Парень приезжает в офис и поднимается в кабинет директора."

    show boss happy at left

    boss "Доброе утро, поздравляем с выходом на новую должность!"

    show boss at left
    
    play sound steps

    show gg at right
    with moveinright

    gg "Доброе, спасибо!"

    gg "Сегодня начальник в хорошем расположении духа, это радует."

    show boss happy at left
    
    boss '''
    Итак, в качестве твоего первого проекта я даю тебе FinTechTrack-проект по разработке инновационного мобильного приложения для управления финансами.

    Это приложение должно предоставлять пользователям удобный и безопасный способ отслеживать свои финансовые операции, составлять бюджеты, анализировать расходы и доходы, а также получать персонализированные рекомендации по управлению финансами.

    Не самая трудная работа, но и не легкая. Ты должен справиться.

    Руководство командой и обеспечение успешного выполнения проекта – твои основные задачи. Не забывай о важности эффективной коммуникации, управления временем и принятия решений.
    '''

    show boss at left

    gg "Звучит тяжело{w}, но не невыполнимо."

    show boss happy at left

    boss "Также на своем пути ты будешь встречаться с разными трудностями и вызовами. Они могут возникнуть как внутри твоей команды, так и вне ее."

    show boss at left

    gg "Ага, понял. Думаю, я со всем справлюсь."

    show boss happy at left

    boss "Молодец! Вот он, боевой настрой!"

    boss "Ну, теперь можешь идти. Сегодня у меня для тебя больше ничего нет."

    show boss at left

    hide boss with moveoutleft

    play sound steps

    gg "Хорошо, до свидания."

    stop music fadeout 1
    play sound steps

    scene bg elevator with fade
    show gg

    "[ggname] направляется на первую встречу со своей командой. Просмотрев папку со всей информацией, он быстро придумывает речь для презентации идеи проекта и мотивации коллег."

    gg "Хм, в голове все выглядит достаточно легче, чем объяснял начальник…"

    gg "Ну, сейчас и узнаем."

    play sound bell

    "Лифт достигает нужного этажа. [ggname] оказывается в коворкинге офиса."

    play music bgmusic

    scene bg meeting room with fade
    show emily:
        xalign 0.1 yalign 1.8
    show michael:
        xalign 0.3 yalign 1.0
    show sarah:
        xalign 0.55 yalign 1.0
    show robert:
        xalign 0.85 yalign 1.0

    "Все остальные члены команды уже были на месте и ждали только своего тимлида."

    gg "Привет, ребята! Я очень рад видеть вас здесь. У нас предстоит великий проект, и я уверен, что вместе мы сможем достичь невероятных результатов. Каждый из вас обладает уникальными навыками и опытом, и я уверен, что мы сможем использовать их на полную мощность."

    emily "Спасибо, [ggname]! Я очень вдохновлена этим проектом и готова внести свой вклад в его разработку. У меня есть несколько идей, которые могут значительно улучшить пользовательский опыт."

    michael "Я полностью поддерживаю Эмили. Дизайн играет огромную роль в создании эффективного продукта. У меня есть несколько концепций, которые могут сделать наш продукт визуально привлекательным и уникальным."

    sarah "И я готова приступить к работе над маркетинговой стратегией. Мы должны выявить наши целевые аудитории, разработать запоминающийся бренд и показать всем, почему наш продукт лучший на рынке."

    robert "Я уже начал исследования в области искусственного интеллекта, и у меня есть несколько интересных идей, которые могут помочь нам улучшить наш продукт и внедрить новые функциональности."

    gg "Отлично, мне нравится ваш рабочий настрой, давайте же определим приоритетные задачи!"

    menu:
        "Какие задачи поставить в приоритет?"

        "Улучшение коммуникации":
            $ communication = True
            jump communication

        "Повышение производительности":
            $ productivity = True
            jump productivity

        "Развитие навыков команды":
            $ skills = True
            jump skills

    return

label communication:
    
    $ renpy.notify("Улучшение коммуникации")

    "[ggname] решает, что для эффективной работы команды необходимо улучшить коммуникацию. Он предлагает регулярные командные собрания, открытые форумы для обмена идеями и механизмы обратной связи. Тем самым создается атмосфера, в которой каждый член команды чувствует себя услышанным и участвующим в процессе принятия решений."

    gg "Я предлагаю регулярные командные собрания, открытые форумы для обмена идеями и механизмы обратной связи. Тем самым каждый член команды будет услышанным и примет участие в процессе принятия решений."

    scene bg discussion with fade

    stop music fadeout 1
    play music office

    '''
    [ggname] реализует свою стратегию по улучшению коммуникации в команде. Он начинает регулярно проводить командные собрания, на которых участники могут делиться своими идеями и проблемами.

    Он также создает открытые форумы, где сотрудники могут высказывать свои предложения и обсуждать важные вопросы.

    Благодаря улучшенной коммуникации, команда становится более согласованной и эффективной. Участники команды начинают лучше понимать друг друга, сотрудничать и решать проблемы вместе.

    Кроме того, создается атмосфера доверия и сотрудничества, что способствует более успешному выполнению проектов.
    '''

    jump act_2

    return

label productivity:

    $ renpy.notify("Повышение производительности")

    "[ggname] считает, что повышение производительности команды является приоритетной задачей. Он внедряет методики управления проектами, оптимизирует рабочие процессы и устанавливает четкие цели и сроки для каждого задания. Он также предлагает индивидуальные консультации для каждого члена команды, помогая им развивать навыки и повышать эффективность работы."
    
    gg "Я предлагаю внедрить некоторые методики управления проектами, оптимизировать рабочие процессы и устанавливать четкие цели и сроки для каждого задания. Также, я могу проводить индивидуальные консультации для каждого члена команды, помогая вам развивать навыки и повышать эффективность работы."

    scene bg discussion with fade

    stop music fadeout 1
    play music office

    '''
    [ggname] сосредотачивается на повышении производительности команды. Он внедряет методики управления проектами, устанавливает четкие цели и сроки для каждого задания, и регулярно отслеживает прогресс.

    Он также предлагает индивидуальные консультации для каждого члена команды, помогая им развивать навыки и повышать эффективность работы.

    В результате улучшения производительности команды, проекты успешно реализуются в срок и соответствуют высоким стандартам качества.

    Команда становится более организованной и способной справиться с различными вызовами. [ggname] видит, как его команда процветает и достигает новых высот.
    '''

    jump act_2

    return

label skills:

    $ renpy.notify("Развитие навыков команды")

    "[ggname] осознает, что для достижения успеха необходимо инвестировать в развитие своей команды. Он предлагает обучающие программы, тренинги и менторство, чтобы участники команды могли расширять свои знания и навыки. Это позволяет команде стать более компетентной и способной справиться с различными вызовами проектов."

    gg "Я предлагаю проводить обучающие программы, тренинги и менторство, чтобы вы могли расширять свои знания и навыки. Это позволяет вам стать более компетентной и способной командой, которая справиться с различными вызовами проектов."

    scene bg discussion with fade

    stop music fadeout 1
    play music office

    '''
    [ggname] сосредотачивает свое внимание на развитии навыков своей команды. Он предлагает обучающие программы, тренинги и менторство, чтобы участники команды могли расширять свои знания и навыки.

    Каждый член команды получает возможность развиваться и повышать свою профессиональную компетентность. Благодаря развитию навыков команды, проекты становятся более сложными и инновационными.

    Команда способна решать технические и организационные проблемы с большей легкостью. [ggname] видит, как его команда развивается и становится все более квалифицированной.
    '''

    jump act_2

    return

label act_2:

    # Акт 2

    gg "Команда, я хотел поделиться с вами важными новостями. Наш проект получил признание на конференции, и мы получили предложение о финансировании от крупного инвестора. Это огромный шаг вперед для нас!"

    emily "Вот это просто поразыительно, [ggname]! Это действительно великолепные новости. Наша команда работала настолько усердно, и теперь мы получаем заслуженное признание."

    michael "Это действительно впечатляюще! Я горжусь тем, что являюсь частью этой команды. Наш дизайн и творческие решения действительно выделяют наш продукт среди конкурентов."

    sarah "Отличные новости! Теперь у нас будет дополнительное финансирование, чтобы продвигать наш продукт на рынке. Мы сможем привлечь больше клиентов и увеличить нашу долю рынка."

    robert "Это прекрасные новости, и я уверен, что с дополнительным финансированием мы сможем ускорить разработку и внедрение наших AI-технологий. Это будет революционно!"

    gg "Спасибо, ребята! Без вашего усердия и вклада мы бы не смогли добиться таких результатов. Наш путь только начинается, и я верю, что вместе мы сможем достичь еще больших высот. Давайте продолжим работать усердно и делать нашу команду еще сильнее."

    menu:
        "Однако у команды все шло не так гладко. Они столкнулись с..."

        "Технические сложности":
            jump technical_problems
        
        "Конфликты в команде":
            jump conflicts
        
        "Изменения в требованиях проекта":
            jump project_changes 
        
    return

label technical_problems:

    $ renpy.notify("Технические сложности")

    scene bg technical problems with fade

    gg "У нас впереди много работы, ребята. Но будьте готовы, мы столкнемся с различными препятствиями. Главное - не паниковать и работать вместе."

    emily "Я заметила, что некоторые части кода не работают должным образом. У нас возникли технические сложности."

    gg "Понимаю. Давайте проведем тщательное техническое исследование и выясним, в чем проблема. Может быть, нам потребуется добавить ресурсы или изменить подход. Кто готов взять на себя это?"

    emily "Я могу взять на себя эту задачу. Я уже начал анализировать код и выявил несколько потенциальных проблемных мест. Думаю, мне потребуется немного времени, чтобы их исправить."

    gg "Отлично, Эмили! Работай над этим и сообщай о своих прогрессах. В то же время, остальные продолжают разработку других функций проекта."

    jump act_3

    return

label conflicts:

    $ renpy.notify("Конфликты в команде")

    scene bg conflicts with fade

    gg "У нас впереди много работы, ребята. Но будьте готовы, мы столкнемся с различными препятствиями. Главное - не паниковать и работать вместе."

    sarah "У нас возникли разногласия в отношении стратегии для достижения наших целей. Некоторые из нас считают, что нам нужно сосредоточиться на определенных функциях, а другие считают, что мы должны идти по другому пути."

    gg "Я понимаю, Сара. Возможно, каждый из вас может представить свои идеи и аргументы, а затем мы проведем голосование для определения наиболее эффективного пути. Важно, чтобы все члены команды чувствовали себя вовлеченными в принятие решения."

    jump act_3
    
    return

label project_changes:

    $ renpy.notify("Изменения в требованиях проекта")

    scene bg optimization with fade

    gg "У нас впереди много работы, ребята. Но будьте готовы, мы столкнемся с различными препятствиями. Главное - не паниковать и работать вместе."

    sarah "Я заметила, что у нас есть ресурсы, которые не используются эффективно. Мы могли бы оптимизировать наш рабочий процесс и повысить производительность."

    gg "Это интересная идея, Сара. Давайте проведем встречу, на которой каждый из нас представит свои предложения по оптимизации рабочего процесса. Может быть, у кого-то есть конкретные идеи или опыт в этой области?"

    emily "У меня есть несколько предложений насчет автоматизации некоторых рутинных задач. Я думаю, мы можем использовать специальные инструменты или программы, чтобы сэкономить время и ресурсы."

    gg "Прекрасно, Эмили! Давайте соберем все предложения и проведем обсуждение нашей текущей системы работы. Посмотрим, какие изменения мы можем внести, чтобы повысить эффективность и оптимизировать наш рабочий процесс."

    jump act_3
    
    return

label act_3:

    # Акт 3

    scene bg meeting room with fade
    show gg

    stop music fadeout 1
    play music bgmusic

    "Команда успешно решает некоторые технические проблемы и продолжает разработку проекта. Они уже достигли середины установленного срока и у них остается меньше времени, чем они надеялись. [ggname] решает собрать команду, чтобы оценить текущее положение дел и обсудить, как они могут ускорить работу."
    
    gg "Ребята, мы успешно преодолели несколько технических проблем, но у нас осталось меньше времени, чем мы хотели."

    gg "Нам нужно обсудить, как мы можем ускорить работу и добиться наших целей в оставшееся время. Кто-то имеет предложения или идеи?"

    hide gg
    show michael

    michael "Я думаю, мы можем параллельно работать над некоторыми задачами. Вместо того, чтобы ждать завершения одной функции, мы можем распределить работу между несколькими членами команды и ускорить процесс разработки."

    hide michael
    show emily:
        xalign 0.5 yalign 1.8

    emily "Я согласна с Майклом. Мы можем создать несколько подкоманд, каждая из которых будет ответственна за определенные функции проекта. Таким образом, мы сможем работать параллельно и сократить время разработки."

    hide emily
    show gg

    gg "Отличная идея! Давайте сформируем эти подкоманды и назначим ответственных за каждую функцию проекта."

    gg "Эмили, ты можешь взять на себя руководство одной из подкоманд, а Майкл - другой. Пожалуйста, выберите своих помощников и начните работу как можно скорее."

    hide gg
    show michael

    michael "Хорошо, я возьму на себя руководство разработкой интерфейса пользователя. [ggname], я могу выбрать Сару в свою команду?"

    hide michael
    show gg

    gg "Конечно, Майкл, выбирайте свою команду и начинайте работу. Майкл, ты можешь выбрать кого-то из оставшихся членов команды и начать работу над функциями бэкэнда."

    hide gg
    show emily:
        xalign 0.5 yalign 1.8

    emily "Я выберу Роберта в свою команду. Мы сосредоточимся на разработке базы данных и серверной части проекта."

    hide emily
    show gg

    gg "Отлично! Каждая подкоманда начинает работу сегодня же. Давайте держать связь и регулярно обмениваться информацией о прогрессе. Если у кого- то возникнут проблемы или затруднения, не стесняйтесь обратиться за помощью."

    "Проходит некоторое время, команда работает параллельно над разными функциями проекта."

    "[ggname] собирает команду для обновления о прогрессе"

    gg "Ребята, у нас осталось всего несколько недель до окончания проекта. Какие результаты у вас до сих пор? Как идут работы?"

    scene bg meeting room 1

    michael "Мы проделали большую работу над интерфейсом пользователя. У нас уже есть прототип, который включает основные функции и дизайн. Сейчас мы проводим тестирование и собираем обратную связь от пользователей, чтобы внести последние корректировки."

    scene bg meeting room
    show gg

    gg "Отличная работа, ребята! Я вижу, что вы очень сосредоточены на достижении наших целей. Давайте продолжим в том же духе и уделите особое внимание исправлению ошибок и оптимизации проекта."

    "Команда продолжает работу над проектом, сосредотачиваясь на завершении разработки и тестировании."

    gg "Ребята, я горжусь каждым из вас за ваше упорство и преданность проекту. Благодаря нашей командной работе мы успешно завершили проект в срок и достигли наших целей. Это было непросто, но мы справились!"

    hide gg
    show michael
    
    michael "Спасибо, [ggname]. Это было замечательное путешествие, и я благодарна всему коллективу за поддержку и сотрудничество. Мы создали отличный продукт!"

    hide michael
    show emily:
        xalign 0.5 yalign 1.8

    emily "Согласен, Майк. Это было нелегкое испытание, но благодаря нашему труду и взаимодействию мы смогли достичь успеха. Я очень горжусь тем, что был частью этой команды."

    hide emily

    "Команда поднимает бокалы и отмечает завершение проекта. Они празднуют свои достижения и готовятся к следующему вызову, зная, что смогут преодолеть любые трудности вместе."

    if communication:

        jump lessons_end

    if productivity:

        jump bad_end
    
    if skills:

        jump happy_end

    return

label lessons_end:

    # Концовка Уроки на пути к успеху

    scene bg conference with fade

    "Когда наступает день презентации, проект демонстрирует хорошие результаты, хотя есть некоторые недочеты, которые заказчик замечает."

    scene bg happy end with fade

    $ renpy.notify("Уроки на пути к успеху")

    gg "Были моменты, когда я сомневался в своих способностях, и мы сталкивались с некоторыми трудностями. Но благодаря вашему терпению и поддержке, мы смогли преодолеть все преграды."

    gg "Я извлек множество уроков из своих ошибок и старался стать лучшим тимлидом для каждого из вас. Сегодня мы празднуем наш успех, и я уверен, что мы еще сделаем большие вещи в будущем."

    return

label happy_end:

    # Концовка Успех и признание

    scene bg conference with fade

    "Когда наступает день презентации, проект демонстрирует высокую производительность, отличную функциональность и пользовательский опыт, вызывая восторг и уважение заказчика."

    scene bg happy end with fade

    $ renpy.notify("Успех и признание")

    gg "Ребята, я очень горжусь всеми вами. Мы сделали невероятную работу и достигли великолепных результатов. Наш проект получил признание от руководства, и они дали мне повышение."

    gg "Я хочу поблагодарить каждого из вас за ваше преданное трудолюбие и профессионализм. Мы сделали это вместе!"

    return

label bad_end:

    # Концовка Провал и извлечение уроков

    stop music fadeout 1
    play music sadend

    scene bg conference with fade
    
    "Когда наступает день презентации, проект сталкивается с серьезными проблемами и сбоями. Заказчик разочарован и отказывается продолжать сотрудничество с командой, считая их некомпетентными."

    scene bg bad end with fade
    show gg sad

    $ renpy.notify("Провал и извлечение уроков")

    gg "Я хочу поговорить с вами всеми. Мы все видели, что наш проект не достиг ожидаемых результатов, и я должен признать свою часть в этом провале. Я не справился с трудностями и не смог обеспечить поддержку, которую вам требовалось."

    gg "Но я хочу, чтобы вы знали, что я извлек множество уроков из этого опыта, и я обязуюсь стать лучшим руководителем, каким только могу быть. Прошу вас дать мне еще один шанс и продолжить работу над нашими проектами."

    return