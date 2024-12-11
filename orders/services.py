from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email_order(product_order, send_to):
    recipient_list = [send_to]
    subject = "Новый заказ"
    context = {
        'user_name': product_order.user.name,
        'order_items': product_order.order_items.all(),
        'total_quantity': product_order.count(),
        'total_sum': product_order.total_sum(),
        'order_date': product_order.date,
        'comments_on_order': product_order.comments_on_order,
        'delivery_on_order': product_order.delivery_on_order,
        'phone_number': product_order.phone_number,
        'lift': product_order.lift,
    }
    text_content = f"""
      Заказ от {product_order.user.name}
      Детали заказа:
      - Продукт/ы: {', '.join([f"{product.product.title} ({product.product.artikul})" for product in product_order.order_items.all()])}
      - Количество: {product_order.count()}
      - Сумма: {product_order.total_sum()} рублей
      - Дата заказа: {product_order.date}
      - Комментарии к заказу: {product_order.comments_on_order}
      - Комментарии к доставке: {product_order.delivery_on_order}
      - Номер телефона: {product_order.phone_number}
      - Лифт: {product_order.lift}
      """

    html_content = render_to_string('email_templates/order_email.html', context)
    email = EmailMultiAlternatives(
        subject,
        text_content,
        'info@parket-promax.ru',
        recipient_list
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


def send_email_service(service_order, send_to):
    recipient_list = [send_to]
    subject = "Новый заказ"

    context = {
        'user_name': service_order.name,
        'ordered_service': service_order.service.title,
        'total_sum': service_order.price.price,
        'order_date': service_order.date,
        'comments_on_order': service_order.comments_on_order,
        'delivery_on_order': service_order.delivery_on_order,
        'phone_number': service_order.phone_number,
        'lift': service_order.lift
    }
    text_content = f"""
      Заказ услуги от {service_order.name}
      Детали заказа:
      - Наименование услуги: {service_order.service.title}
      - Сумма: {service_order.price.price} рублей
      - Дата заказа: {service_order.date}
      - Комментарии к заказу: {service_order.comments_on_order}
      - Комментарии к доставке: {service_order.delivery_on_order}
      - Номер телефона: {service_order.phone_number}
      - Подъем: {service_order.lift}
       """

    html_content = render_to_string('email_templates/order_service.html', context)
    email = EmailMultiAlternatives(
        subject,
        text_content,
        'info@parket-promax.ru',
        recipient_list
    )
    email.attach_alternative(html_content, "text/html")
    email.send()


def send_email_express(express_calc, send_to):
    recipient_list = [send_to]
    subject = "Новый экспресс расчет"

    context = {
        'user_name': express_calc.name,
        'squared_metres': express_calc.squared_metres,
        'parquet_age': express_calc.parquet_age,
        'phone_number': express_calc.phone_number,
        'date': datetime.now().date()
    }
    text_content = f"""
      Заказ экспресс расчета от {express_calc.name}
      Детали заказа:
      - Возраст паркета: {express_calc.parquet_age}
      - Квадратные метры: {express_calc.squared_metres}
      - Номер телефона: {express_calc.phone_number}
      - Дата: {datetime.now().date()}
       """

    html_content = render_to_string('email_templates/order_express_calc.html', context)
    email = EmailMultiAlternatives(
        subject,
        text_content,
        'info@parket-promax.ru',
        recipient_list
    )
    email.attach_file(express_calc.photo.path)
    email.attach_alternative(html_content, "text/html")
    email.send()