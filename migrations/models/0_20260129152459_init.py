from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "age" INT
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
    "eJztlW9r2zAQxr9K8KsOtpF6yVr2Lg2UdmwpdH8YjGEU62KLyJIryVtLl+9enexEtuNkCW"
    "xLC31nP/fIuvtZursPMkmB69dfNKjgXe8+ECQD+9DQX/YCkudeRcGQKXfGwjqcQqbaKBIb"
    "K84I12AlCjpWLDdMCquKgnMUZWyNTCReKgS7KSAyMgGTukS+/7AyExRuQS9f83k0Y8BpI0"
    "9GcW+nR+Yud9qlMOfOiLtNo1jyIhPenN+ZVIqVmwmDagICFDGAnzeqwPQxu6rMZUVlpt5S"
    "plhbQ2FGCm5q5e7IIJYC+dlstCswwV1ehceDk8Hpm7eDU2txmayUk0VZnq+9XOgITD4HCx"
    "cnhpQOh9Fzw9/mntfojVOiuvHV17Qg2tTbEJfIDkoxI7cRB5GY1L4O+1uQfR1djy9G10fD"
    "/gusRNqjXB7wSRUJXQipeoqQEcb3Qbha8BT5Hfd3AWhdGwm6WBMhSTrO4MYbXLn/fIU76F"
    "VsVvCWFk/P963Hc4mx883mtTuMwpTE819E0WgtIkO5ybseysKsrRBhEdOqIkyuGgQjUCxO"
    "u0ZEFdk6JIj3PE+JR3bAtk2Jn3a2Y0p7dLjakr/T4/7DNW10uXA43KHLWdfGLudirS5nr8"
    "YeECv70wT4T8aE3dFAeQebEN9/upp0Q6wtaYGkLDa93z3O9C5z4wBAt/DDejHpTOsbXsd2"
    "9HH0rU10/OHqzNUvtUmU+4r7wNmhB8viAYwx9f0="
)
