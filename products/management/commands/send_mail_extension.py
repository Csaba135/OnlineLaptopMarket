from django.core.mail import send_mail

def SendMailCheaper(price, title, email_list):
    send_mail(
        'One of your favorite product now is cheaper',
        f'The product is :{title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        email_list
    )

def SendMailExpensive(price, title, email_list):
    send_mail(
        'One of your favorite product now is getting expensive come and take it fast',
        f'The product is {title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        email_list
    )

def SendMailSamePrice(price, title, email_list):
    send_mail(
        'One of your favorite product got an update',
        f'The product is {title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        email_list,
    )



