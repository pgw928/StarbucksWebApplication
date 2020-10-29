from django.shortcuts import render, redirect, get_object_or_404
from membership.models import Review, History
from accounts.models import User


def give_footer(request):
    reviews = Review.objects.all().order_by('-id')
    my_list2 = []
    j = 0
    for review in reviews:
        user = get_object_or_404(User, id=review.user_id)
        history = get_object_or_404(History, id=review.history_id)
        temp = (review, user, history)
        my_list2.append(temp)

        if j == 1:
            break
        j += 1
    return {'my_list2':my_list2}