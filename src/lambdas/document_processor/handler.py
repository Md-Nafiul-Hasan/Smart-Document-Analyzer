"""AWS Lambda handler for document processing (adjusted package path)."""
import json
import logging
from src.lambdas.document_processor.document_processor import DocumentProcessor

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
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
