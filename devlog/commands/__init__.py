from kao_command import Commands

commands = Commands(__name__, {None: 'new_log.NewLog',
                               'set': {'dir': 'set_dir.SetDir',
                                       'editor': 'set_editor.SetEditor'}})