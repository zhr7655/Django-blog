import threading
import collections
import time

"""
一个安全的任务队列需要哪些：
1.容器：队列
2.添加任务的功能，提供任务的功能，
3.需要检测队列是否已满，是否是空的
4.需要互斥锁，防止数据冲突

"""

class QueueClosedError(Exception):
    """队列已关闭时抛出的异常"""
    pass


class QueueEmpty(Exception):
    """队列为空时无法取出元素"""
    pass


class QueueFull(Exception):
    """队列已满时无法放入元素"""
    pass

class SafeQueue():
    def __init__(self,maxsize = 0):
        self.queue = collections.deque()
        self._maxsize = maxsize
        self._closed = False
        self.unfinished_tasks = 0

        self._mutex = threading.Lock()
        self._not_empty = threading.Condition(self._mutex)
        self._not_full = threading.Condition(self._mutex)
        self._all_tasks_done = threading.Condition(self._mutex)

    def _qsize(self):
        return len(self.queue)

    def _is_empty(self):
        return len(self.queue) == 0

    def _is_full(self):
        return self._maxsize > 0 and len(self.queue) >= self._maxsize

    def _check_closed(self):
        if self._closed:
            raise QueueClosedError("队列已经被关闭了")

    #添加任务
    #条件判断，1.是否关闭 2.是否已满 3.判断是不是无限期等待  
    def put(self,task,block=True,timeout=None):
        with self._not_full:
            self._check_closed()

            #判断队列是否已满
            if self._is_full():
                #是否阻塞等待
                if not block:
                    raise QueueFull("队列已满")
                #阻塞等待，timeout is None时，代表无限期等待
                deadline = None if timeout is None else time.monotonic() + timeout
                while self._is_full():
                    #检查队列是否被关闭
                    self._check_closed()
                    #检查超时
                    if deadline is not None:
                        remaining = deadline - time.monotonic()
                        if remaining <= 0:
                            raise QueueFull("队列已满（超时）")
                        #让该线程等待，wait()会释放锁，让其他线程可以获取，防止死锁
                        self._not_full.wait(remaining)
                    else:
                        #无限期等待，知道其他程序调用notify()唤起
                        self._not_full.wait()
            #队列出现空位
            #先检查是否被关闭了
            self._check_closed()

            self.queue.append(task)
            self.unfinished_tasks += 1
            #唤起其他线程，加入任务后，唤起非空线程来取任务
            self._not_empty.notify()

    def get(self,block=True,timeout=None):
        with self._not_empty:
            self._check_closed()

            if self._is_empty():
                if not block:
                    raise QueueEmpty("队列是空的")

            deadline = None if timeout is None else time.monotonic() + timeout

            while self._is_empty():
                self._check_closed()

                if deadline is not None:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        raise QueueEmpty("队列是空的（超时）")
                    self._not_empty.wait(remaining)
                else:
                    self._not_empty.wait()
            self._check_closed()

            task = self.queue.popleft()
            #取出任务后，唤起非满线程加入任务
            self._not_full.notify()

            return task

    def task_done(self):
        """
            标记一个任务已完成
        """
        with self._all_tasks_done:
            if self.unfinished_tasks <= 0:
                raise ValueError("task_done() 被调用次数太多")
            self.unfinished_tasks -= 1
            if self.unfinished_tasks == 0:
                self._all_tasks_done.notify_all()

    def join(self):
        with self._all_tasks_done:
            while self.unfinished_tasks > 0:
                self._all_tasks_done.wait()

    #关闭任务队列，不再添加和取出
    def close(self):
        with self._mutex:
            if not self._closed:
                self._closed = True
                self.unfinished_tasks = 0 
                self._not_empty.notify_all()
                self._not_full.notify_all()
                self._all_tasks_done.notify_all()

    def qsize(self):
        """返回当前队列中的元素数量（近似值）。"""
        with self._mutex:
            return self._qsize()

    def empty(self):
        """队列是否为空。"""
        with self._mutex:
            return self._is_empty()

    def full(self):
        """队列是否已满（无界队列永远返回 False）。"""
        with self._mutex:
            return self._is_full()

    def closed(self):
        """队列是否已关闭。"""
        with self._mutex:
            return self._closed

    def __len__(self):
        return self.qsize()

    
            

