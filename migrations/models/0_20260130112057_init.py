from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "age" INT
);
CREATE TABLE IF NOT EXISTS "To do lists" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" TEXT NOT NULL,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "todoitem" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "description" VARCHAR(10000) NOT NULL,
    "completed" BOOL NOT NULL DEFAULT False,
    "todolist_id" INT NOT NULL REFERENCES "To do lists" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmW1v2jAQx78K4lUnbdPKylrtHbB2Y6UgtelUaZqQSY5g1bHTxFmLOr77bCcmwXkYmU"
    "AiEn3Tcr5LfL+e/T+b17bHHCDhe4s5bMjBa39uvbYp8kD8kRt722oj309HpIGjGVHOXHhh"
    "7TULeYBsLuxzREIQJgdCO8A+x4wKK40IkUZmC0dM3dQUUfwUwZQzF/gCAjHw85cwY+rAC4"
    "T6o/84nWMgzsZ0sSPfrexTvvSVbUj5lXKUb5tNbUYij6bO/pIvGF17Y8ql1QUKAeIgH8+D"
    "SE5fzi7JVGcUzzR1iaeYiXFgjiLCM+luycBmVPITswlVgq58y7vO6dn52cXHT2cXwkXNZG"
    "05X8XppbnHgYrA2Gqv1DjiKPZQGFNu2WnlAA4WKCgmaIQZKEUCJkoNroqlNqQw0wLaEU0P"
    "vUwJUJcvxMfTD+Kngt6P3u3gW+/2RPm9kRkxUdhxxY+TwY4elZhTrDbzfAIy9RzUPmMEEC"
    "3muhFnUJ2JwH1hrbtSDa4VEPuTyUjO2gvDJ6IMQ8tAeX/TvxSUFWHhJDaSbO2mUOUuQ3DI"
    "p7UWuxH171V/IKW6g4Uvd8v5Y+G611TyIK9YANil17BUPIdiVojaUMAuIxGj5FGHx3Gl60"
    "Fb0z06QM9rJTHLRKQpkoO4FAe9u0Hvy2VbAZ0h+/EZBc50g6wcYR1mWNa++SGv45kWRJGr"
    "GMhM5LxNwCX6rOGX67PFWg5ryfTCo0Q3TaI55gTy6Cx4KdvxdEBTZLkCj3X5YG3Ihxbek5"
    "veg1IMb5mMjCbjr9o9oy6D0aRvCEkUQlBPRDIRRwFZM9yBeNwnjzk8ftsKR6Y06opGZm8U"
    "h6ewoFdMwq6ub4Ggkm674KTWHJqrfQqnKq4C0dRFVy6Y8p96lMrGSaX6nSNXfozV/k0Rys"
    "3za3ebw2u3/OTazR1bZdnXZZiN2Q3HvVfhnimChzCpg3Ad0ER+p9veoVTdoJgIxX5eYwdM"
    "vP+rM0vYNL0x26bJ0EfcHTQazTvv77XR6EGA7UVRq5GMVDYbKPU5dhsHttCquo3fokeseW"
    "+eCWlmz9HpdrfY7YVX6W6vxozdXiyNGhAT92YC3ItcijdyoAWXud/vJuOybxrWIQZIB9u8"
    "9adFDn2LL+In862+LjJvhmT+LORuoJ6iHtCvJ7C7F5bVXz5+fcE="
)
