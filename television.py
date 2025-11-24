class Television:


    # Class variables (constants)
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize a Television object with default settings.

        Sets status and muted to False, volume to MIN_VOLUME, and channel to MIN_CHANNEL.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the television.

        Turns the TV on if it's off, or off if it's on.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggle the mute status of the television.

        Only works when the TV is on. Mutes if unmuted, unmutes if muted.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the channel by 1.

        Only works when the TV is on. Wraps to MIN_CHANNEL if at MAX_CHANNEL.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel by 1.

        Only works when the TV is on. Wraps to MAX_CHANNEL if at MIN_CHANNEL.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the volume by 1.

        Only works when the TV is on. Unmutes the TV if muted.
        Stays at MAX_VOLUME if already at maximum.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by 1.

        Only works when the TV is on. Unmutes the TV if muted.
        Stays at MIN_VOLUME if already at minimum.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the Television's current state.

        Returns:
            str: A formatted string showing Power status, Channel, and Volume.
                 When muted, Volume is displayed as 0.
        """
        display_volume = 0 if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"