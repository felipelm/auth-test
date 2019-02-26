import jwt
from datetime import datetime
import time
# encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
encoded=jwt.encode({'exp': datetime.utcnow()+datetime.timedelta(seconds=30)}, 'secret')
print(encoded)
time.sleep(60)
decoded = jwt.decode(encoded, 'secret', algorithms=['HS256'])
print(decoded)