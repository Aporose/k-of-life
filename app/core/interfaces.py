# app/core/interfaces.py
from abc import ABC, abstractmethod
from typing import Dict, Any
from datetime import datetime

class BirthChartInterface(ABC):
    """生辰八字数据接口"""
    
    def __init__(self, year: int, month: int, day: int, hour: int, 
                 minute: int = 0, is_leap: bool = False, calendar_type: str = "gregorian"):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.is_leap = is_leap  # 是否闰月
        self.calendar_type = calendar_type  # gregorian 或 lunar

class FortuneAnalysisInterface(ABC):
    """命运分析接口"""
    
    @abstractmethod
    async def analyze(self, birth_chart: BirthChartInterface) -> Dict[str, Any]:
        """
        对生辰八字进行命运分析
        
        Args:
            birth_chart: 生辰八字数据
            
        Returns:
            分析结果字典，包含各项分析内容
        """
        pass

class ModelProviderInterface(ABC):
    """大模型提供者接口"""
    
    @abstractmethod
    async def generate_analysis(self, prompt: str) -> str:
        """
        调用大模型生成分析结果
        
        Args:
            prompt: 输入提示词
            
        Returns:
            模型生成的分析文本
        """
        pass
