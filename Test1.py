import eel
import subprocess


eel.init('web')

@eel.expose
def test(query):
    output = subprocess.Popen(["howdoi",query], stdout = subprocess.PIPE, stderr=subprocess.PIPE)
    data,_ = output.communicate()
    data = str(data)[2:]
    data = data[:-1]
    result = data.replace('\\n',"<br />")
    eel.setResult(result)

eel.start('main.html',size=(1300,760))