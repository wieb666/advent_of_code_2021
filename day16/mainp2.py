import sys
from typing import NamedTuple, Protocol, Tuple

class _Packet(Protocol):
    @property
    def version(self) -> int: ...
    @property
    def type_id(self) -> int: ...
    @property
    def n(self) -> int: ...
    @property
    def packets(self): ...

class Packet(NamedTuple):
    version: int
    type_id: int
    n: int = -1
    packets: Tuple[_Packet, ...] = ()


def read_file(fname: str) -> str:
    with open(fname) as f:
        lines = f.readlines()[0]
    return lines

def compute(s: str) -> int:
    bin_str = ''
    for c in s:
        bin_str += f'{int(c, 16):04b}'

    def parse_packet(i: int) -> Tuple[int, _Packet]:
        def _read(n: int) -> int:
            nonlocal i
            ret = int(bin_str[i:i + n], 2)
            i += n
            return ret

        version = _read(3)
        type_id = _read(3)

        if type_id == 4:
            chunk = _read(5)
            n = chunk & 0b1111
            while chunk & 0b10000:
                chunk = _read(5)
                n <<= 4
                n += chunk & 0b1111

            return i, Packet(version=version, type_id=type_id, n=n)
        else:
            mode = _read(1)

            if mode == 0:
                bits_length = _read(15)
                j = i
                i = i + bits_length
                packets = []
                while j < i:
                    j, packet = parse_packet(j)
                    packets.append(packet)

                ret = Packet(
                    version=version,
                    type_id=type_id,
                    packets=packets,
                )
                return i, ret
            else:
                sub_packets = _read(11)
                packets = []
                for _ in range(sub_packets):
                    i, packet = parse_packet(i)
                    packets.append(packet)
                ret = Packet(
                    version=version,
                    type_id=type_id,
                    packets=packets,
                )
                return i, ret

    def val(packet: _Packet) -> int:
        if packet.type_id == 0:
            return sum(val(sub_packet) for sub_packet in packet.packets)
        elif packet.type_id == 1:
            res = 1
            for sub_packet in packet.packets:
                res *= val(sub_packet)
            return res
        elif packet.type_id == 2:
            return min(val(sub_packet) for sub_packet in packet.packets)
        elif packet.type_id == 3:
            return max(val(sub_packet) for sub_packet in packet.packets)
        elif packet.type_id == 4:
            return packet.n
        elif packet.type_id == 5:
            return val(packet.packets[0]) > val(packet.packets[1])
        elif packet.type_id == 6:
            return val(packet.packets[0]) < val(packet.packets[1])
        elif packet.type_id == 7:
            return val(packet.packets[0]) == val(packet.packets[1])
        else:
            raise AssertionError(packet)
    
    _, packet = parse_packet(0)
    return val(packet)

if __name__ == "__main__":
    print(compute(read_file(sys.argv[1])))
