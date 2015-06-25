from fabric.api import local, run, cd, env, prefix

env.hosts = ['188.226.158.212']

VIRTUAL_ENV = '/apps/wordgame/bin/activate'
PROJECT_DIR = '/apps/wordgame/wordgame/'


def mc():
    local('./manage.py schemamigration wordgame --auto')


def migrate():
    local('./manage.py migrate')


def runs():
    local('./manage.py runserver 127.0.0.1:8020')


def commit():
    local('git add -p && git commit')


def push():
    local('git push')


def prepare():
    # test()
    commit()
    push()


def deploy():
    # prepare()

    with cd(PROJECT_DIR):
        with prefix('source %s' % VIRTUAL_ENV):
            run('git pull')
            run('./manage.py migrate')
            run('sudo supervisorctl restart wordgame')


def pd():
    prepare()
    deploy()


def restart():
    run('sudo supervisorctl restart wordgame')
