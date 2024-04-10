class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        count=0
        while n >0:
            k = n%10
            n = n//10
            if k >0:
                count+=k-1


            print(k,n)
# 1,3,5
# 11,22,33
# 111,122,133,
# 121,131,141,144
# 100,101

s =Solution()
print(s.countSpecialNumbers(135))

import base64

encoded_string = "EAAAAFqZoydG/WUR2aw7ox9bTEKh7dOTywBmD6C3OZbH7fqnhWzJpRddd7SGVCSq7O2XcFiu4jvOC55FeGz27hY2RSUpmkdllRFfe4qZQzkZ0M/FzcuvmdC1MzTWtDAfokHz+sjt6lH7ZSGxdvOL1vSCV68rZEqrwMSaEZEAg8+8hzjbpFePfvunkOI2hrTxueaQN9ffPRaxWHqMMYxY07BoHG3sxoWP0aJwWfqzJ09xzg3phj5zwvRaOXgd1a0adk6i6xGILfO3vzyY3TacbnUZz/Vwh39RbrWSf5Cvb5n6Ifqyf5iiG6h7t30th1MqtMImunJ0PIHom1QyUPsdjdf5joPgmW4musfK0K69EaTUBYaoYicosuUVQwn86B85ALEz2wd63Y+h55txmsrt9aAzdPkH+UhczZFSF9AuA6BAnSlN+rI5+a9+EpwfdNoge1jJ7jdKZmpVH90d9J2YeaSEAcySShxyxSPmELvG82r9hlK3VPmdpaNpqpClgz9e6J+bn2ujMb9HJe5J3ouxRR85HRA="

decoded_bytes = base64.b64decode(encoded_string)
print(decoded_bytes)
decoded_string = decoded_bytes.decode('utf-8')
print(decoded_string)
# print(s.countSpecialNumbers(20))
