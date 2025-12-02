# 🎬 09-pjt : Axios 비동기 통신을 이용한 웹사이트 구현

![](/pjt/skeleton/images/1.png)

## 📌 프로젝트 개요

이 프로젝트는 Django 백엔드와 JavaScript를 활용한 AJAX 비동기 통신을 통해 새로고침 없이 데이터를 생성, 조회, 수정, 삭제할 수 있는 영화 추천 커뮤니티 서비스를 구현하는 것을 목표로 합니다. Axios를 사용하여 JSON 데이터를 주고받으며, 사용자 팔로우, 리뷰 좋아요, 영화 장르 필터링 등의 기능을 제공합니다.

---

## ⚙️ 주요 기능

| 구분         | 기능명                  | 설명                                                |
| ---------- | -------------------- | ------------------------------------------------- |
| 유저 팔로우 | 팔로우/언팔로우 기능             | AJAX를 이용한 새로고침 없는 팔로우 토글 기능                             |
| 리뷰 좋아요  | 좋아요/좋아요 취소 기능             | AJAX를 이용한 새로고침 없는 좋아요 토글 기능                  |
| 영화 필터링 | 장르별 영화 필터링             | 장르 선택 시 AJAX로 해당 장르의 영화만 동적 출력 |
| N:1 관계 | Review-User, Comment-User, Comment-Review       | ForeignKey를 활용한 1:N 관계 구현  |
| M:N 관계 | User-User (팔로우), Review-User (좋아요), Movie-Genre                | ManyToManyField를 활용한 M:N 관계 구현                         |

---

## 📋 구현 기능 및 기술

### 프로젝트 구조

```
skeleton/
├── accounts/           # 회원 관리 앱
│   ├── models.py      # User 모델 (팔로우 기능)
│   ├── views.py       # 회원가입, 로그인, 프로필, 팔로우
│   └── templates/
│       └── accounts/
│           ├── signup.html
│           ├── login.html
│           └── profile.html  # 팔로우 AJAX 구현
├── community/         # 리뷰 관리 앱
│   ├── models.py      # Review, Comment 모델
│   ├── views.py       # 리뷰 CRUD, 좋아요
│   └── templates/
│       └── community/
│           ├── index.html   # 좋아요 AJAX 구현
│           ├── create.html
│           └── detail.html
├── movies/            # 영화 관리 앱
│   ├── models.py      # Movie, Genre 모델
│   ├── views.py       # 영화 목록, 장르 필터링
│   └── templates/
│       └── movies/
│           ├── index.html   # 장르 필터링 AJAX 구현
│           └── recommended.html
├── mypjt/             # 프로젝트 설정
│   ├── settings.py
│   └── urls.py
└── .gitignore
```

---

## 전체 페이지

![](/pjt/skeleton/images/1.png)

---

### A. 유저 팔로우 기능 (F01)

![](/pjt/skeleton/images/2.png)

#### 백엔드 구현 (accounts/views.py)

- URL: `/accounts/<user_pk>/follow/`
- 메소드: POST
- 팔로우/언팔로우 토글 기능
- JSON 응답: `is_followed`, `followers_count`, `followings_count`
- 로그인 사용자만 접근 가능, 자기 자신 팔로우 불가

```python
@require_POST
@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)

    if request.user == person:
        return redirect('accounts:profile', person.username)

    if request.user in person.followers.all():
        person.followers.remove(request.user)
        is_followed = False
    else:
        person.followers.add(request.user)
        is_followed = True

    from django.http import JsonResponse
    return JsonResponse({
        'is_followed': is_followed,
        'followers_count': person.followers.count(),
        'followings_count': person.followings.count(),
    })
```

#### 프론트엔드 구현 (accounts/templates/accounts/profile.html)

- Axios를 사용한 비동기 POST 요청
- CSRF 토큰을 헤더에 포함하여 전송
- 응답 데이터로 버튼 텍스트와 팔로워/팔로잉 수 실시간 업데이트

```javascript
axios({
  method: 'post',
  url: `/accounts/${userPk}/follow/`,
  headers: {'X-CSRFToken': csrftoken},
})
  .then(response => {
    const isFollowed = response.data.is_followed
    const followBtn = document.querySelector('#follow-btn')

    if (isFollowed === true) {
      followBtn.value = 'Unfollow'
    } else {
      followBtn.value = 'Follow'
    }

    const followersCount = document.querySelector('#followers-count')
    const followingsCount = document.querySelector('#followings-count')
    followersCount.innerText = response.data.followers_count
    followingsCount.innerText = response.data.followings_count
  })
```

---

### B. 리뷰 좋아요 기능 (F02)

![](/pjt/skeleton/images/3.png)

#### 백엔드 구현 (community/views.py)

- URL: `/community/<review_pk>/like/`
- 메소드: POST
- 좋아요/좋아요 취소 토글 기능
- JSON 응답: `is_liked`, `likes_count`
- 로그인 사용자만 접근 가능
- 비인증 사용자 접근 시 401 에러와 에러 메시지 반환

```python
@require_POST
def like(request, review_pk):
    from django.http import JsonResponse

    # 로그인하지 않은 사용자 체크
    if not request.user.is_authenticated:
        return JsonResponse({
            'error': '로그인이 필요합니다.'
        }, status=401)

    review = Review.objects.get(pk=review_pk)

    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True

    return JsonResponse({
        'is_liked': is_liked,
        'likes_count': review.like_users.count(),
    })
```

#### 프론트엔드 구현 (community/templates/community/index.html)

![](/pjt/skeleton/images/4.png)

- 여러 리뷰의 좋아요 버튼을 `querySelectorAll`로 관리
- 각 폼에 `data-review-pk` 속성으로 리뷰 ID 저장
- 응답 데이터로 버튼 텍스트와 좋아요 수 실시간 업데이트
- 에러 처리: 401 에러 발생 시 alert로 에러 메시지 표시

```javascript
likeForms.forEach(form => {
  form.addEventListener('submit', function(event) {
    event.preventDefault()
    const reviewPk = event.target.dataset.reviewPk

    axios({
      method: 'post',
      url: `/community/${reviewPk}/like/`,
      headers: {'X-CSRFToken': csrftoken},
    })
      .then(response => {
        const isLiked = response.data.is_liked
        const likeBtn = event.target.querySelector('.like-btn')

        if (isLiked === true) {
          likeBtn.value = '좋아요 취소'
        } else {
          likeBtn.value = '좋아요'
        }

        const likesCount = event.target.parentElement.querySelector('.likes-count')
        likesCount.innerText = response.data.likes_count
      })
      .catch(error => {
        if (error.response && error.response.status === 401) {
          alert(error.response.data.error)
        } else {
          console.log(error.response)
        }
      })
  })
})
```

---

### C. 영화 장르 필터링 (F03)

![](/pjt/skeleton/images/5.png)

#### 백엔드 구현 (movies/views.py)

- URL: `/movies/filter-genre/`
- 메소드: GET
- Query Parameter: `genre_pk`
- 장르별로 영화를 필터링하여 JSON 배열로 반환
- `genre_pk`가 없으면 전체 영화 반환

```python
def filter_genre(request):
    genre_pk = request.GET.get('genre_pk')

    if genre_pk:
        movies = Movie.objects.filter(genres__pk=genre_pk)
    else:
        movies = Movie.objects.all()

    movies_data = []
    for movie in movies:
        movies_data.append({
            'id': movie.pk,
            'title': movie.title,
            'release_date': movie.release_date,
            'popularity': movie.popularity,
            'vote_count': movie.vote_count,
            'vote_average': movie.vote_average,
            'overview': movie.overview,
            'poster_path': movie.poster_path,
        })

    return JsonResponse({'movies': movies_data})
```

#### 프론트엔드 구현 (movies/templates/movies/index.html)

![](/pjt/skeleton/images/6.png)

- `<select>` 요소로 장르 선택 UI 구현
- 장르 변경 시 Axios GET 요청으로 필터링된 영화 목록 받아오기
- DOM API로 영화 목록 동적 생성 및 교체

```javascript
genreSelect.addEventListener('change', function(event) {
  const genrePk = event.target.value
  let url = '/movies/filter-genre/'

  if (genrePk) {
    url += `?genre_pk=${genrePk}`
  }

  axios({
    method: 'get',
    url: url,
  })
    .then(response => {
      const movies = response.data.movies
      moviesList.innerHTML = ''

      movies.forEach(movie => {
        const li = document.createElement('li')
        li.innerText = movie.title
        moviesList.appendChild(li)
      })
    })
})
```

---


## 💡 학습한 내용

1. **AJAX와 Axios**: Axios 라이브러리를 활용한 비동기 HTTP 통신
2. **JSON 데이터 처리**: Django에서 JsonResponse로 데이터 반환, JavaScript에서 파싱
3. **CSRF 보호**: Django의 CSRF 토큰을 AJAX 요청에 포함하는 방법
4. **Django ORM**: ManyToManyField의 `add()`, `remove()`, `filter()` 메소드 활용
5. **DOM 조작**: `querySelector`, `createElement`, `appendChild`를 활용한 동적 UI 업데이트
6. **이벤트 핸들링**: `addEventListener`와 `preventDefault()`를 통한 폼 제출 제어
7. **M:N 관계**: 팔로우(User-User), 좋아요(Review-User), 장르(Movie-Genre) 구현

---

## 🤔 어려웠던 부분

- CSRF 토큰을 Axios 요청 헤더에 포함시키는 방법을 처음에는 몰라서 403 에러가 발생했다. `X-CSRFToken` 헤더에 토큰을 추가해야 한다는 것을 배웠다.
- 여러 개의 좋아요 버튼을 관리할 때, 각 버튼이 어떤 리뷰에 속하는지 구분하기 위해 `data-` 속성을 사용하는 방법을 익혔다.
- JSON 응답에서 받은 데이터로 DOM을 업데이트할 때, 정확한 요소를 선택하는 것이 중요했다. 특히 반복문 안에서는 `event.target`을 기준으로 상대적으로 요소를 찾아야 했다.
- 비인증 사용자의 좋아요 처리: 로그인하지 않은 사용자가 좋아요를 누르면 "undefined 명이 이 글을 좋아합니다"라는 메시지가 표시되는 문제가 발생했다. `@login_required` 데코레이터는 AJAX 요청에 적합하지 않았고, 리디렉션 대신 JSON 에러 응답을 반환하도록 수동으로 인증 체크를 해야 했다. 또한 프론트엔드에서 `.catch()` 블록을 통해 401 에러를 감지하고 사용자에게 alert를 표시하는 에러 처리를 추가했다.

---

## 🌱 새로 배운 것

- **비동기 통신의 장점**: 페이지 새로고침 없이 사용자 경험을 향상시킬 수 있다는 점이 인상적이었다.
- **Django의 JsonResponse**: Python 딕셔너리를 자동으로 JSON으로 변환해주는 편리함
- **Axios의 Promise 체이닝**: `.then()`과 `.catch()`를 활용한 비동기 처리 패턴
- **M:N 관계 설계**: `symmetrical=False` 옵션으로 비대칭 팔로우 관계 구현
- **AJAX에서의 인증 처리**: `@login_required` 데코레이터는 일반 페이지에서는 로그인 페이지로 리디렉션하지만, AJAX 요청에서는 적절하지 않다. AJAX 요청에서는 `request.user.is_authenticated`로 수동 체크하고, HTTP 상태 코드(401 Unauthorized)와 함께 JSON 에러 메시지를 반환하는 것이 올바른 방법이다.
- **Axios 에러 핸들링**: `.catch()` 블록에서 `error.response.status`를 확인하여 HTTP 상태 코드별로 다른 에러 처리를 할 수 있다. 401 에러는 인증 문제, 403은 권한 문제, 500은 서버 에러 등으로 구분할 수 있다.

---

## ✨ 느낀 점

- AJAX를 사용하면 사용자 경험이 크게 향상된다는 것을 직접 체험할 수 있었습니다. 버튼을 클릭할 때마다 페이지 전체가 새로고침되지 않고 부분만 업데이트되는 것이 매우 인상적이었습니다.
- Django의 ORM과 JavaScript를 함께 사용하면서, 프론트엔드와 백엔드 간의 데이터 흐름을 명확히 이해하게 되었습니다.
- M:N 관계를 실제 서비스(팔로우, 좋아요)에 적용해보면서 데이터베이스 설계의 중요성을 체감했습니다.
