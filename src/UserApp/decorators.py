from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def buyer_required(function=None,redirect_field_name=REDIRECT_FIELD_NAME,login_url='login'):
    '''
    Decorator for views that checks that the logged in UserApp is a Normal User,
    redirects to the log-in page if necessary.
    '''
    actual_decorator=user_passes_test(
        lambda u:u.is_active and u.is_user,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def seller_required(function=None,redirect_field_name=REDIRECT_FIELD_NAME,login_url='login'):
    '''
    Decorator for views that checks that the logged in UserApp is a seller,
    redirects to the log-in page if necessary.
    '''
    actual_decorator=user_passes_test(
        lambda u:u.is_active and u.is_seller,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# if UserApp purchase any product that time  UserApp this decoator
# write like below
# @login_required
# @user_required