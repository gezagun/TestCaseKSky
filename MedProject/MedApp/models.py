from django.db import models


class Patient(models.Model):
    """Модель пациента"""

    Female = 'Female'
    Male = 'Male'
    fio = models.CharField(max_length=150, null=False, verbose_name='ФИО')
    birthday_date = models.DateField(verbose_name='Дата рождения', null=False)
    GENDERS = [(Female, 'Женский'), (Male, 'Мужской')]
    gender = models.CharField(max_length=7, choices=GENDERS, default=Male, null=False)

    def __str__(self):
        return self.fio


class TreatmentCase(models.Model):
    """Случай лечения"""

    Helped = 'Helped'
    Useless = 'Useless'
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент', null=False)
    start_date = models.DateField(auto_now_add=True, null=False, verbose_name='Дата начала лечения')
    end_date = models.DateField(verbose_name='Окончание лечения', null=True)
    RESULTS = [(Helped, 'Помогло'), (Useless, 'Не помогло')]
    result = models.CharField(max_length=11, choices=RESULTS, default=None, null=True)

    def __str__(self):
        return 'лечение ' + str(self.patient)


class MedDocument(models.Model):
    """Медицинский документ"""

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Пациент', null=False)
    treatment_case = models.ForeignKey(TreatmentCase, on_delete=models.CASCADE, verbose_name='Случай лечения',
                                       null=True)
    header = models.CharField(max_length=200, verbose_name='Заголовок', null=False)
    date = models.DateField(auto_now_add=True, verbose_name='Дата документа')

    def __str__(self):
        return str(self.patient) + ' ' + self.header


class DocumentBody(models.Model):
    """Тело документа"""

    document = models.OneToOneField(MedDocument, on_delete=models.CASCADE, null=False, verbose_name='Документ')
    content = models.JSONField(verbose_name='Содержание документа')

