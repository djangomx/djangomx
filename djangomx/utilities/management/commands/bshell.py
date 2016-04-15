from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "bpython I prefer this shell, suckers"

    def handle(self, **options):
        from django.db.models.loading import get_models
        from bpython import cli
        for model in get_models():
            exec "from %s import %s" % (model.__module__, model.__name__)
        cli.main(args=[], locals_=locals())
