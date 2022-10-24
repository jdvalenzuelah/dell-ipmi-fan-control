
import os

IMPITOOL =  'ipmitool'

def _exec_raw_impi_cmd(payload: str) -> int:
    cmd = f'{IMPITOOL} raw {payload}'
    return os.system(cmd)

def _manual_fancontrol_toggle_command(enabled: bool) -> str:
    toggle = '0x00' if enabled else '0x01'
    return f'0x30 0x30 0x01 {toggle}' 

def _fan_speed_command(speedHex: str) -> str:
    return f'0x30 0x30 0x02 0xff {speedHex}'

def enable_fancontrol() -> int:
    return _exec_raw_impi_cmd(_manual_fancontrol_toggle_command(enabled=True))

def disable_fancontrol() -> int:
    return _exec_raw_impi_cmd(_manual_fancontrol_toggle_command(enabled=False))

def set_manual_fanspeed(speed: int) -> int:
    if 100 > speed > 0:
        return _exec_raw_impi_cmd(_fan_speed_command(hex(speed)))
    else:
        raise Exception(f'Invalid speed {speed}. Fan speed must be between 0 and 100')