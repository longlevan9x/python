import cx_Freeze
executables = [cx_Freeze.Executable("game.py")]
cx_Freeze.setup(name = "Game debut",
			options = {"build_exe":{"packages":["pygame"],
					"include_files":["image/racecar1.png","sounds/crash.wav","sounds/jazz.wav"]}},
	executables=executables
	)