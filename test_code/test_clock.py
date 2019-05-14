class Test_clock():

    def test_reset_time(self):
        self.pretime=time.time()
        self.remaining_time=60

    def show_time(self):
        newtime=time.time()
        if int(newtime-self.pretime)>=1:
            print(int(newtime-self.pretime),self.remaining_time)
            self.remaining_time-=1
            self.pretime=time.time()

    def test(self):
        test_clock=Test_clock()
        test_clock.test_reset_time()
        while 1:
            test_clock.show_time()