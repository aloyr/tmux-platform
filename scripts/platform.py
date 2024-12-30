from subprocess import Popen, PIPE

def get_projects()-> list[list[str]]:
    p = Popen(['platform','project:list','--no-header','--format=plain','--columns=id,title'], stdout=PIPE)
    (data, err) = p.communicate()
    return [x.split() for x in data.decode().strip().split('\n')]

def make_menu(projects: list[list[str]])-> None:
    cmd = [
            'tmux',
            'menu', '-T', 'Projects',
            '-x', 'R', '-y', 'S',
            '']

    for project in projects:
        cmd.append(project[1])
        cmd.append('')
        run_param = "run -b 'printf " + project[0] + " | pbcopy'"
        #run_param = "send-keys " + project[0]
        cmd.append(run_param)

    p = Popen(cmd, stdout=PIPE)
    (data, err) = p.communicate()

def login()-> bool:
    Popen(['tmux','display-message','determining login status'], stdout=PIPE).communicate()
    (stdout, stderr) = Popen(['platform', 'auth:info'], stdout=PIPE, stderr=PIPE).communicate()
    if len(stderr) > 0:
        Popen(['tmux','display-message','-d', '0', 'Error: Not logged in. Please login with "platfom auth:browser-login" first'], stdout=PIPE).communicate()
        return False
    return True


def main()-> None:
    if login():
        Popen(['tmux','display-message','loading project list'], stdout=PIPE).communicate()
        data = get_projects()
        make_menu(data)
        (selection, err) = Popen(['pbpaste'], stdout=PIPE).communicate()
        Popen(['tmux','display-message','-d', '0', 'project id: ' + selection.decode() + ' copied to pasteboard'], stdout=PIPE).communicate()

if __name__ == '__main__':
    main()

