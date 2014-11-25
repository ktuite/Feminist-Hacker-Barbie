from django.db import models

class BarbiePage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    image_path = models.TextField()
    original_text =  models.TextField(blank=True)
    width = models.IntegerField()
    height = models.IntegerField()
    text_x = models.IntegerField()
    text_y = models.IntegerField()
    text_w = models.IntegerField()
    text_h = models.IntegerField()

    def __str__(self):
        return "Page %d: %s [%s]" % (self.id, self.name, self.image_path)

    def simple(self):
        return dict(
            id=self.id, 
            name=self.name, 
            image_path=self.image_path, 
            original_text=self.original_text, 
            width=self.width,
            height=self.height,
            text_x=self.text_x,
            text_y=self.text_y,
            text_w=self.text_w,
            text_h=self.text_h,
            )

class Adaptation(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.ForeignKey(BarbiePage) 
    new_text = models.TextField()
    imgur_id = models.TextField()
    endorsed = models.BooleanField(default=False)
    flagged = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return "Page %d: %s [%s]" % (self.page.id, self.new_text, self.imgur_id)


