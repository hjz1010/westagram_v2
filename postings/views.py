import json
from django.http import JsonResponse
import jwt

from django.views import View
from django.conf  import settings

from users.models    import User
from postings.models import Posting

class PostingView(View):

    def post(self,request):
        '''
        목적: 사용자가 입력한 게시글을 데이터베이스에 저장한다.

        1. client에서 받아온 데이터에서 token을 통해 사용자를 확인한다.
        2. 받아온 데이터에서 image, contents 를 확인한다.
        3. DB에 게시자(사용자), 이미지, 게시글, 게시 시간을 저장한다.
        '''
        data = json.loads(request.body)
        '''
        request.body = {
            'access_token' = 'eyJ0eXAiOiiJ9.eyJpZCI6MX0.-xXA0iObF54J9lj2RwduAI'
            'image'        = 'https://t1.ddfasdfn.net/tranor/image/og-image.png,
            'contents'     = 'my favorite'
        }
        '''
        try: 
            access_token = data['access_token']
            image        = data['image']
            contents     = data['contents']

            header = jwt.decode(access_token, settings.SECRET_KEY, 'HS256')
            # print(header)  # {'user_id':5}
                        
            Posting.objects.create(
                user     = User.objects.get(id = header['user_id']),
                image    = image,
                contents = contents
            )
        
            return JsonResponse({'message': 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except jwt.InvalidTokenError:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=401)
