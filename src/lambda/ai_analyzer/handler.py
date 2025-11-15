"""AWS Lambda handler for AI analysis."""
import json
import logging
from ai_analyzer import AIAnalyzer

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Handle AI analysis Lambda invocation.
    
    Args:
        event: Lambda event containing document data
        context: Lambda context object
        
    Returns:
        dict: Analysis result with insights and findings
    """
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
