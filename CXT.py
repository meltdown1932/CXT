"""
made by Meltdown (known as kenjung)
version 2.0.0
Copyright © 2023 C.X.T.
"""
__version__ = "2.0.0"
if __name__ == "__main__" :
  import sys,os,importlib.util,importlib,time,traceback,inspect,json
  os.system("echo \033]0;CXT2\007")
  path_of_file = os.path.dirname(sys.argv[0])
  ori=sys.path.copy()
  error = 0
  debuging = 0


  #core
  class CXT:
    varlible = {} 
    mod_dict = {}
    program_dict = {}
    
    def __init__(cls):
      cls.mod_dict["CXT"]=CXT
      def echo(content) :
        print(content)
      cls.mod_dict["echo"]=echo
      global error
      ori = sys.path.copy()
      sys.path.insert(0,path_of_file+"/cxt/mod")
      for i in os.listdir(path_of_file+"/cxt/mod") :
        try : cls.mod_dict[i.split(".")[0]] = importlib.import_module(i.split(".")[0])
        except :
          error +=1
          print(f"ERROR detected at {i}")
          #F:\CXT\CXT\mod
          with open(path_of_file+"\\CXT\\log\\{}.txt".format(time.ctime(time.time()).replace(":"," ")),"a") as f:
            f.write(traceback.format_exc())
            f.write("\n")
      sys.path.insert(0,path_of_file+"/cxt/program")
      for i in os.listdir(path_of_file+"/cxt/program") :
        try : cls.program_dict[i] = importlib.import_module(i)
        except :
          error +=1
          print(f"ERROR detected at {i}")
          with open(path_of_file+"\\CXT\\log\\{}.txt".format(time.ctime(time.time()).replace(":"," ")),"a") as f:
            f.write(traceback.format_exc())
            f.write("\n")
      sys.path = ori
      if "__pycache__" in list(cls.mod_dict.keys()) :
        cls.mod_dict.pop("__pycache__")

    def mvalue(cls, name, value):
      try:
          cls.varlible[name] = eval(value)
      except (SyntaxError, NameError):
        if str(value) in list(cls.varlible.keys()):
          cls.varlible[name] = cls.varlible[value]
          print("set")
        else:
          print(f"There is no variable named {name}")
    
    def rvalue(cls,name) :
      if name in list(cls.varlible.keys()) :
        print( cls.varlible[name])

    def debug(cls) :
      print("program dict :",cls.program_dict)
      print("mod dict :",cls.mod_dict)
      print("varlible dict :",cls.varlible)
    
    def help(cls) :
      def walk(module_or_class, indent=2):
        print(module_or_class.__name__,type(module_or_class).__name__)
        for name, item in inspect.getmembers(module_or_class):
          if name.startswith("_") :
            continue
          if inspect.isclass(item):
            print((" " * indent)+"." + item.__name__)
            walk(item, indent + 2)
          else:
            print((" " * indent) + "." + name, type(item).__name__)
      print("--=CXT=-=help=command=--\n")
      print("-function/mod/class-list-")
      if cls.mod_dict.keys() :
        for key,args in cls.mod_dict.items() :
          walk(args)
      else :
        print("empty")
      
      print("\n-varlible-list-")
      for key,args in cls.varlible.items() :
        print(f"{key} {type(args).__name__}")
      if cls.mod_dict.keys() :
        for key,args in cls.varlible.items() :
          print(f"{key} {type(args).__name__}")
      else :
        print("empty")
      
      if cls.varlible.keys() :
        for key,args in cls.varlible.items() :
          print(f"{key} {type(args).__name__}")
      else : print("empty")
    def exec(cls,command) :
      if command  :
        fun = command.split()[0]
        if len(command.split()) > 1 :
          value = command.split()[1:]
        else :
          value = None
        first_command = fun.split(".")[0]
        if first_command in list(cls.mod_dict.keys()) :
          code = cls.mod_dict[first_command]
          for i in fun.split(".")[1:] :
            if hasattr(code,i) :
              code = getattr(code,i)
            else :
              print(f"there no {i} in {code}")
              return
          #arg checker
          if inspect.isfunction(code) :
            arg_count = 0
            arg_needed_value_count = 0
            is_function_have_cls = False
            for name,args in inspect.signature(code).parameters.items() :
              if name != "cls" :
                arg_count +=1
                if args.default == inspect.Parameter.empty :
                  arg_needed_value_count +=1
              else :
                is_function_have_cls = True
            if arg_count != 0 :
              if not value :
                print("function arguments is can't be empty")
                return
              if arg_needed_value_count == len(value) <= arg_count :
                if is_function_have_cls :
                  code(CXT,*value)
                else : code(*value)
            else :
              if is_function_have_cls :
                code(CXT)
              else:
                code()
          elif first_command in list(cls.varlible) :
            print(code)
        elif first_command in list(cls.varlible.keys()) :
          print(cls.varlible[first_command])
        else :
          print(f"there no function or varlible name {first_command}")
  CXT = CXT()
  #end

  #cmd reader
  if len(sys.argv) > 1 :
    for i in sys.argv[1:] :
      if i.startswith("-") :
        if i == "-bug" :
          debuging = not debuging
          print(f"now debug is {debuging}")
      elif os.path.isfile(i) :
        with open(i,"r") as f :
          code_line = f.readlines()
      else :
        print(f"{i} is not command or file path")
    is_manual = False
  else :
    is_manual = True

  #module
  internal_module = {}
  ori=sys.path.copy()
  sys.path.insert(0,path_of_file+"/CXT/data/module")
  requests = importlib.import_module("requests")
  keyboard = importlib.import_module("requests")
  mouse = importlib.import_module("requests")
  sys.path = ori
  #end

  if is_manual and __name__ == "__main__":

    for i in range(5) :
      print(f"loading attempt [{i+1}/5]")
      with open(path_of_file+"/cxt/data/cache/internet.txt","w",encoding="utf-8") as f :
        website = requests.get("https://raw.githubusercontent.com/meltdown1932/CXT/main/data/online.json",timeout = 5)
        if website.status_code == 200 :
          f.write(website.text)
          break
    with open(path_of_file+"/cxt/data/cache/internet.txt","r",encoding="utf-8") as f:
      online_data = json.loads(f.read())
    os.system("cls" if os.name == "nt" else "clear")
    if not online_data :
      print("CXT entered offline mode due can't load data")
      CXT_offline = True
    else :
      CXT_offline = False
    if not CXT_offline :
      print(online_data["icon"])
    print("CXT2\ntype \"discord\" \"update_log\" \"credit\" \"copyright\" for information")
    if __version__ != online_data["current version"] :
      print(f"CXT is out of date\n your current version {__version__}\nnew avalible version",online_data["current version"],"\ntype \"for update\"")
      outdate=False
    else :
      outdate=True
    while 1 :
      _input =input("X>")
      if _input.startswith("discord") :
        if not CXT_offline :
          print(online_data["discord"])
      elif _input.startswith("update_log") :
        if not CXT_offline :
          print(online_data["update"])
      elif _input.startswith("credit") :
        if not CXT_offline :
          print(online_data["credit"])
      elif _input.startswith("copyright") :
        if not CXT_offline :
          print(online_data["copyright"])
      elif _input.startswith("update") :
        if not CXT_offline :
          if outdate == True :
            os.startfile(path_of_file+"/CXT/updater.py")
          else :
            print("update update is unavalibie")
        else :print("CXT currently offline")
      else :
        CXT.exec(command=_input)
