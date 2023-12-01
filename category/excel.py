
from .models import Category, Works, ChangeLog, Specialist
from .serializers import WorkSerializer, CatergorySerializer, SpecialistSerializer
from django.http import HttpResponse, JsonResponse
from legal.settings import BASE_DIR, STATIC_URL
import openpyxl
def parce_excel(request):
    path = BASE_DIR + STATIC_URL + 'Виды работ.xlsx'
    print('первый уровень')
    works = []
    groups = []
    doc = openpyxl.load_workbook(filepath)
    if len(doc.worksheets) == 0:
        print('no worksheets')
    sheet = doc.worksheets[0]
    print(sheet)
    cols = list(ascii_uppercase)
    end_row = max(list(map(lambda col: len(sheet[col]), cols)))
    print(end_row, 'энд роу')
    have_dates = False
    num_col = 'A'  # Столбец номера или наименования раздела
    name_col = 'B'  # Столбец для проверки по ГЭСН
    detail_col = 'C'
    #name_col = 'C'  # Столбец наименования
    count_type_col = 'D'  # Столбец единиц измерения
    hours_col = 'E'  # Столбец количества
    price_col = 'F'  # Столбец общей стоимости
    count_col = 'F'
    start_date_col = 'H'
    print('второй уровень')
    # start_date_col_num = 4
    # end_date_col = 'H'
    # end_date_col_num = 4
    # date_cols = {}  # Масив колонок плановых дат выполнения работы
    columns_count = 0
    for col in sheet.columns:
        columns_count += 1
    print(columns_count)
    # Найти шапку Таблицы
    row = 1
    while sheet[num_col + str(row)].value is None or 'Категория' not in sheet[name_col + str(row)].value and row < end_row:
        row += 1
    # Найти первый раздел
    # while sheet[num_col + str(row)].value is None or sheet[num_col + str(row)].value != 1 \
    #         and row < end_row:
    #     print(sheet[num_col + str(row)].value)
    #     row += 1
    start_row = row
    print(row, 'ров')
    print('treriy uroven')
    print('start_row', start_row)

    print('date_cols', date_cols)
    print('Текущая строка после обработки шапки: ' + str(row))
    print('На первом разделе')
    print('pytuy')
    # Ожидание, что нет пустых ячеек в колонке А в теле таблицы
    while row <= end_row and sheet[name_col + str(row)].value != None:
        #print(str(sheet[reason_col + str(row)].value), 'СМОТРИ СЮДА')
        #print('row:', row)
        name = sheet[name_col + str(row)].value
        name_or_num = sheet[num_col + str(row)].value
        try:
            name_or_num = int(name_or_num)
            building = True
        except:
            building = False
            if 'Категория' not in sheet[name_col + str(row)].value:
                dopoltinelno = True
            else:
                dopoltinelno =False
        #pattern = re.compile('раздел \d', re.IGNORECASE)
        #match = re.findall(pattern, name_or_num)
        if building == True:
            # Это здание
            # name = name_or_num.replace(match[0] + '.', '').strip()
            # num = int(match[0].lower().replace('раздел', ''))
            work_name = sheet[name_col + str(row)].value
            works.append({
                'name': name,
                'num': name_or_num
            })
            work = Works.objects.create(number=sheet[num_col + str(row)].value, name=work_name, hours=sheet[hours_col + str(row)].value, count=sheet[count_col + str(row)].value, )
            category.services.add(work)
        else:
            name = sheet[name_col + str(row)].value
            if dopoltinelno == True:
                category = Category.objects.create(name='Дополнительно - ' + name, isOriginal=dopoltinelno)
            else:
                category = Category.objects.create(name=name, isOriginal = dopoltinelno)
        row += 1
    #print('works', works)
    print(category)
    return groups, works