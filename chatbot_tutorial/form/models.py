from django.db import models



class Feedback(models.Model):
    details = models.TextField(max_length=40)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name