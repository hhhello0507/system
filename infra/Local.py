import pickle
import os
import time
from typing import List, Tuple

base_path = './save/'

if not os.path.exists(base_path):
    os.makedirs(base_path)


class Local:
    def __init__(self, save_path: str):
        self.save_path = save_path

    def __joined_save_path(self):
        return os.path.join(base_path, self.save_path)

    def push(self, value):
        joined_save_path = self.__joined_save_path()

        save_data = []

        # 기존 데이터가 존재하는 경우 로드
        if os.path.exists(joined_save_path):
            with open(joined_save_path, 'rb') as f:
                try:
                    save_data = pickle.load(f)
                except (EOFError, pickle.PickleError):
                    save_data = []

        save_data.append((time.time(), value))

        # 변경된 캐시 데이터 저장
        with open(joined_save_path, 'wb') as f:
            pickle.dump(save_data, f)

    def load(self) -> List[Tuple[int, any]]:
        joined_save_path = self.__joined_save_path()

        if not os.path.exists(joined_save_path):
            raise FileNotFoundError

        with open(joined_save_path, 'rb') as f:
            save_data = pickle.load(f)

        return save_data

    def load_recent(self):
        return self.load()[-1][1]

CategoryLocal = Local('categories.pkl')
ResultLocal = Local('results.pkl')
SkillLocal = Local('skills.pkl')
