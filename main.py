# -*- coding:utf-8 -*-
# @Auther: XiongGuoqing
# @Datetime: 2019/12/21 4:27 下午
# @Contact: xiong3219@icloud.com

import math, random
import numpy as np


class RSA():
    def __init__(self, p, q):
        self.p = p
        self.q = q
        if self.primality(self.p) is False:
            print('p不是素数')
        elif self.primality(self.q) is False:
            print('q不是素数')
        else:
            self.RSA_generate()

    # 素性检验
    def primality(self, n):
        m = n
        p = 2
        while (p <= math.sqrt(m)):
            if (m % p == 0):
                m //= p
            else:
                p += 1
        if m == n:
            return True
        else:
            return False

    # 生成公钥e
    def e_generate(self, phi):
        e = random.randint(2, phi - 1)
        if math.gcd(e, phi) != 1:
            return self.e_generate(phi)
        else:
            return e

    # 扩展欧几里得方法求逆元
    def Eulid_Extended(self, a, b):
        x1, x2, x3, y1, y2, y3 = 1, 0, a, 0, 1, b
        while (y3 > 1):
            q = x3 // y3
            t1 = x1 - q * y1
            t2 = x2 - q * y2
            t3 = x3 - q * y3
            x1 = y1
            x2 = y2
            x3 = y3
            y1 = t1
            y2 = t2
            y3 = t3
        if y3 == 0:
            return -1
        elif y2 > 0:
            return y2
        else:
            return y2 + a

    # 公钥e和n和密钥d的生成
    def RSA_generate(self):
        self.n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        self.e = self.e_generate(phi)
        self.d = self.Eulid_Extended(phi, self.e)
        return [(self.n, self.e), self.d]

    # 加密 √
    def encrypt(self, inp):
        return inp ** self.e % self.n

    # 解密 √
    def decrypy(self, inp):
        return inp ** self.d % self.n


if __name__ == '__main__':
    R = RSA(557, 601)
    print(R.RSA_generate())
    code = R.encrypt(30091)
    print(code)
    print(R.decrypy(code))
