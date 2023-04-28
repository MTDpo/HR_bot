from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from hr_text import doc_links as link
inline_btn_0 = InlineKeyboardButton('↖️В начало', callback_data='inline_btn_0')


#=======================================Главное меню====================================================================

inline_btn_1 = InlineKeyboardButton('✅ВВОД В ПРОФЕССИЮ', callback_data='inline_btn_1')
inline_btn_2 = InlineKeyboardButton('🙎‍♂️Подбор персонала', callback_data='inline_btn_2')
inline_btn_3 = InlineKeyboardButton('📞Холодный звонок', callback_data='inline_btn_3')
inline_btn_4 = InlineKeyboardButton('👥Собеседование', callback_data='inline_btn_4')
inline_btn_5 = InlineKeyboardButton('🔹Работа с возражениями', callback_data='inline_btn_5')
inline_btn_05 = InlineKeyboardButton('📕 Учебные материалы', callback_data='inline_btn_05')

#=======================================# ✅ВВОД В ПРОФЕССИЮ============================================================

inline_btn_6 = InlineKeyboardButton('📃Кто такой HR менеджер?', url=link['inline_btn_6'])
inline_btn_7 = InlineKeyboardButton('🎦Видео о профессии HR', callback_data='inline_btn_7')
inline_btn_8 = InlineKeyboardButton('📃Массовый рекрутинг', url=link['inline_btn_8'])
inline_btn_9 = InlineKeyboardButton('🎦Видео о массовом рекрутинге', callback_data='inline_btn_9')
inline_btn_10 = InlineKeyboardButton('📃Бизнес-процесс работы HR', url=link['inline_btn_10'])
inline_btn_11 = InlineKeyboardButton('📖Книга "Внимание на HR"', url=link['inline_btn_11'])

#=======================================🙎‍♂️Подбор персонала=========================================================

inline_btn_12 = InlineKeyboardButton('😎 УТП', url=link['inline_btn_12'])
inline_btn_13 = InlineKeyboardButton('💫Ресурсы подбора персонала', callback_data='inline_btn_13')
inline_btn_14 = InlineKeyboardButton('📃Составление вакансии', callback_data='inline_btn_14')
inline_btn_15 = InlineKeyboardButton('📃Примеры вакансий', url=link['inline_btn_15'])
inline_btn_16 = InlineKeyboardButton('🎦Как набирать сотрудников? ', callback_data='inline_btn_16')
inline_btn_17 = InlineKeyboardButton('✅Отчет HR/GF.📊Нормативы набора', callback_data='inline_btn_17')

# 💫Ресурсы подбора персонала
headhunter = InlineKeyboardButton('👥HeadHunter', callback_data='headhunter')
avito = InlineKeyboardButton('🙋‍♀️Авито', callback_data='avito')
friend = InlineKeyboardButton('👫Программа “Приведи друга”', callback_data='friend')
vacancy_video = InlineKeyboardButton('🎦Ресурсы размещения вакансий (видео)', callback_data='vacancy_video')
# 👥HeadHunter
headhunter_vacancy = InlineKeyboardButton('🎦Head Hunter. Создание вакансии', callback_data='headhunter_vacancy')
headhunter_info = InlineKeyboardButton('🎦 Нead Hunter. Полезная информация', callback_data='headhunter_info')
# 📃Составление вакансии
make_vacancy = InlineKeyboardButton('Гугл документ', url=link['make_vacancy'])
make_vacancy_video = InlineKeyboardButton('🎦Видео по составлению вакансий', callback_data='make_vacancy_video')
#✅Отчет HR/GF.📊Нормативы набора
otchet_hr = InlineKeyboardButton('Отчет HR', url=link['otchet_hr'])
rasstanovka = InlineKeyboardButton('Расстановка', url=link['rasstanovka'])
min_norma = InlineKeyboardButton('📊Минимальная норма набора людей в неделю', url=link['min_norma'])

#=======================================# 📞Холодный звонок=============================================================

inline_btn_18 = InlineKeyboardButton('📃Телефонное интервью', url=link['inline_btn_18'])
inline_btn_19 = InlineKeyboardButton('📃Правила после звонка', url=link['inline_btn_19'])
inline_btn_20 = InlineKeyboardButton('📃Скрипт редакция от 09/21', url=link['inline_btn_20'])
inline_btn_21 = InlineKeyboardButton('📃Скрипты при звонке', url=link['inline_btn_21'])
inline_btn_23 = InlineKeyboardButton('🎦Видеоролики по ХЗ', callback_data='inline_btn_23')

# 🎦Видеоролики по ХЗ
poisk_candidate = InlineKeyboardButton('🎦Прямой поиск кандидатов', callback_data='poisk_candidate')
script_edu = InlineKeyboardButton('🎦Обучение по скриптам', callback_data='script_edu')
cold_call = InlineKeyboardButton('🎦Холодный звонок', callback_data='cold_call')
hh_autosearch = InlineKeyboardButton('🎦НН. Автопоиск и комментарии к резюме', callback_data='hh_autosearch')
superjob_search = InlineKeyboardButton('🎦Суперджоб.Информация, вакансии, поиск.', callback_data='superjob_search')

#=======================================# 👥Собеседование===============================================================

inline_btn_24 = InlineKeyboardButton('📃Алгоритм собеседования', url=link['inline_btn_24'])
inline_btn_25 = InlineKeyboardButton('📃Анкета кандидата', url=link['inline_btn_25'])
inline_btn_26 = InlineKeyboardButton('📃Основные моменты при собеседовании', url=link['inline_btn_26'])
#inline_btn_27 = InlineKeyboardButton('📃Пример собеседования', callback_data='inline_btn_27')
inline_btn_28 = InlineKeyboardButton('📃Проверка соискателей', url=link['inline_btn_28'])
inline_btn_29 = InlineKeyboardButton('🎦Правила при собеседовании', callback_data='inline_btn_29')
inline_btn_30 = InlineKeyboardButton('🎦Пример проведения собеседования', callback_data='inline_btn_30')
inline_btn_31 = InlineKeyboardButton('🗂Маркетинг-кит HR', url=link['inline_btn_31'])
inline_btn_32 = InlineKeyboardButton('🎦Работа в AmoCRM', callback_data='inline_btn_32')

# 🔹Работа с возражениями

inline_btn_33 = InlineKeyboardButton('Работа с возражениями', url=link['inline_btn_33'])
inline_btn_34 = InlineKeyboardButton('Обучение по работе с возражениями', callback_data='inline_btn_34')

#========================================# 📕 Учебные материалы=========================================================

inline_btn_35 = InlineKeyboardButton('🎓 Потоковое обучение', callback_data='inline_btn_35')
inline_btn_36 = InlineKeyboardButton('🌟Адаптация', callback_data='inline_btn_36')
inline_btn_37 = InlineKeyboardButton('☝️Увольнение', callback_data='inline_btn_37')
inline_btn_38 = InlineKeyboardButton('🌐Должностные инструкции сотрудников', url=link['inline_btn_38'])
inline_btn_39 = InlineKeyboardButton('🎥 Видеоролики компании', callback_data='inline_btn_39')
inline_btn_40 = InlineKeyboardButton('📖Список рекомендуемой литературы', url=link['inline_btn_40'])
inline_btn_41 = InlineKeyboardButton('😎Социальные сети', callback_data='inline_btn_41')

#Потоковое обучение
checklist_online_edu = InlineKeyboardButton('📃Чек-лист онлайн-обучения', url=link['checklist_online_edu'])
hr_metodichka = InlineKeyboardButton('🗂HR-методичка', callback_data='hr_metodichka')
raspisanie_rassilka = InlineKeyboardButton('📃Расписание.Рассылка в чаты.', callback_data='raspisanie_rassilka')
lection_materials = InlineKeyboardButton('🗂Материалы к лекциям', callback_data='lection_materials')
confa_zoom = InlineKeyboardButton('🎦Как пользоваться конференцией ZOOM?', callback_data='confa_zoom')
examen = InlineKeyboardButton('📃Экзамен', callback_data='examen')
test_examen = InlineKeyboardButton('📃Тесты к экзаменам', url=link['test_examen'])
interview_agent = InlineKeyboardButton('🎦Интервью агентов', callback_data='interview_agent')
agent_literature = InlineKeyboardButton('📖Литература для агентов', url=link['agent_literature'])

#🗂HR-методичка
hr_metodichka_doc = InlineKeyboardButton('Гугл документ', url=link['hr_metodichka_doc'])

#📃Расписание.Рассылка в чаты.
everyday_rassilka = InlineKeyboardButton('Ведение чатов со стажерами', url=link['everyday_rassilka'])
raspisanie_zanyati = InlineKeyboardButton('Расписание занятий', url=link['raspisanie_zanyati'])

#🗂Материалы к лекциям
materil_lections = InlineKeyboardButton('Гугл документы', url=link['materil_lections'])
zapisi1 = InlineKeyboardButton('Записи 06-10 сентября 1-2 группы', url=link['zapisi1'])
zapisi2 = InlineKeyboardButton('Ноябрь 2021', url=link['zapisi2'])

#🎦Как пользоваться конференцией ZOOM?
zoom_instruction_platform = InlineKeyboardButton('🎦Инструкция по платформе ZOOM', callback_data='zoom_instruction_platform')
zoom_instruction = InlineKeyboardButton('📃Инструкция ZOOM', url=link['zoom_instruction'])
zoom_pravila = InlineKeyboardButton('📃Правила общения в ZOOM', url=link['zoom_pravila'])

#📃Экзамен
exam_reglament = InlineKeyboardButton('Регламент приема экзамена', url=link['exam_reglament'])
exam_question = InlineKeyboardButton('Вопросы к экзамену по лекциям', url=link['exam_question'])
exam_material = InlineKeyboardButton('Материалы для подготовки к экзамену', url=link['exam_material'])

#🎦Интервью агентов
interview1 = InlineKeyboardButton('🎦Интервью Артема', callback_data='interview1')
interview2 = InlineKeyboardButton('🎦Интервью Марата', callback_data='interview2')
interview3 = InlineKeyboardButton('🎦Интервью Анастасии', callback_data='interview3')

#🌟Адаптация
adapt_aloritm = InlineKeyboardButton('📃Алгоритм адаптации', url=link['adapt_aloritm'])
adapt_list= InlineKeyboardButton('📃Адаптационный лист', url=link['adapt_list'])
adapt_stajor = InlineKeyboardButton('📃Чек-лист адаптации стажера', url=link['adapt_stajor'])
adapt_comand = InlineKeyboardButton('📃Формирование команды', url=link['adapt_comand'])
adapt_instrument = InlineKeyboardButton('📃Инструменты на сплочение коллектива', url=link['adapt_instrument'])
adapt_vipusknik = InlineKeyboardButton('📃Встреча выпускников', url=link['adapt_vipusknik'])
adapt_video = InlineKeyboardButton('🎦Видео по адаптации', callback_data='adapt_video')
adapt_motivation = InlineKeyboardButton('📃Нематериальная мотивация', url=link['adapt_motivation'])



#🎦Видео по адаптации
adapt_video_hr = InlineKeyboardButton('🎦Видео по адаптации от HR', callback_data='adapt_video_hr')
adapt_system = InlineKeyboardButton('🎦Система адаптации/ Игорь Рябов', callback_data='adapt_system')
adapt_stajor_uhod = InlineKeyboardButton('🎦Адаптация или почему стажеры уходят?', callback_data='adapt_stajor_uhod')
adapt_uskoren = InlineKeyboardButton('🎦Система ускоренной адаптации', callback_data='adapt_uskoren')
#☝️Увольнение

#uvolnenie_obhod = InlineKeyboardButton('📃Обходной лист', url='https://docs.google.com/document/d/1GEp24ZzCgIg8q12E6qoSTUZK7nfzsOc_/edit?usp=sharing&ouid=108154125398903504271&rtpof=true&sd=true')
#uvolnenie_interview = InlineKeyboardButton('📃Выходное интервью', url='https://docs.google.com/document/d/1nh1QRsxjMiSOaVLF3NvVPtTyxrDA2joK/edit?usp=sharing&ouid=108154125398903504271&rtpof=true&sd=true')
inline_btn_37_doc  = InlineKeyboardButton('Гугл документ', url=link['inline_btn_37_doc'])
inline_btn_37_video = InlineKeyboardButton('🎦Интервью на выходе', callback_data='uvolnenie_na_vihode')
#🎥 Видеоролики компании
video_work = InlineKeyboardButton('Работа в ОН Перспектива', callback_data='video_work')
video_what = InlineKeyboardButton('Что для Вас Перспектива24?', callback_data='video_what')
video_imidj = InlineKeyboardButton('Имиджевый ролик о компании', callback_data='video_imidj')
video_5_voprosov = InlineKeyboardButton('5 вопросов агенту по недвижимости', callback_data='video_5_voprosov')
video_presentation_2020 = InlineKeyboardButton('Презентация HR бренд платформы', callback_data='video_presentation_2020')
video_brand_platforma = InlineKeyboardButton('Бренд-платформа HR Презентация', callback_data='video_brand_platforma')
video_galochka = InlineKeyboardButton('Видео галочка', callback_data='video_galochka')
#Работа в ОН Перспектива
video_work_perspektiva = InlineKeyboardButton('Перспективная работа', callback_data='video_work_perspektiva')
video_work_on1 = InlineKeyboardButton('Работа в ОН Перспектива вариант 1', callback_data='video_work_on1')
video_work_on2 = InlineKeyboardButton('Работа в ОН Перспектива вариант 2', callback_data='video_work_on2')
#📖Список рекомендуемой литературы
literature_vnimanie_hr = InlineKeyboardButton('📖Внимание на HR', callback_data='literature_vnimanie_hr')
literature_plan_zahvat = InlineKeyboardButton('📖Книга продаж.План захват. Версия 2.0', callback_data='literature_plan_zahvat')
literature_edu_materials = InlineKeyboardButton('📖Книга продаж.Обучающие материалы.', callback_data='literature_edu_materials')
literature_recomendations = InlineKeyboardButton('📖Рекомендуем к прочтению', callback_data='literature_recomendations')
#😎Социальные сети
socseti_konferenci = InlineKeyboardButton('🎦Конференции', callback_data='socseti_konferenci')
konferenci_video = InlineKeyboardButton('Конференция от 02.12.2020', callback_data='konferenci_video')
konferenci_doc = InlineKeyboardButton('Документы к конференции', url='https://drive.google.com/drive/folders/1x2JAw5q1jzHrA9x5JVz6GoI-NQX10T1u?usp=sharing')
socseti = InlineKeyboardButton('🆔Социальные сети', callback_data='socseti')
socseti_kamaletdinov = InlineKeyboardButton('👔 Совещание РГ. Марат Камалтдинов', callback_data='socseti_kamaletdinov')
socseti_levchenko = InlineKeyboardButton('👔 Совещание агентов сети. М. Левченко', callback_data='socseti_levchenko')
#🆔Социальные сети
socseti_maketi = InlineKeyboardButton('📱Макеты вакансий для Instagram', url='https://drive.google.com/drive/folders/1FUwlPGWP_0D-ZBD1lLoIce0DwRCzkesB?usp=sharing')
socseti_guru_instagram = InlineKeyboardButton('🤴Гуру Instagram Эрнест Исмагилов', callback_data='socseti_guru_instagram')
ismagilov_text = InlineKeyboardButton('📃Рекомендации от Эрнеста Исмагилова', url='https://docs.google.com/document/d/1b8h8YDOGZTasM9TwwpwRpfRm02bjB1Ti/edit?usp=sharing&ouid=108154125398903504271&rtpof=true&sd=true')
ismagilov_video  = InlineKeyboardButton('🎦Социальные сети HRM. Э.Исмагилов', callback_data='ismagilov_video')
#Совещание РГ. Марат Камалтдинов
kamaletdinov_1 = InlineKeyboardButton('Обучение от 15.01.2021', callback_data='kamaletdinov_1')
kamaletdinov_2 = InlineKeyboardButton('Обучение от 22.01.2021', callback_data='kamaletdinov_2')
kamaletdinov_3 = InlineKeyboardButton('Обучение от 29.01.2021', callback_data='kamaletdinov_3')
kamaletdinov_4 = InlineKeyboardButton('Обучение от 05.02.2021', callback_data='kamaletdinov_4')
kamaletdinov_5 = InlineKeyboardButton('Обучение от 12.02.2021', callback_data='kamaletdinov_5')
kamaletdinov_6 = InlineKeyboardButton('Обучение от 26.02.2021', callback_data='kamaletdinov_6')
#Совещание агентов сети. М. Левченко
levchenko_1 = InlineKeyboardButton('Обучение от 15.01.2021', callback_data='levchenko_1')
levchenko_2 = InlineKeyboardButton('Обучение от 22.01.2021', callback_data='levchenko_2')
levchenko_3 = InlineKeyboardButton('Обучение от 29.01.2021', callback_data='levchenko_3')
levchenko_4 = InlineKeyboardButton('Обучение от 05.02.2021', callback_data='levchenko_4')
levchenko_5 = InlineKeyboardButton('Обучение от 12.02.2021', callback_data='levchenko_5')
levchenko_6 = InlineKeyboardButton('Обучение от 19.02.2021', callback_data='levchenko_6')
levchenko_7 = InlineKeyboardButton('Обучение от 26.02.2021', callback_data='levchenko_7')



#=======================================================================================================================
back_button = InlineKeyboardButton('⬅️Назад', callback_data="back_button")





class Keyboard:

    def inlinekey(self, option=None, parent=None):
        source_inline_menu = InlineKeyboardMarkup(row_width=1)
        if option == None or option == 'inline_btn_0':
            source_inline_menu.add(inline_btn_1).add(inline_btn_2).add(inline_btn_3).add(inline_btn_4).add(inline_btn_5).add(inline_btn_05)
        if option == 'inline_btn_1':
            source_inline_menu.add(inline_btn_6).add(inline_btn_7).add(inline_btn_8).add(inline_btn_9).add(inline_btn_10).add(inline_btn_11)
            raspisanie = InlineKeyboardButton('📌Расписание дня HR-менеджера📌', url=link['raspisanie'])
            source_inline_menu.add(raspisanie)
        if option == 'inline_btn_2':
            source_inline_menu.add(inline_btn_12).add(inline_btn_13).add(inline_btn_14).add(inline_btn_15).add(inline_btn_16).add(inline_btn_17)
        if option == 'inline_btn_3':
            source_inline_menu.add(inline_btn_18).add(inline_btn_19).add(inline_btn_20).add(inline_btn_21).add(inline_btn_23)
        if option == 'inline_btn_4':
            source_inline_menu.add(inline_btn_24).add(inline_btn_25).add(inline_btn_26).add(inline_btn_28).add(inline_btn_29).add(inline_btn_30).add(inline_btn_31).add(inline_btn_32)
        if option == 'inline_btn_5':
            source_inline_menu.add(inline_btn_33).add(inline_btn_34)
        if option == 'inline_btn_05':
            source_inline_menu.add(inline_btn_35).add(inline_btn_36).add(inline_btn_37).add(inline_btn_38).add(inline_btn_39).add(inline_btn_40).add(inline_btn_41)
        if option == 'inline_btn_37':
            source_inline_menu.add(inline_btn_37_doc).add(inline_btn_37_video)
        if option == 'inline_btn_12':
            utp_company = InlineKeyboardButton('УТП компании', url=link['utp_company'])
            utp_agent = InlineKeyboardButton('УТП при найме агента', url=link['utp_agent'])
            source_inline_menu.add(utp_company).add(utp_agent)
        if option == 'inline_btn_13':
            source_inline_menu.add(headhunter).add(avito).add(friend).add(vacancy_video)
        if option == 'inline_btn_14':
            source_inline_menu.add(make_vacancy_video)
        if option == 'inline_btn_17':
            source_inline_menu.add(otchet_hr).add(rasstanovka).add(min_norma)
        if option == 'headhunter':
            source_inline_menu.add(headhunter_vacancy).add(headhunter_info)
        if option == 'inline_btn_23':
            source_inline_menu.add(poisk_candidate).add(script_edu).add(cold_call).add(hh_autosearch).add(superjob_search)
        if option == 'inline_btn_35':
            source_inline_menu.add(checklist_online_edu).add(hr_metodichka).add(raspisanie_rassilka).add(lection_materials).add(confa_zoom).add(examen).add(test_examen).add(interview_agent).add(agent_literature)
        if option == 'confa_zoom':
            source_inline_menu.add(zoom_instruction_platform).add(zoom_instruction).add(zoom_pravila)
        if option == 'examen':
            source_inline_menu.add(exam_reglament).add(exam_question).add(exam_material)
        if option == 'hr_metodichka':
            source_inline_menu.add(hr_metodichka_doc)
        if option == 'raspisanie_rassilka':
            source_inline_menu.add(everyday_rassilka).add(raspisanie_zanyati)
        if option == 'lection_materials':
            source_inline_menu.add(materil_lections).add(zapisi1).add(zapisi2)
        if option == 'interview_agent':
            source_inline_menu.add(interview1).add(interview2).add(interview3)
        if option == 'inline_btn_36':
            source_inline_menu.add(adapt_aloritm).add(adapt_list).add(adapt_stajor).add(adapt_comand).add(adapt_instrument).add(adapt_vipusknik).add(adapt_video).add(adapt_motivation)
        if option == 'adapt_video':
            source_inline_menu.add(adapt_video_hr).add(adapt_system).add(adapt_stajor_uhod).add(adapt_uskoren)
        if option == 'inline_btn_39':
            source_inline_menu.add(video_work).add(video_what).add(video_imidj).add(video_5_voprosov).add(video_presentation_2020).add(video_brand_platforma).add(video_galochka)
        if option == 'video_work':
            source_inline_menu.add(video_work_perspektiva).add(video_work_on1).add(video_work_on2)
        if option == 'inline_btn_41':
            source_inline_menu.add(socseti_konferenci).add(socseti).add(socseti_kamaletdinov).add(socseti_levchenko)
        if option == 'socseti':
            source_inline_menu.add(socseti_maketi).add(socseti_guru_instagram)
        if option == 'socseti_guru_instagram':
            source_inline_menu.add(ismagilov_text).add(ismagilov_video)
        if option == 'socseti_konferenci':
            source_inline_menu.add(konferenci_video).add(konferenci_doc)
        if option == 'socseti_kamaletdinov':
            source_inline_menu.add(kamaletdinov_1).add(kamaletdinov_2).add(kamaletdinov_3).add(kamaletdinov_4).add(kamaletdinov_5).add(kamaletdinov_6)
        if option == 'socseti_levchenko':
            source_inline_menu.add(levchenko_1).add(levchenko_2).add(levchenko_3).add(levchenko_4).add(levchenko_5).add(levchenko_6).add(levchenko_7)
        if option == '':
            source_inline_menu.add()
        if option == '':
            source_inline_menu.add()
        if option == '':
            source_inline_menu.add()
        if option == '':
            source_inline_menu.add()
        if option in link:
            google_doc = InlineKeyboardButton('Гугл документы', url=f'{link[option]}')
            source_inline_menu.add(google_doc)
        if parent != None and option != 'inline_btn_0':
            source_inline_menu.add(back_button)
        if option != None and option != 'inline_btn_0':
            source_inline_menu.add(inline_btn_0)
        return source_inline_menu


#
#
