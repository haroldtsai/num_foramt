import re

data_in = '12\'h1bc'
pattern = re.compile('(?P<num_bits>[0-9]+)\'(?P<format_type>[b|h|d])(?P<num>[0-9a-f]+)')
r_pat = pattern.match(data_in)
if r_pat:
    num_bits = int(r_pat.group('num_bits'))
    print(num_bits)
    format_type = r_pat.group('format_type')
    print(format_type)
    num = r_pat.group('num')
    print(num)

    def to_z_padding_bin(bin_input):
        return '0'*(num_bits - len(bin_input)) + bin_input

    if format_type == 'b':
        out = to_z_padding_bin(num)
        print(out)

    elif format_type == 'd':
        bin_input = bin(int(num))[2:]
        out = to_z_padding_bin(bin_input)
        print(out)

    elif format_type == 'h':
        bin_input = bin(int(num, 16))[2:]
        out = to_z_padding_bin(bin_input)
        print(out)
