import threading
import SafeQueue

class ThreadPool():

    def __init__(self,num_threads):
        self.tasks = SafeQueue()
        self.threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=self._worker)
            t.daemon = True  # 设为守护线程，主线程退出时自动结束
            t.start()
            self.threads.append(t)

    def _worker(self):
        while True:
            func, args, kwargs = self.tasks.get()
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(f"任务出错: {e}")
            finally:
                self.tasks.task_done()

    def submit(self, func, *args, **kwargs):
        self.tasks.put((func, args, kwargs))

    def wait_completion(self):
        self.tasks.join()