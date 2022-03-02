from django.db import models

class Stage(models.Model):
    stage_name = models.CharField(max_length=20) 

    def __str__(self):
        return self.stage_name


class Type(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name


class Attribute(models.Model):
    attribute_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.attribute_name


class Baby(models.Model):
    baby_name = models.CharField(max_length=20)
    baby_description = models.TextField()
    stage = models.ForeignKey(Stage,on_delete= models.CASCADE)
    typ = models.ForeignKey(Type,on_delete= models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete= models.CASCADE)

    def __str__(self):
        return self.baby_name


class Training(models.Model):
    training_name = models.CharField(max_length=20)
    training_description = models.TextField()
    stage = models.ForeignKey(Stage,on_delete= models.CASCADE)
    typ = models.ForeignKey(Type,on_delete= models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete= models.CASCADE)

    def __str__(self):
        return self.training_name


class Rookie(models.Model):
    rookie_name = models.CharField(max_length=30)
    rookie_description = models.TextField()
    stage = models.ForeignKey(Stage,on_delete= models.CASCADE)
    typ = models.ForeignKey(Type,on_delete= models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete= models.CASCADE)

    def __str__(self):
        return self.rookie_name


class Champion(models.Model):
    champion_name = models.CharField(max_length=30)
    champion_description = models.TextField()
    stage = models.ForeignKey(Stage,on_delete= models.CASCADE)
    typ = models.ForeignKey(Type,on_delete= models.CASCADE)
    attribute = models.ForeignKey(Attribute,on_delete= models.CASCADE)
    
    def __str__(self):
        return self.champion_name


class First(models.Model):
    baby = models.ForeignKey(Baby,on_delete= models.CASCADE)
    training = models.ForeignKey(Training,on_delete= models.CASCADE)

    def __str__(self):
        return self.pk


class Second(models.Model):
    training = models.ForeignKey(Training,on_delete= models.CASCADE)
    rookie = models.ForeignKey(Rookie,on_delete= models.CASCADE)

    def __str__(self):
        return self.pk


class Third(models.Model):
    rookie = models.ForeignKey(Rookie,on_delete= models.CASCADE)
    champion = models.ForeignKey(Champion,on_delete= models.CASCADE)

    def __str__(self):
        return self.pk