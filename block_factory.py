import random
from abc import ABC, abstractmethod
from block_builder import BlockBuilder
from block_director import BlockDirector


class BlockFactory(ABC):
    @abstractmethod
    def create_random_block(self):
        pass
    
    @abstractmethod
    def reset_bag(self):
        pass


class RandomBagBlockFactory(BlockFactory):
    def __init__(self):
        self.director = BlockDirector(BlockBuilder())
        self._block_constructors = self._get_block_constructors()
        self._current_bag = []
        self.reset_bag()
    
    def _get_block_constructors(self):
        return [
            self.director.create_i_block,
            self.director.create_j_block,
            self.director.create_l_block,
            self.director.create_o_block,
            self.director.create_s_block,
            self.director.create_t_block,
            self.director.create_z_block
        ]
    
    def create_random_block(self):
        if not self._current_bag:
            self.reset_bag()
        
        constructor = random.choice(self._current_bag)
        self._current_bag.remove(constructor)
        
        return constructor()
    
    def reset_bag(self):
        self._current_bag = self._block_constructors.copy()


class TrueRandomBlockFactory(BlockFactory):
    def __init__(self):
        self.director = BlockDirector(BlockBuilder())
        self._block_constructors = self._get_block_constructors()
    
    def _get_block_constructors(self):
        return [
            self.director.create_i_block,
            self.director.create_j_block,
            self.director.create_l_block,
            self.director.create_o_block,
            self.director.create_s_block,
            self.director.create_t_block,
            self.director.create_z_block
        ]
    
    def create_random_block(self):
        constructor = random.choice(self._block_constructors)
        return constructor()
    
    def reset_bag(self):
        # Since is truly random, no state to reset
        pass

