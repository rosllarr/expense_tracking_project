from datetime import date
from django.core.management.base import BaseCommand

from months.models import Month


class Command(BaseCommand):
    help = 'Generate simple data to Month table'

    june_trans = [
        Month(name='เงินเดือนเข้า',           fixed=True, income=True,   due_date=date.fromisoformat('2023-05-25'), date=date.fromisoformat('2023-05-25'), amount=38353),
        Month(name='ให้แม่',                 fixed=True, expenses=True, due_date=date.fromisoformat('2023-05-25'), date=date.fromisoformat('2023-05-25'), amount=13000),
        Month(name='ประกันรถ',              fixed=True, expenses=True, due_date=date.fromisoformat('2023-05-25'), date=date.fromisoformat('2023-05-25'), amount=1100),
        Month(name='ให้จอย',                fixed=True, expenses=True, due_date=date.fromisoformat('2023-05-26'), date=date.fromisoformat('2023-05-26'), amount=1000),
        Month(name='ให้เนย',                fixed=True, expenses=True, due_date=date.fromisoformat('2023-05-26'), date=date.fromisoformat('2023-05-26'), amount=3000),
        Month(name='เงินลูกเข้า',             fixed=True, income=True  , due_date=date.fromisoformat('2023-05-30'), date=date.fromisoformat('2023-05-30'), amount=800),
        Month(name='netflix',              fixed=True, expenses=True, due_date=date.fromisoformat('2023-06-05'), date=date.fromisoformat('2023-06-05'), amount=210),
        Month(name='ผ่อนรถ',                fixed=True, expenses=True, due_date=date.fromisoformat('2023-06-14'), amount=9000),
        Month(name='บ้าน42',                fixed=True, expenses=True, due_date=date.fromisoformat('2023-06-17'), amount=2001),
        Month(name='กินใช้',                 fixed=True, expenses=True, due_date=date.fromisoformat('2023-05-25'), date=date.fromisoformat('2023-05-25'), amount=2000),
        Month(name='กินใช้',                 fixed=True, expenses=True, due_date=date.fromisoformat('2023-06-05'), date=date.fromisoformat('2023-06-05'), amount=2000),
        Month(name='กินใช้',                 fixed=True, expenses=True, due_date=date.fromisoformat('2023-06-15'), amount=2000),
        Month(name='ค่าโทร',                fixed=True, expenses=True, due_date=date.fromisoformat('2023-06-15'), amount=1285),
        Month(name='ค่าน้ำมันรถใหญ่',          fixed=True, expenses=True, amount=200),
        Month(name='ค่าน้ำมันมอไซค์',          fixed=True, expenses=True, date=date.fromisoformat('2023-05-26'), amount=1000),
        Month(name='ค่าไฟ42',               fixed=True, expenses=True, due_date=date.fromisoformat('2023-06-03'), date=date.fromisoformat('2023-06-05'), amount=500),
        Month(name='olay cream',           extra=True, expenses=True, date=date.fromisoformat('2023-05-25'), amount=600),
        Month(name='ให้เนยเพิ่ม',             extra=True, expenses=True, date=date.fromisoformat('2023-05-26'), amount=1000),
        Month(name='mouse and flashdrive', extra=True, expenses=True, date=date.fromisoformat('2023-05-31'), amount=270),
    ]

    def handle(self, *args, **options):
        trans = self.june_trans
        for t in trans:
            t.save()
        