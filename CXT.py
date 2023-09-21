
if __name__ == "__main__" :
  #load module
  import time,importlib,traceback,sys,os, threading as thing,json,shutil, inspect,webbrowser,subprocess,pydrive
  if os.name != "posix" :
    os.system("echo \033]0;CXT loading\007")
  module_path_folder = os.path.dirname(sys.argv[0])+"data\\cxtdata\\module"
  origi = sys.path.copy()
  sys.path.insert(0,module_path_folder)
  print("loading system [     ]",flush=True,end="\r")
  requests = importlib.import_module("requests")
  if os.name != "posix" :
    keyboard = importlib.import_module("keyboard")
    mouse = importlib.import_module("mouse")
    colorama = importlib.import_module("colorama")
    pygetwindow=importlib.import_module("pygetwindow")
    psutil = importlib.import_module("psutil")
  sys.path= origi
  #end
  #start varlibles
  print("loading system [—    ]",flush=True,end="\r")
  #standard
  self_path = os.path.dirname(sys.argv[0])
  builtin_mod_folder_path = self_path+"/data/cxtdata/builtin_mod"
  mod_folder_path = self_path+"/data/mod/"
  imported_program = {}
  imported_mod = {}
  debuging = False
  cache_file_path = self_path+"/data/cache"
  skiping = 0
  online_info = {}
  os_info = os.name
  
  #funcition
  def log(content="") :  
    if content:
      with open(self_path+"/data/log.txt","a") as f:
        f.write("[{}] {}\n".format (time.ctime(time.time()),content))
  def log_error(content="") :
    if content:
      with open(self_path+"/data/error_log.txt","a") as f :
        f.write("[{}] {}\n".format (time.ctime(time.time()),content))
  def show_command() :
    global imported_mod
    print("----HELP-COMMAND----")
    for i in imported_mod.items() :
      count= len(str(i[0])+" "*10)
      print(i[0]," "*10,type(i[1]).__name__)
      if debuging :
        print(" "*count,i[1])
  def dir_command(content="") :
    if content :
      global imported_mod
      if not content in imported_mod.keys() :
        return
      for i in dir(imported_mod[content]) :
        if not i.startswith("__") :
          print(i)
  def cles() :
    os.system("cls" if os.name == "nt" else "clear")
  def cxt_help() :
    print(online_info["guide"])
  def echo(*content) :
    if content :
      print(" ".join(content))
  def alert(content="",symbol="!!!") :
    print(f"[{symbol}]{content}[{symbol}]")
  def kill() :
    sys.exit()
  def adjustment() :
    print("type \"exit\" to exit from setting or cancel inputing value")
    while 1 :
      for i in setting.items() :
        print("setting name \"{}\"    value: \"{}\"".format(*i))
      print("clear_log")
      print("clear_errorlog")
      print("clear_cashe")
      try :
        _input = input("->")
      except KeyboardInterrupt :
        break
      value_to_set = _input[:]
      if _input in setting.keys() :
        type_of_setting = type(setting[_input])
        while 1 :
          _input = input("change {} as {} :".format(value_to_set,type_of_setting.__name__))
          if _input == "exit" :
            break
          try :
            setting[value_to_set]=eval(f"{type_of_setting.__name__}({_input})")
            with open(self_path+"/data/cxtdata/setting.json", "w",encoding="utf-8") as f :
              f.write(json.dumps(setting,indent=2))
            print("setting done")
            break
          except Exception as ex :
            print("formating error")
            print(ex)
      elif _input == "clear_log" :
        with open(self_path+"/data/log.txt","w") :
          ...
      elif _input == "clear_errorlog" :
        with open(self_path+"/data/error_log.txt","w") :
          ...
      elif _input == "clear_cashe" :
        cashe_path=self_path+"/data/cache"
        for item in os.listdir(cashe_path):
          item_path = os.path.join(cashe_path, item)
          os.remove(item_path)
      elif _input == "exit" :
        break
      else :
        print("no any function {} to trigger".format(_input))
  def show_icon() :
    print(cxt_icon)
  def restart() :
    os.system(sys.argv[0])
  def cxt_exec(_input="") :
    global self_path,builtin_mod_folder_path,builtin_mod_folder_path,mod_folder_path,skiping,imported_mod,imported_program,debuging,online_info,os_info
    def error_handler(func,*value) :
      try :
        if value :
          func(*value)
        else :
          func()
      except Exception as ex:
        print(f"function has been error\n{ex}")
        log_error(traceback.format_exc())
    if _input :
      command_line = _input.split()[0]
      command_list = command_line.split(setting["command_spliter"])
      first_cmd = command_list[0]
      value = _input.split(" ")[1:]
      if debuging :
        print("value varlible :",value)
      if first_cmd in list(imported_mod.keys()) :
        item = imported_mod[first_cmd]
        if len(command_list) >1:
          for i in command_list[1:] :
            if debuging:
              print(item)
            if str(i) in dir(item) :
              item = getattr(item,i)
              skiping = False
            else :
              alert(f"{i} is not in {first_cmd}")
              skiping = True
        if skiping :
          return
        if inspect.isfunction(item) :
          if any(inspect.signature(item).parameters) :
            count_empty = 0
            parameters_in_function = inspect.signature(item).parameters
            for i in parameters_in_function.items() :
              if i[1].default == inspect.Parameter.empty :
                count_empty += 1
            if len(value) >= count_empty and len(value) <= len(parameters_in_function):
              error_handler(item,*value)
            else: 
               alert("function get {0} varlible{2} but needed {1} varlible{3}".format(len(value),len(parameters_in_function),"s" if len(value) >1 else "","s" if len(parameters_in_function) > 1 else ""))
          else :
            error_handler(item)
        else :
          print(item)
      else :
        alert("no mod or built-in name \"{}\"".format(first_cmd))
  cxt_exit = kill
  
  #class
  class program :
    def run(content="") :
      global imported_program
      if content == "" :
        if content in imported_program.keys() :
          getattr(imported_program[content],"program")()
    def info() :
      for i in imported_program.keys() :
        try :
          print(i)
          print("---------------------------")
          print(imported_program[i].info)
          print("---------------------------\n")
        except :
          ...
  class debug :
    def check_mod() :
      global imported_mod
      print(imported_mod)
    def check_program() :
      global imported_program
      print(imported_program)
    def debug_toggle() :
      global debuging
      debuging = not debuging
      print("now debug is now ","enabled" if debuging == True else "disabled")
    def user_info() :
      print(f"os : {os.name}\ncurrent time : {time.ctime(time.time())}\nos time: {os.times()}\nCPU count : {os.cpu_count()}\nuser name : {os.getlogin()} | note : a furture for new version ig\ncurrent path running : {os.getcwd()}")
  class info :
    def update() :
      print(online_info["update"])
    def discord() :
      print(online_info["discord"])
    def creadit() :
      print(online_info["creadit"])
    def request() :
      print(online_info["request"])
    def join_discord() :
      webbrowser.open_new(online_info["discord"])
    def reload() :
      print("loading")
      loading =0
      load_able = True
      print("connecting website")
      try :
        web =requests.get("https://justpaste.it/bdjw6")
        print("connected")
      except Exception :
        print("can't load website")
        load_able = False
      if load_able :
        data=web.text
        for i in (("discord",9),("update",8),("creadit",9),("request",9),("guide",7)) :
          online_info[i[0]] = data[data.find(f"--{i[0]}")+i[1]:data.find(f"--/{i[0]}")].replace("\\n","\n")
          loading +=2.0
          print("process [{}]".format("".join(("—"*round(loading*2)," "*(20-round(loading*2))))),flush=True,end="\r")
        web.close()
        print()
        print("done reloading")
  #end
  print("loading system [——   ]",flush=True,end="\r")
  
  #load setting
  try : 
    with open(self_path+"/data/cxtdata/setting.json", "r") as f :
      setting=json.load(f)
  except Exception as ex :
    print("\nerror\nUnable to load settings")
    with open(self_path+"/data/error_log.txt","a") as f :
      log_error("{}\n{}\n".format(traceback.format_exc(),"—"*30))
    input()
    quit()
  with open(self_path+"/data/cxtdata/icon.txt","r") as f :
    cxt_icon = f.read()

  #end
  print("[———  ]",flush=True,end="\r")
  
  #load mod
  mod_error_while_importing = 0
  ori_path=sys.path.copy()
  sys.path.insert(0,mod_folder_path)
  
  ##start load internal mod
  for i in [debug,log,log_error,show_command,dir_command,cxt_help,echo,info,cles,cxt_exit,kill,alert,show_icon,restart,adjustment,cxt_exec,program] :
    imported_mod[i.__name__]=i
  ## end load
  
  ##start load  external builtin mod
  for i in os.listdir(mod_folder_path):
    if i.endswith(".py") :
      try :
        imported_mod[i.split(".")[0]]=(importlib.import_module(i.split(".")[0]))
      except Exception as ex:
        mod_error_while_importing+=1
  ##end load
  
  sys.path = ori_path
  ori_path=sys.path.copy()
  sys.path.insert(0,builtin_mod_folder_path)
  
  ##start load external mod
  for i in os.listdir(builtin_mod_folder_path):
    if i.endswith(".py") :
      try :
        imported_mod[i.split(".")[0]]=(importlib.import_module(i.split(".")[0]))
      except Exception as ex:
        mod_error_while_importing+=1
  ##end load
  
  sys.path = ori_path

  #end
  print("loading system [———— ]",flush=True,end="\r")
  
  #loading program
  origi = sys.path.copy()
  program_folder_path = self_path+"/data/program"
  sys.path.insert(0,program_folder_path)
  for i in os.listdir(program_folder_path) :
    path_program = os.path.join(program_folder_path,i)
    if os.path.isdir(path_program) :
      try :
        imported_program[i]=importlib.import_module(i)
      except :
        ...
  sys.path = origi
  #end

  print("loading system [—————]",flush=True)
  
  #load online data
  print("loading online data")
  loading =0
  load_able = True
  try :
    web = requests.get("https://justpaste.it/bdjw6")
  except Exception:
    print("can't load web")
    if os.name == "nt" :
      print("press [space] to continue as offline")
      keyboard.wait("space")
    else :
      print("auto skip load in 2 secs")
      time.sleep(2)
    load_able = False
  if load_able :
    data = web.text
    for i in (("discord",9),("update",8),("creadit",9),("request",9),("guide",7)) :
      online_info[i[0]] = data[data.find(f"--{i[0]}")+i[1]:data.find(f"--/{i[0]}")].replace("\\n","\n")
      loading +=2.0
      print("process [{}]".format("".join(("—"*round(loading*2)," "*(20-round(loading*2))))),end="\r",flush=True)
    print()
    web.close()
  #end
  
  #booting
  if os_info != "posix" :
    os.system("echo \033]0;CXT {}.{}.{}\007".format(setting["major_version"],setting["minor_version"],setting["micro_version"]))
  os.system("cls" if os.name == "nt" else "clear")
  print(cxt_icon)
  print("CXT version {}.{}.{}".format(setting["major_version"], setting ["minor_version"],setting["micro_version"]))
  if setting ["extra_sign_version"] :
    print(setting["extra_sign_version"])
  print("—–"*30)
  mod_boot_error=0
  for i in imported_mod.values() :
    if type(i).__name__ == "module" :
      try :
        euc = getattr(i,"program_event")
        getattr(euc,"on_program_boot")()
      except :
        mod_boot_error +=1
  if mod_boot_error :
    print("[ERROR {}]".format(mod_boot_error))
  print("—–"*30)
  print("use \"cxt_help\" for guide")
  _input = ""
  #end
  
  while 1:
    try :
     _input = input(setting ["input_sign"])
    except KeyboardInterrupt :
      sys.exit()
    except Exception :
      print("something went wrong")
      continue
    if _input:
      cxt_exec(_input)
