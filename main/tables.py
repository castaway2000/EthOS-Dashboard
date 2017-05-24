from models import Miner_Info
import django_tables2 as tables

class MinerTable(tables.Table):
    class Meta:
        model = Miner_Info
