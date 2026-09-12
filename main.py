import time


class Explorer:
    def __init__(self, name):
        self.name = name
        self.file = {
            '/': {
                'appfile': {
                    'tistcode001.ngg': '''
                    /INC [std,string]
                    /USING [std]
                    int main()
                    {
                        cout<<"hello world"<<turn;
                        endturn 0;
                    }
                    '''
                },
                'Document': {
                    'test.txt': 'hello world',
                    'test.txt1': 'hello world',
                    'test.txt2': 'hello world',
                    'test.txt3': 'hello world'
                }
            }
        }
    def Processing(self, command):
        if command[0:command.find(' ')] == 'cd':
            Temporary_peach = {}
            Temporary_peach = self.file['/']
            path = command[command.find(' ') + 1:].strip('/')
            for seg in path.split('/'):
                if seg:
                    Temporary_peach = Temporary_peach[seg]
            print(list(Temporary_peach.keys()))
            #print(Temporary_peach)


Explorer('root').Processing('cd /Document')
