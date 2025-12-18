# app/core/mock_model_provider.py
from app.core.interfaces import ModelProviderInterface
import asyncio

class MockModelProvider(ModelProviderInterface):
    """模拟大模型提供者，用于测试和演示"""

    async def generate_analysis(self, prompt: str) -> str:
        """
        模拟生成分析结果
        """
        # 模拟网络延迟
        await asyncio.sleep(0.1)

        # 返回预设的分析结果
        return """
        根据您的生辰八字分析：

        【基本信息】
        八字：甲子 乙丑 丙寅 丁卯
        五行：木水 木土 火木 火木
        日主：丙火
        身强：较强

        【性格分析】
        您为人聪明机智，思维活跃，富有创造力。为人正直，做事有原则，但有时过于坚持己见。
        感情丰富，重视人际关系，容易得到他人信任和支持。

        【事业方向】
        适合从事与火、木相关的行业，如教育、文化、传媒、艺术设计等。
        具有领导才能，可在管理岗位上发挥优势。

        【财运分析】
        财运较为稳定，不宜投机。通过正当途径积累财富更为合适。
        注意理财规划，避免不必要的开支。

        【健康提醒】
        注意心脏、血液循环系统保养。
        避免过度劳累，保持心情舒畅。

        【流年运势】
        今年整体运势平稳，事业发展有机遇，注意把握。
        感情方面有喜事可能，单身者有望遇到良缘。
        """

    def _build_prompt(self, birth_chart_data: dict) -> str:
        """构建提示词"""
        prompt = f"""
        请根据以下生辰八字信息进行命理分析：
        公历年份：{birth_chart_data.get('year')}
        公历月份：{birth_chart_data.get('month')}
        公历日期：{birth_chart_data.get('day')}
        公历小时：{birth_chart_data.get('hour')}
        
        农历年份：{birth_chart_data.get('lunar_year', '待转换')}
        农历月份：{birth_chart_data.get('lunar_month', '待转换')}
        农历日期：{birth_chart_data.get('lunar_day', '待转换')}
        农历小时：{birth_chart_data.get('lunar_hour', '待转换')}
        
        八字：{birth_chart_data.get('eight_characters', '待计算')}
        
        请从以下方面进行详细分析：
        1. 日主强弱分析
        2. 五行平衡情况
        3. 十神配置特点
        4. 性格特征分析
        5. 事业发展方向
        6. 财运分析
        7. 婚姻感情状况
        8. 健康注意事项
        9. 流年运势概览
        """
        return prompt.strip()
