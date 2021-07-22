from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import dbus.service
import os
import re

DBusGMainLoop(set_as_default=True)

objpath = "/KRunnerAlias"
iface = "org.kde.krunner1"

class Alias:
    def __init__(self,name,command):
        self.name = name
        self.command = command

class Runner(dbus.service.Object):
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.service.BusName(
            "org.kde.KRunnerAlias", dbus.SessionBus()), objpath)
        self.aliases = {}
        self.initAliases()
        
    def initAliases(self):
        bashrcPath = os.path.expanduser("~/.bashrc")
        bashrc = open(bashrcPath,"r")
        bashrcLines = bashrc.readlines()
        for line in bashrcLines:
            try:
                parsed = re.search('alias ([^ =]+)=([^\s].+)', line)
                name = parsed.group(1)
                command = re.search('(?<=\')(.+)(?=\'[ ]*$|\'[ ]*#)|(?<=")(.+)(?="[ ]*$|"[ ]*#)|^(?!["\'#])(\S+(?=[ ]*#)|\S+$)',parsed.group(2))
                if(command):
                    self.aliases[name] = (Alias(name,command.group(0)))
            except AttributeError as e:
                pass

    @dbus.service.method(iface, in_signature="s", out_signature="a(sssida{sv})")
    def Match(self, originalQuery: str):
        query = originalQuery.split(" ",1)
        if(query[0] in self.aliases):
            if(len(query) == 1):
                return [(self.aliases[query[0]].command, "Run alias: " + query[0], "Terminal", 100, 100, {}), ]
            else:
                return [(self.aliases[query[0]].command + " " + query[1], "Run alias: " + query[0] + " with supplied arguments.", "Terminal", 100, 100, {}), ] 
        else:
                return [(originalQuery, "Run: " + originalQuery, "Terminal", 0, 0, {}), ]


    @dbus.service.method(iface, in_signature="ss")
    def Run(self, data: str, action_id: str):
        os.system(data)


runner = Runner()
loop = GLib.MainLoop()
loop.run()
