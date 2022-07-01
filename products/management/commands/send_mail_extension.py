from django.core.mail import send_mail

def SendMailCheaper(price, title):
    send_mail(
        'One of your favorite product now is cheaper',
        f'The product is :{title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        ['testdjangoemailcsaba@gmail.com']
    )

def SendMailExpensive(price, title):
    send_mail(
        'One of your favorite product now is getting expensive come and take it fast',
        f'The product is {title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        ['testdjangoemailcsaba@gmail.com']
    )

def SendMailSamePrice(price, title):
    send_mail(
        'One of your favorite product got an update',
        f'The product is {title} and \n now the price is {price}',
        'testdjangoemailcsaba@gmail.com',
        ['testdjangoemailcsaba@gmail.com']
    )



