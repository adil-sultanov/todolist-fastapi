from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" RENAME COLUMN "password" TO "hashed_password";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" RENAME COLUMN "hashed_password" TO "password";"""


MODELS_STATE = (
    "eJztmVFv2jAQx78K4qmTtmllZUV7A9ZurBSklk6VpikyyRGsOnYam7Wo47vPNjEJTsJIBR"
    "qR6EvL+S7x/Xr2/2xe6gHzgPD3I+axnoCg/rn2UqcoAPlHZuxtrY7CMBlRBoHGRDsL6YWN"
    "15iLCLlC2ieIcJAmD7gb4VBgRqWVzghRRuZKR0z9xDSj+HEGjmA+iClEcuDnL2nG1INn4O"
    "Zj+OBMMBBvbbrYU+/WdkfMQ23rUXGpHdXbxo7LyCygiXM4F1NGV96YCmX1gUKEBKjHi2im"
    "pq9mF2dqMlrONHFZTjEV48EEzYhIpbslA5dRxU/OhusEffWWd43Ts/Oz1sdPZy3pomeysp"
    "wvlukluS8DNYHBqL7Q40igpYfGmHBLTysDsDtFUT5BK8xCKROwURpwm1gaQwIzKaAd0QzQ"
    "s0OA+mIqP55+kD8b6P1o33S/tW9OtN8blRGThb2s+EE82DCjCnOC1WVBSEClnoHaYYwAov"
    "lc1+IsqmMZuC+sZVeqxXUDxM5w2FezDjh/JNrQG1ko7647F5KyJiyd5EaSrt0EqtplCObC"
    "KbXYrah/r/oDKdUdLHy1W04ecte9oZIFeckiwD69grnm2ZOzQtSFHHYpiejHjzo8jgtTD8"
    "aa7NERelopiV0mMk2ZHCxLsdu+7ba/XNQ10DFyH55Q5DlrZNUIazDLsvLNDgWNwLYginzN"
    "QGWi5m0DLtBnA79Yn0es5rGaSo8fJbpqEi2wIJBFN4Lnoh3PBFRFljfgGV3cj9bkwwjvyX"
    "X7XitGMI9H+sPBV+OeUpduf9ixhGTGISonIqmIo4CsGO5APO7ixxwev22FI1UaZUUjtTfK"
    "wxPP6RXjsMurGyCooNvOOalVh+Zin8KpiytHNE3RFQum+qcepbJyUql/Z8gVH2ONf1WEcv"
    "382tzm8NosPrk2M8dWVfZlGaZjdsNx71W4Z4oQIEzKIFwFVJHf6bZ3KJtuUGyEcj8vsQPG"
    "3q/qzGI2FWvM0qymiE/Bc0LE+ROLcpSjuPByQl9Vgv8B4noNNlrb1GCjVVyDaiyn4d2meT"
    "NXBzto4Kp3j7LXBq4NEXaneS1cPLKxiUOJz7GLO7gNrLiL+y1775LfR6RCqtnLNZrNLXYw"
    "6VW4g+kxS0Xl0igBMXavJsC9tCHyjQJoziX599vhoOgbnFWIBdLDrqj9qZFD3+Lz+Kl8N1"
    "/D2TduKn/GhR/pp+gHdMoJ7O6FZfEXDM3srw=="
)
