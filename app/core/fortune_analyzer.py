# app/core/fortune_analyzer.py
from app.core.interfaces import FortuneAnalysisInterface, BirthChartInterface
from app.core.mock_model_provider import MockModelProvider
from typing import Dict, Any
import asyncio

class FortuneAnalyzer(FortuneAnalysisInterface):
    """命运分析器实现"""

    def __init__(self, model_provider=None):
        # 默认使用模拟提供者
        self.model_provider = model_provider or MockModelProvider()

    async def analyze(self, birth_chart: BirthChartInterface) -> Dict[str, Any]:
        """
        对生辰八字进行命运分析

        Args:
            birth_chart: 生辰八字数据

        Returns:
            分析结果字典
        """
        # 1. 转换日历
        birth_chart.convert_calendar()

        # 2. 计算八字
        eight_characters = birth_chart.get_eight_characters()

        # 3. 构造分析所需数据
        analysis_data = {
            "year": birth_chart.year,
            "month": birth_chart.month,
            "day": birth_chart.day,
            "hour": birth_chart.hour,
            "minute": birth_chart.minute,
            "is_leap": birth_chart.is_leap,
            "calendar_type": birth_chart.calendar_type,
            "lunar_year": birth_chart.lunar_year,
            "lunar_month": birth_chart.lunar_month,
            "lunar_day": birth_chart.lunar_day,
            "lunar_hour": birth_chart.lunar_hour,
            "gregorian_year": birth_chart.gregorian_year,
            "gregorian_month": birth_chart.gregorian_month,
            "gregorian_day": birth_chart.gregorian_day,
            "gregorian_hour": birth_chart.gregorian_hour,
            "eight_characters": eight_characters
        }

        # 4. 构建提示词
        prompt = self.model_provider._build_prompt(analysis_data)

        # 5. 调用大模型生成分析
        analysis_result = await self.model_provider.generate_analysis(prompt)

        # 6. 返回完整分析结果
        return {
            "birth_info": {
                "gregorian": f"{birth_chart.gregorian_year}-{birth_chart.gregorian_month:02d}-{birth_chart.gregorian_day:02d} {birth_chart.gregorian_hour:02d}:{birth_chart.minute:02d}",
                "lunar": f"{birth_chart.lunar_year}-{birth_chart.lunar_month}-{birth_chart.lunar_day} {birth_chart.lunar_hour}",
                "calendar_type": birth_chart.calendar_type
            },
            "eight_characters": eight_characters,
            "analysis": analysis_result,
            "generated_at": "2023-01-01 00:00:00"  # 实际使用时应为当前时间
        }
