import unittest
import sys

sys.path.append(sys.path[0] + "/..")
from app.model import Users, LobbyTimes, Lobby, LobbyPlayers

normal_user = Users(
    UID=500000001,
    Username="normal",
    Email="normal@email.com",
    IsAdmin=0
)
normal_user.set_password("normal password")

admin_user = Users(
    UID=500000002,
    Username="admin",
    Email="admin@email.com",
    IsAdmin=1
)
admin_user.set_password("normal password")

time_mon = LobbyTimes (
    RowID=0,
    LobbyID=222222,
    TimeBlockStart="00:00",
    DayOfWeek="0",
    TimeBlockEnd="00:50"
)
time_wed = LobbyTimes (
    RowID=2,
    LobbyID=222222,
    TimeBlockStart="00:00",
    DayOfWeek="2",
    TimeBlockEnd="00:50"
)
time_fri = LobbyTimes (
    RowID=4,
    LobbyID=222222,
    TimeBlockStart="00:00",
    DayOfWeek="4",
    TimeBlockEnd="00:50"
)
time_sun = LobbyTimes (
    RowID=6,
    LobbyID=222222,
    TimeBlockStart="00:00",
    DayOfWeek="6",
    TimeBlockEnd="00:50"
)

class UserIsAdminTestCase(unittest.TestCase):
    def test_not_admin(self):
        self.assertFalse(normal_user.is_admin())

    def test_is_admin(self):
        self.assertTrue(admin_user.is_admin())


class LobbyTimesDayStringTestCase(unittest.TestCase):
    def test_is_mon(self):
        self.assertEqual(time_mon.get_day_string(), "MON")

    def test_is_wed(self):
        self.assertEqual(time_wed.get_day_string(), "WED")

    def test_is_fri(self):
        self.assertEqual(time_fri.get_day_string(), "FRI")

    def test_is_sun(self):
        self.assertEqual(time_sun.get_day_string(), "SUN")

if __name__ == "__main__":
    unittest.main(verbosity=2)

