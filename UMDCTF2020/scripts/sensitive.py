def main():
    g = open("actual.pdf", "a+")
    with open("sensitive") as f:
        count = 0
        while True:
            c = f.read(1)
            if not c:
                break
            if count % 2 == 0:
                g.write(c)
            count += 1
        f.close()
        g.close()


if __name__ == "__main__":
    main()
