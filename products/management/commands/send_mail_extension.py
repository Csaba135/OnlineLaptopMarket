from django.core.mail import send_mail

def send_mail_cheaper(price, title, email_list):
    send_mail(
        'One of your favorite product now is cheaper',
        f'The product is :{title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        email_list
    )

def send_mail_expensive(price, title, email_list):
    send_mail(
        'One of your favorite product now is getting expensive come and take it fast',
        f'The product is {title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        email_list
    )

def send_mail_same_price(price, title, email_list):
    send_mail(
        'One of your favorite product got an update',
        f'The product is {title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        email_list,
    )



