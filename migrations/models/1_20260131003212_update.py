from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ADD "password" VARCHAR(128);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" DROP COLUMN "password";"""


MODELS_STATE = (
    "eJztmVFv2jAQx78K4qmTtmllZUV7A9ZurBSklk6VpgmZ5AhWHTuNzVrU8d1nm5gEJ2FJBR"
    "qR6EvL+S7x/Xr2/2xe6j5zgfD3I+ayngC//rn2UqfIB/lHauxtrY6CIB5RBoEmRDsL6YWN"
    "14SLEDlC2qeIcJAmF7gT4kBgRqWVzglRRuZIR0y92DSn+HEOY8E8EDMI5cDPX9KMqQvPwM"
    "3H4GE8xUDcjeliV71b28diEWhbj4pL7ajeNhk7jMx9GjsHCzFjdO2NqVBWDyiESIB6vAjn"
    "avpqdlGmJqPVTGOX1RQTMS5M0ZyIRLoFGTiMKn5yNlwn6Km3vGucnp2ftT5+OmtJFz2Tte"
    "V8uUovzn0VqAkMRvWlHkcCrTw0xphbclopgN0ZCrMJWmEWSpmAjdKA28bSGGKYcQHtiKaP"
    "nscEqCdm8uPpB/mzhd6P9k33W/vmRPu9URkxWdirih9Egw0zqjDHWB3mBwRU6imoHcYIIJ"
    "rNdSPOojqRgfvCWnalWly3QOwMh301a5/zR6INvZGF8u66cyEpa8LSSW4kydqNoapdhmAu"
    "xqUWuxX171V/IKW6g4WvdsvpQ+a6N1TSIC9ZCNijV7DQPHtyVog6kMEuIRH96FGHx3Fp6s"
    "FY4z06RE9rJbHLRKYpk4NVKXbbt932l4u6BjpBzsMTCt3xBlk1whrMsqx900N+w7ctiCJP"
    "M1CZqHnbgHP02cDP1+cRq7msptLjR4mumkQLLAik0Y3gOW/HMwFVkeUteEYX96MN+TDCe3"
    "LdvteK4S+ikf5w8NW4J9Sl2x92LCGZcwjLiUgi4igga4Y7EI+76DGHx6+ocCRKo6xoJPZG"
    "eXjiGb1iFHZ5dQME5XTbGSe16tBc7lM4dXFliKYpunzBVP/Uo1RWTir17xS5/GOs8a+KUG"
    "6eX5tFDq/N/JNrM3VsVWVflmEyZjcc916Fe6YIPsKkDMJ1QBX5nRa9Q9l2g2IjlPt5iR0w"
    "8n5VZxaxqVhjlmQVIM6fWJghGfkVl4x5VdH9B2ybVddoFam6Riu/6tRYRotbpF0zlwU7aN"
    "mqd3Oy15atDSF2ZllNWzSytW1Dsc+xbzu4LSu/b/stu+2S30AkQqrZvTWazQI7mPTK3cH0"
    "mKWbcmmUgBi5VxPgXhoP+UYBNONa/PvtcJD3nc06xALpYkfU/tTIoW/xWfxUvtsv3uw7Np"
    "U/48IL9VP0AzrlBHb3wrL8C1Tf5xc="
)
