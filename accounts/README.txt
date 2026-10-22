یک درخواست جدید بساز
متد رو روی POST بذار و آدرس رو بنویس:

1) http://127.0.0.1:8000/api/account/register/

بدنه (Body) رو تنظیم کن
تب Body رو باز کن.
گزینه raw رو انتخاب کن.
از منوی کشویی کنارش JSON رو بذار.

اطلاعات کاربر رو بنویس
json
{
  "username": "kia",
  "email": "kia@test.com",
  "password": "Test12345"
}

روی Send بزن

اگه درست باشه، وضعیت 201 Created و چیزی شبیه این برمی‌گرده:

json
{
  "username": "kia",
  "email": "kia@test.com"
}

-----------------------------------------

وارد شو (login)

حالا مثل مرحله قبل، یک درخواست POST به این آدرس بفرست:

2) http://127.0.0.1:8000/api/account/login/

با بدنه:

json
{
  "username": "kia",
  "password": "Test12345"
}

توکن رو دریافت می‌کنی.

-----------------------------------------

یک درخواست GET به این آدرس بفرست:

3) http://127.0.0.1:8000/api/account/me/

و توی تب Headers این رو اضافه کن:

Key: Authorization
Value: Token <توکن_خودت>