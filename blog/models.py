from django.db import models
from django.utils.translation import gettext_lazy as _
from blog.abstract import BaseModel





#class Author(BaseModel):
 #   full_name = models.CharField(max_length=100)
  #  image = models.ImageField(upload_to='media/')

   # def str(self) -> str:
    #    return self.full_name
    
    #class Meta:
     #   verbose_name = _("full name")
      #  verbose_name_plural = _("full names")


#class Tags(BaseModel):
 #   name = models.CharField(max_length=100)

 #   def str(self) -> str:
   #     return self.name
  #  
    #class Meta:
     #   verbose_name=_("name")
      #  verbose_name_plural=_("names")
    
#class Post(BaseModel):
 #   title = models.CharField(max_length=100)
  #  body = models.TextField(max_length=100)
   # article = models.CharField(max_length=100)

    #author = models.ForeignKey(Author, on_delete = models.CASCADE)

    #tag = models.ManyToManyField(Tags)

    #def str(self) -> str:
     #   return self.title
    
    #class Meta:
     #   verbose_name=_("title")
      #  verbose_name_plural=_("titles")


#class Coment(BaseModel):
 #   name = models.CharField(max_length=100)
  #  email = models.EmailField()
   # comment = models.TextField()
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)

    #def str(self) -> str:
     #   return self.name
    
    #class Meta:
     #   verbose_name=_("name")
      #  verbose_name_plural=_("names")


class Author(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')


    def __str__(self) -> str:
     return self.full_name
    
    class Meta:
        verbose_name = _("full_name")
        verbose_name_plural = _("full_names")


class Tags(BaseModel):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name
 
    class Meta:
        verbose_name = _("name")
        verbose_name_plural = _("names")




class Post(BaseModel):
    title = models.CharField(max_length=100)  
    body = models.TextField()     
    # = models.CharField(widget=models.Textarea,label="IZOH")
    article = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    tag = models.ManyToManyField(Tags) #related_name='name')


    def __str__(self) -> str:
        return self.title #self.body, self.article, self.author, self.image, self.tag
    
    class Meta:
        verbose_name = _("title")
        verbose_name_plural = _("titles")






class Comment(BaseModel):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name #self.email, self.comment, self.post
    
    class Meta:
        verbose_name = _("name")
        verbose_name_plural = _("names")



        #verbose_name=_("full name") 
        #verbose_name=_("name"))
        #verbose_name=_("title")
        # verbose_name=_("article")
        #verbose_name=_("name")
