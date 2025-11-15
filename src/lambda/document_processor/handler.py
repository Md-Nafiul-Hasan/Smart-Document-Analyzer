"""AWS Lambda handler for document processing."""
import json
import logging
from document_processor import DocumentProcessor

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Handle document processing Lambda invocation.
    
    Args:
        event: Lambda event containing document information
        context: Lambda context object
        
    Returns:
        dict: Processing result with status and processed document data
    """
    try:
        logger.info(f"Received event: {json.dumps(event)}")
        
        processor = DocumentProcessor()
        document_path = event.get('document_path')
        
        if not document_path:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'document_path is required'})
            }
        
        result = processor.process(document_path)
        
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    except Exception as e:
        logger.error(f"Error processing document: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
