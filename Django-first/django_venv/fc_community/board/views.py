from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Board
from .forms import BoardForm
from tag.models import Tag
from fcuser.models import Fcuser
# Create your views here.


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'board_detail.html', {'board': board})


def board_write(request):

    if not request.session.get('user'):
        return redirect('/fcuser/login')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():  # 검증
            # 검증이 된후 동작
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            for tag in tags :
              if not tag :
                  continue
            
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            _tag, _ = Tag.objects.get_or_create(tagname=tag)
            board.tags.add(_tag)



            return redirect('/board/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    # all() 전부 가져와서 order_by 로 내림차 , 오름차 순을 설정할 수 있다.
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 3)

    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})
