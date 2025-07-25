from django.db import models


#name, age, sex, 
class Member(models.Model):
    name= models.CharField(max_length =100, blank=False, null= False)
    age= models.IntegerField(blank= False, null= False)
    sex=models.CharField(max_length=10, blank= False, null= False)
    
    #yo chai family id nahalney ko lagi blannk =true rakheko 
    family_id=models.CharField(max_length=20, blank=True, null= True)
    
    #sabaile aafno l+ukauna milxa so eslai boolean type ma rakheko
    show_age=models.BooleanField(default=False)

    #yo function chai hamro name chai database ma herda dekhiyos vanera rakheko ho
    def __str__(self):

        return self.name