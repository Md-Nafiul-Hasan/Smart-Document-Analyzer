"""AWS Lambda handler for AI analysis (adjusted package path)."""
import json
import logging
from src.lambdas.ai_analyzer.ai_analyzer import AIAnalyzer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {json.dumps(event)}")

        analyzer = AIAnalyzer()
        document_data = event.get('document_data')

        if not document_data:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'document_data is required'})
            }

        result = analyzer.analyze(document_data)

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except Exception as e:
        logger.error(f"Error analyzing document: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
