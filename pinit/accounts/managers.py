from django.contrib.auth.models import BaseUserManager,AbstractUser


class UserManager(BaseUserManager):

    def create_user(self, email, username, password,first_name,last_name):
        if not email:
            raise ValueError('Email is required!')
        if not username:
            raise ValueError('full name is required!')

        user = self.model(email=self.normalize_email(email), username=username,first_name=first_name, last_name = last_name)
        user.set_password(password)
        user.save(using=self.db)
        # profile = Profile(
        #     user = user,
        #     fname = first_name,
        #     lname = last_name
        # )
        # profile.save()
        # board = Board(
        #     User=user,
        #     title="profile"
        # )
        # board.save()
        return user
    
#declaring custom user
# class CustomUser(AbstractUser):
#     objects = UserManager()