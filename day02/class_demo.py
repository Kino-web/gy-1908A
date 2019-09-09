class ClassDemo():
    def abc(self):
        print("蔡徐坤")
    def xyz(self):
        print("吴亦凡")
        self.abc()

if __name__ == "__main__":
    c = ClassDemo()
    c.abc()
    c.xyz()

