import abc

class TerminalInterface(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def change_terminal(pokemon):
        raise NotImplementedError('users must define change_terminal to use this base class')     

    @abc.abstractmethod
    def clear_terminal():
        raise NotImplementedError('users must define clear_terminal to use this base class')

    @abc.abstractmethod
    def determine_terminal_pokemon():
        raise NotImplementedError('users must define determine_terminal_pokemon to use this base class')