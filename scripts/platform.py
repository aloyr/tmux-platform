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
        cmd.append(run_param)

    p = Popen(cmd, stdout=PIPE)
    (data, err) = p.communicate()

def main()-> None:
    Popen(['tmux','display-message','loading project list'], stdout=PIPE).communicate()
    data = get_projects()
    make_menu(data)
    (selection, err) = Popen(['pbpaste'], stdout=PIPE).communicate()
    Popen(['tmux','display-message','project id: ' + selection.decode()], stdout=PIPE).communicate()

if __name__ == '__main__':
    main()

