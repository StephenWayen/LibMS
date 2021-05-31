"""
Django settings for LibMS project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l@ix*j1!doyb5uv0hj2rw22lt#rv=t4y$0&to(5!q-neojmvv$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_crontab',
    'libapp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibMS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibMS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'LibMS',
            'HOST': '124.70.221.131',
            'PORT': 3306,
            'USER': 'admin',
            'PASSWORD': 'Adg23456789.',
        }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", "/")    #设置静态文件路径为主目录下的media文件夹
MEDIA_URL = '/media/'

SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_ACTION = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True  # 是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = False  # 是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.163.com'  # 发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 25  # 发件箱的SMTP服务器端口

# 上面配置可以不动，下面配置修改为自己的

EMAIL_HOST_USER = 'shu_libms@163.com'  # 发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'RQHHZFSKZFSDZPOH'  # 发送邮件的邮箱密码(这里使用的是授权码)
EMAIL_TO_USER_LIST = ['xxxx@foxmail.com', 'xxx@qq.com']   # 此字段是可选的，用来配置收件人列表


SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menu_display': ['读者账号', '图书/CIP', '借阅/预约', '权限认证', ],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
    'menus': [
        {
        'name': '读者账号',
        'models': [{
            'name': '个人账号',
            'url': 'libapp/user',
        }, {
            'name': '个人信息',
            'url': 'libapp/reader',
        }]
    }, {
        'name': '图书/CIP' ,
        'models': [{
            'name': 'CIP管理',
            'url': 'libapp/cip',
        },{
            'name': '图书管理',
            'url': 'libapp/books',
        }]
    }, {
        'name': '借阅/预约' ,
        'models': [{
            'name': '借阅图书',
            'url': 'libapp/bookslips',

        },{
            'name': '预约图书',
            'url': 'libapp/reservations',
        },{
            'name': '借阅逾期',
            'url': 'libapp/fines',
        }]
    },{
        'app': 'auth',
        'name': '权限认证',
        'models': [{
            'name': '用户',
            'url': 'auth/user/'
        }]
    }]
}

CRONJOBS = [
    # 每小时执行一次
    ('0 * * * *', 'libapp.views.timingTask')
]