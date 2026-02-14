from docxtpl import DocxTemplate

# Загрузка шаблона
doc = DocxTemplate("templates/123.docx")

# Данные для замены
context = {
    'lab_number': 1,  # Укажите номер лабораторной работы
    'var_number': 5      # Укажите вариант
}

# Замена меток данными
doc.render(context)

# Сохранение нового документа
doc.save("результат.docx")
