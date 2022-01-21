"""
Bridge é um padrao de projeto estrutural que tem a intencao de desacoplar
ma abstracao da sua implementacao, de modo que as duas possam variar e evoluir
indepentemente.

Abstracao é uma camada de alto nivel para algo. Geralmente, a abstracao nao faz
nenhum trabalho por conta propria, ela delega parte ou todo o trabalho para a
camada de implementacao.

RELEMBRANDO: Adapter é um padrao de projeto estrutural que tem a intencao de
permitir que duas classes que seriam incompativeis trabalhem em conjunto
atraves de um "adaptador"

Diferença (GoF pag. 208) - A diferenca chave entre esses padroes está nas suas
intencoe ...
... O padrao Adapter faz as coisas funcionarem APOS elas terem sido projetadas;
o Bridge as faz funcionar ANTES QUE existam...
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: pass

    @abstractmethod
    def decrease_volume(self) -> None: pass

    @abstractmethod
    def power(self) -> None: pass


class RemoteControl(IRemoteControl):

    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power


class RemoteControlWithMute(RemoteControl):
    def mute(self) -> None:
        self._device.volume = 0


class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, volume: int) -> None: pass

    @property
    @abstractmethod
    def power(self) -> bool: pass

    @power.setter
    def power(self, power: bool) -> None: pass


class TV(IDevice):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

# ####################################################### #
# Fazer padrao state para retirar toda essa logica de ifs #
# ####################################################### #
    @volume.setter
    def volume(self, volume: int) -> None:
        if not self.power:
            print(f"Please, turn {self._name} ON.")
            return

        if volume > 100:
            return
        if volume < 0:
            return

        self._volume = volume
        print(f"Volume is now {self._volume}.")

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power
        power_status = "ON" if self._power else "OFF"

        print(f"{self._name} is now {power_status}")


class Radio(TV):
    ...


if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    remote = RemoteControl(tv)

    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.power()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()

    print()

    remote = RemoteControlWithMute(radio)

    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.power()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    print('MUTE')
    remote.mute()
