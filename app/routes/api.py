# app/routes/api.py
from flask import Blueprint, request, jsonify
from app.models.birth_chart import BirthChart
from app.core.fortune_analyzer import FortuneAnalyzer
import asyncio

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/analyze', methods=['POST'])
def analyze_birth_chart():
    try:
        # 获取请求数据
        data = request.get_json()

        # 创建生辰八字对象
        birth_chart = BirthChart(
            year=data.get('year'),
            month=data.get('month'),
            day=data.get('day'),
            hour=data.get('hour'),
            minute=data.get('minute', 0),
            is_leap=data.get('is_leap', False),
            calendar_type=data.get('calendar_type', 'gregorian')
        )

        # 创建分析器并执行分析
        analyzer = FortuneAnalyzer()
        # 使用asyncio.run来运行异步函数
        result = asyncio.run(analyzer.analyze(birth_chart))

        return jsonify({
            "status": "success",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "人生K线图API服务正常运行"
    })
