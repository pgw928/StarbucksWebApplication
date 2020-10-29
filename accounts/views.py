from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import User, Post, Comment
from datetime import datetime
from accounts.forms import PostForm, CommentForm
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import messages


def log_in(request):
    # post 방식
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        if User.objects.filter(user_id=user_id).exists() == True: # user_id 가 일치하면 True
            user = get_object_or_404(User, user_id=user_id)  # 변수 선언
            if user.password == password:
                request.session['user_id'] = user_id
                request.session['check'] = 1
                request.session['user_n'] = user.id
            else:
                messages.add_message(request, messages.INFO, '가입하지 않은 아이디이거나, 잘못된 비밀번호입니다.')
                return render(request, 'login.html')

        else:
            messages.add_message(request, messages.INFO, '가입하지 않은 아이디이거나, 잘못된 비밀번호입니다.')
            return render(request, 'login.html')

        return redirect('/')
    # get 방식
    return render(request, 'login.html')


def sign_up(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        request.session['tmp_flag'] = -1
        user_id = request.POST['user_id']  # 변수 선언
        if User.objects.filter(user_id=user_id).exists() == False:  # user_id 중복이 되면 False
        # password와 confirm에 입력된 값이 같다면
            if request.POST['password1'] == request.POST['password2']:
                # user 객체를 새로 생성
                user = User(user_id=request.POST['user_id'], password=request.POST['password1'],
                            user_name=request.POST['user_name'], phone_num=request.POST['phone_num'])
                user.save()
                request.session['user_id'] = user_id
                request.session['check'] = 0    # 로그인 성공시 화면 넘어가기


                return redirect('accounts:login')
            else :
                request.session['tmp_flag'] = 0
                messages.add_message(request, messages.INFO, '비밀번호가 일치하지 않습니다.')
                return redirect('/accounts/signup/')
        else:
            request.session['tmp_flag'] = 1
            messages.add_message(request, messages.INFO, '이미 존재하는 아이디입니다.')
            return redirect('/accounts/signup/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')


def log_out(request):
    request.session['check'] = 0
    del request.session['user_id']

    return redirect('/')


# def cash(request):
#     if request.method == 'POST':
#         user = get_object_or_404(User, user_id=request.session['user_id'])
#         user.point += int(request.POST['cash'])
#         user.save()
#         return redirect('/')
#
#     return render(request, 'cash.html')


def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    return render(request, 'list.html', {'list': my_list})


def p_create(request):

    if not request.session['check'] == 1:
        return HttpResponse('<script type="text/javascript">alert("로그인이필요합니다.");history.back(); '
                            '</script>')

    if request.method == 'POST':
        post = Post()
        post.author_id = request.session['user_n']
        post.title = request.POST['title']
        post.contents = request.POST['contents']
        post.qtype = request.POST['choice']
        post.created_date = datetime.now()
        post.save()
        return redirect('accounts:list')
        # return redirect('/accounts/list/')
        # post = Post(author=request.POST['author'], title=request.POST['title'], contents=request.POST['contents'])

    else:
        flag = False
        return render(request, 'create_voc.html', {"flag" : flag})


def p_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('accounts:list')


# def p_update(request, post_id):
#
#     post = get_object_or_404(Post, pk=post_id)
#     post
#
#     return redirect('accounts:list')

def p_update(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        post.author_id = request.session['user_n']
        post.title = request.POST['title']
        post.contents = request.POST['contents']
        post.qtype = request.POST['choice']
        post.created_date = datetime.now()
        post.save()
        return redirect('accounts:list')

    else:
        # 작성자 : 김은수

        flag = True

        comment = post.comment_set.all()
        comment.author = request.session['user_n']
        comment_form = CommentForm(request.POST)
        post_form = PostForm(instance=post)

        for i in post_form.fields:
            post_form.fields[i].disabled=True

        context = {'comment_list': comment, 'post': post, "flag": flag}

        return render(request, 'update.html',context)
    # ------------------------


    # if request.method == 'POST':
    #     post_form = PostForm(request.POST, instance=post)
    #
    #     if post_form.is_valid():
    #         post_form.save()
    #         return redirect('reviews:list')


def p_detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':

        comment = Comment()

        comment.text = request.POST['text']
        comment.post = post
        comment.created_date = datetime.now()
        comment.author = request.session['user_id']
        comment.save()

        return redirect(f'/accounts/{post_id}/detail/')

    else:
        comment = post.comment_set.all()
        comment.author = request.session['user_n']
        comment_form = CommentForm(request.POST)
        post_form = PostForm(instance=post)
        context = {'comment_list': comment, 'post_form': post_form, 'comment_form': comment_form, 'post': post}

        for i in post_form.fields:
            post_form.fields[i].disabled=True

        return render(request, 'detail.html', context)


def c_delete(request, comment_id, post_id):

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    path = "/accounts/{}/detail".format(post_id)
    return redirect(path)


# def hits(request, no=0):
#     if no == 0: return HttpResponseRedirect('list')
#
#     post = Post.objects.filter(id=no)
#     post.update(hit=F('hit')+1)
#     data = {
#         'post':post[0]
#     }
#     return render(request, 'accounts:list', data)



