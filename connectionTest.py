import ConectionManager as Connection

conn = Connection.Connection()

conn.sendCommand('move', 'stop')

conn.sendCommand('freq', 50)
conn.sendCommand('move', 'left')

conn.disconnect()


