import pytest
from television import Television


# Tests for __init__ method
def test_init():
    """Test the status, channel, and volume values after initialization."""
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


# Tests for power method
def test_power_on():
    """Test the tv details when the tv is on."""
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_power_off():
    """Test the tv details when the tv is off."""
    tv = Television()
    tv.power()
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


# Tests for mute method
def test_mute_on_volume_increased_then_muted():
    """Test the tv details when the tv is on, volume increased once, and then tv muted."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_mute_on_and_unmuted():
    """Test the tv details when the tv is on and unmuted."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_mute_off_and_muted():
    """Test the tv details when the tv is off and muted."""
    tv = Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute_off_and_unmuted():
    """Test the tv details when the tv is off and unmuted."""
    tv = Television()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


# Tests for channel_up method
def test_channel_up_off():
    """Test the tv details when the tv is off and the channel has been increased."""
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_channel_up_on():
    """Test the tv details when the tv is on and the channel has been increased."""
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"


def test_channel_up_past_maximum():
    """Test the tv details when the tv is on and one has increased the channel past the maximum value."""
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


# Tests for channel_down method
def test_channel_down_off():
    """Test the tv details when the tv is off and the channel has been decreased."""
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_channel_down_past_minimum():
    """Test the tv details when the tv is on and one has decreased the channel past the minimum value."""
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"


# Tests for volume_up method
def test_volume_up_off():
    """Test the tv details when the tv is off and the volume has been increased."""
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_volume_up_on():
    """Test the tv details when the tv is on and the volume has been increased."""
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_up_on_muted():
    """Test the tv details when the tv is on, muted, and the volume has been increased."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_up_past_maximum():
    """Test the tv details when the tv is on and one has increased the volume past the maximum value."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


# Tests for volume_down method
def test_volume_down_off():
    """Test the tv details when the tv is off and the volume has been decreased."""
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_volume_down_on():
    """Test the tv details when the tv is on and the volume has been decreased."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_down_on_muted():
    """Test the tv details when the tv is on, muted, and the volume has been decreased."""
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_down_past_minimum():
    """Test the tv details when the tv is on and one has decreased the volume past the minimum value."""
    tv = Television()
    tv.power()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"