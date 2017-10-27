from __future__ import unicode_literals
from django.db import models
import re 
import bcrypt

class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {"errors": [], "status": False, "user": None}
        email_matches = self.filter(email = postData["email"])
        if len(email_matches) == 0:
            results["errors"].append("please check your email and password and try again")
            results["status"] = True
        else:
            results["user"] = email_matches[0]
            if not bcrypt.checkpw(postData["password"].encode(), results["user"].password.encode()):
                results["errors"].append("please check your email and password and try again")
                results["status"] = True
        return results

    def createUser(self, postData):
        password = hash1 = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())
        print password
        self.create(first_name = postData["first_name"], last_name = postData["last_name"], email = postData["email"], password = password)

    def registerVal(self, postData):
        results = {"errors": [], "status": False}

        if len(postData["first_name"]) < 2:
            results["status"] = True
            results["errors"].append("First name is too short")
        if len(postData["last_name"]) < 2:
            results["status"] = True
            results["errors"].append("Last name is too short")
        if len(postData["alias"]) < 2:
            results["status"] = True
            results["errors"].append("Alias name is too short")
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", postData["email"]):
            results["status"] = True
            results["errors"].append("Email is not valid")
        if len(postData["password"]) < 3:
            results["status"] = True
            results["errors"].append("Password is too short")
        if postData["password"] != postData["confirm_password"]:
            results["status"] = True
            results["errors"].append("Passwords do not match")
        if len(postData["date"]) < 8:
            results["status"] = True
            results["errors"].append("Birthday needs to be in mm/dd/yyyy format")

        user = self.filter(email = postData["email"])

        if len(user) > 0:
            results["status"] = True
            results["errors"].append("User already exists")    

        return results
class User(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    date = models.IntegerField(null=True)
    password = models.CharField(max_length=2255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
