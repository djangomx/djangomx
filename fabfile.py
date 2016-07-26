from fabric.api import runs_once, lcd, local, task


@task
@runs_once
def register_deployment(git_path):
    with(lcd(git_path)):
        revision = local('git log -n 1 --pretty="format:%H"', capture=True)
        branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
        local('curl https://intake.opbeat.com/api/v1/organizations/9652e6f850dd4856857cc34028a163a6/apps/9f9c5def57/releases/'
              ' -H "Authorization: Bearer 4c8c3b73ae8bf4c66945cceac29163752cabe53f"'
              ' -d rev="{}"'
              ' -d branch="{}"'
              ' -d status=completed'.format(revision, branch))
