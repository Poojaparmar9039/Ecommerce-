from django.db import models

class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="shop/images",default="")

    
    def __str__(self):
        return self.product_name
    
class address(models.Model):
    user_id=models.AutoField
    name=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    block=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.IntegerField()
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
   
    def __str__(self):
        return self.name


class order_details(models.Model):
    order_no = models.AutoField(primary_key=True)  
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    order_date = models.DateField(auto_now_add=True)  

    def __str__(self):
        return f"Order: {self.product_name}"

   

class delivery_update(models.Model):
    order = models.ForeignKey(order_details, on_delete=models.CASCADE, related_name="updates")
    update_desc=models.CharField(max_length=500)
    timestamp=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc