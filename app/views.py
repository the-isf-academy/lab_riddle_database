from banjo.urls import route_get, route_post
from banjo.http import BadRequest
from .models import Riddle


@route_get('riddles/all')
def list_riddles(params):
    riddles = []

    for riddle in Riddle.objects.all():
        riddles.append(riddle.to_dict_answerless())

    return {'riddles':riddles}

@route_post('riddles/guess',args={'id':int,'guess':str})
def guess_answer(params):
    if 'guess' not in params or 'id' not in params:

        raise BadRequest('incorrect request')

    user_guess = params['guess']
    id = params['id']
    riddle = Riddle.objects.get(id=id)
    
    if riddle.check_guess(user_guess):
        print('hi')
        return {'correct':riddle.to_dict()}

    else:
        print(riddle.check_guess(user_guess))
        print(user_guess)
        print(riddle.to_dict_answerless())
        
        return {
            'correct': riddle.check_guess(user_guess),
            'guess': user_guess,
            'riddle':riddle.to_dict_answerless()
            }
