"""Example usage of Smart Document Analyzer."""

import json
from pathlib import Path

# Mock Lambda handlers for demonstration
def demo_document_processor():
    """Demonstrate document processor."""
    print("\n" + "="*70)
    print("DOCUMENT PROCESSOR DEMO")
    print("="*70)
    
    # Simulate Lambda event
    event = {
        "document_path": "tests/sample_documents/sample.txt"
    }
    
    print(f"\nLambda Event:")
    print(json.dumps(event, indent=2))
    
    print(f"\nProcessing document: {event['document_path']}")
    
    # Simulated response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "success": True,
            "metadata": {
                "path": "tests/sample_documents/sample.txt",
                "size": 1024,
                "encoding": "utf-8"
            },
            "parsed_content": {
                "type": "TEXT",
                "content": "Sample document content...",
                "word_count": 150,
                "line_count": 15
            }
        })
    }
    
    print(f"\nLambda Response:")
    print(json.dumps(response, indent=2))


def demo_ai_analyzer():
    """Demonstrate AI analyzer."""
    print("\n" + "="*70)
    print("AI ANALYZER DEMO")
    print("="*70)
    
    # Simulate Lambda event
    event = {
        "document_data": {
            "content": """
            This is an excellent document with great insights.
            The analysis provides wonderful and positive feedback.
            Machine learning is amazing for text processing.
            """
        }
    }
    
    print(f"\nLambda Event:")
    print(json.dumps(event, indent=2))
    
    print(f"\nAnalyzing document content...")
    
    # Simulated response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "success": True,
            "timestamp": "2024-01-15T10:30:00",
            "analysis_count": 3,
            "analyses": [
                {
                    "analysis_type": "sentiment",
                    "sentiment": "positive",
                    "positive_indicators": 5,
                    "negative_indicators": 0
                },
                {
                    "analysis_type": "entity_extraction",
                    "unique_words": 32,
                    "total_words": 45,
                    "entities": {
                        "numbers": [],
                        "proper_nouns": []
                    }
                },
                {
                    "analysis_type": "keyword_extraction",
                    "top_keywords": [
                        {"keyword": "analysis", "frequency": 2},
                        {"keyword": "machine", "frequency": 1},
                        {"keyword": "learning", "frequency": 1}
                    ],
                    "unique_keywords": 28
                }
            ]
        })
    }
    
    print(f"\nLambda Response:")
    print(json.dumps(response, indent=2))


def demo_workflow():
    """Demonstrate end-to-end workflow."""
    print("\n" + "="*70)
    print("END-TO-END WORKFLOW DEMO")
    print("="*70)
    
    print("""
    1. Document Upload
       └─> S3 Bucket receives document
    
    2. S3 Trigger
       └─> Invokes Document Processor Lambda
    
    3. Document Processing
       └─> DocumentProcessor parses and validates
       └─> Extracts metadata
       └─> Sends to SQS Queue
    
    4. Message Queue
       └─> SQS receives processed document
    
    5. AI Analysis
       └─> Invokes AI Analyzer Lambda
       └─> Runs sentiment analysis
       └─> Extracts entities
       └─> Identifies keywords
    
    6. Results Storage
       └─> Stores analysis results in DynamoDB
    
    7. Response
       └─> Returns insights and analysis to client
    """)


def main():
    """Run demo."""
    print("\n" + "="*70)
    print("SMART DOCUMENT ANALYZER - DEMO")
    print("="*70)
    
    demo_document_processor()
    demo_ai_analyzer()
    demo_workflow()
    
    print("\n" + "="*70)
    print("Demo completed!")
    print("="*70 + "\n")


if __name__ == '__main__':
    main()
