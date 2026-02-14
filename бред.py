def add_loot_pool(self):
    if self.enemies in loot_tables:
        self.loot_pool[self.enemies] = loot_tables[self.enemies]
    else:
        print(f"лут таблица для врага {self.enemies} не найдена")