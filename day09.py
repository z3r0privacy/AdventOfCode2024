class Disk_P1:
    def __init__(self, input):
        self._sizes = [int(c) for c in input]
        self._posAL = 0
        self._isFileL = True
        self._posAR = len(self._sizes)-1
        #self._isFileR = True
        self._fileIdL = 0
        self._fileIdR = len(self._sizes) // 2

    def is_current_file(self):
        if self._posAR < self._posAL:
            raise ValueError("pos right smaller than pos left")
        return self._isFileL and self._sizes[self._posAL] > 0
    
    def pop_current_file(self):
        if self._sizes[self._posAL] <= 0:
            raise ValueError("0 or less of file left")
        if not self._isFileL:
            raise ValueError("Currently not a file")
        id = self._fileIdL
        self._sizes[self._posAL] -= 1
        while self._sizes[self._posAL] == 0:
            self._posAL += 1
            self._isFileL = not self._isFileL
            if self._isFileL:
                self._fileIdL += 1
        return id
    
    def push_file(self):
        if self._isFileL:
            raise ValueError("current is file and not empty")
        if self._sizes[self._posAL] <= 0:
            if self.is_defragmented():
                return
            raise ValueError("empty space is zero or less")
        self._sizes[self._posAL] -= 1
        if self._sizes[self._posAL] == 0:
            self._posAL += 1
            self._isFileL = True
            self._fileIdL += 1

    def pop_fragmented(self):
        if self._sizes[self._posAR] <= 0:
            raise ValueError("0 or less of fragmented file left")
        id = self._fileIdR
        self._sizes[self._posAR] -= 1
        if self._sizes[self._posAR] == 0:
            self._posAR -= 1
            self._fileIdR -= 1
            if self._posAR >= self._posAL:
                self._sizes[self._posAR] = 0
                self._posAR -= 1
            else:
                raise ValueError("Should not happen... i think?")
        return id

    def is_defragmented(self):
        return sum(self._sizes[self._posAL:]) == 0

class DiskNode_P2:
    def __init__(self, isFile:bool, size:int, id:int=0):
        self.isFile = isFile
        self.size = size
        self.id = id
        self.tried_to_move = False
        self.prev = None
        self.next = None

    def append(self, node:"DiskNode_P2"):
        self.next = node
        node.prev = self

    def insert_after(self, node:"DiskNode_P2"):
        r = self.next
        self.next = node
        r.prev = node
        node.prev = self
        node.next = r

    def take_out(self):
        l = self.prev
        r = self.next
        e = DiskNode_P2(False, self.size)
        e.prev = l
        e.next = r
        if l: l.next = e
        if r: r.prev = e
        self.prev = None
        self.next = None

    def get_next_move_candidate(self):
        c = self.prev
        while c:
            if c.isFile and not c.tried_to_move:
                return c
            c = c.prev
        return None

def part1(line):
    checksum = 0
    d = Disk_P1(line)
    curr_pos = 0
    while not d.is_defragmented():
        val = 0
        if d.is_current_file():
            val = d.pop_current_file()
        else:
            val = d.pop_fragmented()
            d.push_file()
        checksum += curr_pos * val
        # print(f"{curr_pos} * {val}")
        curr_pos += 1
    print(f"Checksum 1: {checksum}")

def printnodes(start:DiskNode_P2):
    n = start
    while n:
        c = n.id if n.isFile else "."
        for i in range(n.size):
            print(c, end="")
        n = n.next
    print()

def part2(line):
    startNode = DiskNode_P2(True, int(line[0]), 0)
    isFile = False
    prev = startNode
    id = 1
    for s in line[1:]:
        n = DiskNode_P2(isFile, int(s), id if isFile else 0)
        if isFile: id += 1

        prev.append(n)
        prev = n
        isFile = not isFile
    
    #printnodes(startNode)
    next_candidate = prev
    while next_candidate:
        cand = next_candidate
        next_candidate = cand.get_next_move_candidate()
        curr_empty = startNode
        while curr_empty != cand:
            if curr_empty.isFile or curr_empty.size < cand.size:
                curr_empty = curr_empty.next
                continue
            curr_empty.size -= cand.size
            cand.take_out()
            curr_empty.prev.insert_after(cand)
            break
        cand.tried_to_move = True
        #printnodes(startNode)
    
    checksum = 0
    idx = 0
    curr_chks = startNode
    while curr_chks:
        if curr_chks.isFile:
            idx_sum = sum(idx+i for i in range(curr_chks.size))
            checksum += idx_sum*curr_chks.id
        idx += curr_chks.size
        curr_chks = curr_chks.next
    print(f"Checksum 2: {checksum}")
                

from datetime import datetime

if __name__ == "__main__":
    line = open("inputs\\day09.txt").read()
    start = datetime.now()
    part1(line)
    part2(line)
    dur = datetime.now() - start
    print(dur)