from django.db import models

class Approach(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    score = models.FloatField()

    def __str__(self):
        return '[ID: %d, Approach: %s, Score: %f]' % (self.id, self.name, self.score)

class Tool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    score = models.FloatField()
    approach = models.ForeignKey(Approach, on_delete=models.CASCADE)

    def __str__(self):
        return '[ID: %d, Tool: %s, Score: %f, Approach: %s]' % (self.id, self.name, self.score, self.approach)

class Scale_Choice(models.Model):
    id = models.AutoField(primary_key=True)
    #----------
    TOTALLY_AGREE = 5
    AGREE = 4
    NEITHER_AGREE_NOR_DISAGREE = 3
    DISAGREE = 2
    TOTALLY_DISAGREE = 1

    SCALE_CHOICES = (
        (TOTALLY_AGREE, 'Totally Agree'),
        (AGREE, 'Agree'),
        (NEITHER_AGREE_NOR_DISAGREE, 'Neither agree nor disagree'),
        (DISAGREE, 'Disagree'),
        (TOTALLY_DISAGREE, 'Totally disagree'),
    )

    scale_choice_txt = models.CharField(max_length=30, default='null')

    scale_choice_value = models.PositiveIntegerField(
        choices = SCALE_CHOICES,
        default = TOTALLY_AGREE,
    )

    def __str__(self):
        return '[Choice: %s, Value: %d]' % (self.scale_choice_txt, self.scale_choice_value)

class Dicotomic_Choice(models.Model):
    id = models.AutoField(primary_key=True)
    #----------
    YES = 5
    NO = 1

    DICOTOMIC_CHOICES = (
        (YES, 'Yes'),
        (NO, 'No'),
    )

    dicotomic_choice_txt = models.CharField(max_length=5, default='null')

    dicotomic_choice_value = models.PositiveIntegerField(
        choices = DICOTOMIC_CHOICES,
        default = YES,
    )

    def __str__(self):
        return '[Choice: %s, Value: %d]' % (self.dicotomic_choice_txt, self.dicotomic_choice_value)

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    tool = models.ForeignKey(Tool,
                            null=True,
                            blank=True,
                            on_delete=models.CASCADE)
    approach = models.ForeignKey(Approach,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE
                                )


    #-----
    SCALE = 'scale'
    DICOTOMIC = 'dicotomic'

    type_choices = (
        (SCALE, 'Scale'),
        (DICOTOMIC, 'Dicotomic')
    )

    type = models.CharField(
        max_length=30,
        choices=type_choices,
        default=SCALE
    )

    def __str__(self):
        return '[ID: %d, Question: %s, Type: %s, Approach: %s, Tool: %s]' % (self.id, self.question_text, self.type, self.approach, self.tool)
