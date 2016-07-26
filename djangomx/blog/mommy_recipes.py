from itertools import cycle

from model_mommy.recipe import Recipe

from .models import Post


POST_TITLES = [
    'Bacon ipsum dolor amet',
    'Turducken ham kevin',
    'Beef shoulder meatloaf boudin',
    'Ribeye kielbasa fatback shankle',
]

unique_post = Recipe(
    Post,
    title=cycle(POST_TITLES),
)
