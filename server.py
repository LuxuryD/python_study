import asynchat
import asyncore

PORT = 6666

class EndSession(Exception):
    pass

class ChatServer(asyncore.dispatcher):
    '''
    chat server
    '''

    def __init__(self,port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)

class ChatSession(asynchat.async
