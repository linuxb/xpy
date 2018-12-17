def process(pid):
    x = 6
    y = 10
    return pid + x + y


def main():
    res = process(8)
    print('res: {}'.format(res))

main()