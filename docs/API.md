# Smart Document Analyzer - API Documentation

## Document Processor Lambda

### Function: `lambda_handler(event, context)`

#### Input Event
```json
{
  "document_path": "/path/to/document.txt"
}
```

#### Success Response
```json
{
  "statusCode": 200,
  "body": {
    "success": true,
    "metadata": {
      "path": "/path/to/document.txt",
      "size": 1024,
      "encoding": "utf-8"
    },
    "parsed_content": {
      "type": "TEXT",
      "content": "...",
      "word_count": 150,
      "line_count": 10
    }
  }
}
```

#### Error Response
```json
{
  "statusCode": 400,
  "body": {
    "error": "document_path is required"
  }
}
```

### Class: `DocumentProcessor`

#### Methods

##### `process(document_path: str) -> Dict[str, Any]`
Process a single document.

**Parameters**:
- `document_path` (str): Path to the document file

**Returns**: Dictionary with processing results

**Example**:
```python
processor = DocumentProcessor()
result = processor.process("/path/to/document.txt")
```

##### `get_processed_documents() -> List[Dict]`
Get all processed documents.

**Returns**: List of processed document results

---

## AI Analyzer Lambda

### Function: `lambda_handler(event, context)`

#### Input Event
```json
{
  "document_data": {
    "content": "Document text content..."
  }
}
```

#### Success Response
```json
{
  "statusCode": 200,
  "body": {
    "success": true,
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
        "unique_words": 45,
        "total_words": 150,
        "entities": {
          "numbers": ["42", "123"],
          "proper_nouns": ["John", "Smith", "AWS"]
        }
      },
      {
        "analysis_type": "keyword_extraction",
        "top_keywords": [
          {"keyword": "machine", "frequency": 3},
          {"keyword": "learning", "frequency": 2}
        ],
        "unique_keywords": 35
      }
    ]
  }
}
```

### Class: `AIAnalyzer`

#### Methods

##### `analyze(document_data: Dict[str, Any]) -> Dict[str, Any]`
Perform comprehensive AI analysis on document.

**Parameters**:
- `document_data` (dict): Dictionary containing 'content' key with text

**Returns**: Dictionary with analysis results

**Example**:
```python
analyzer = AIAnalyzer()
result = analyzer.analyze({
    'content': 'This is a great document!'
})
```

##### `get_analysis_history() -> List[Dict]`
Get history of all analyses performed.

**Returns**: List of analysis results

### Analysis Strategies

#### SentimentAnalyzer
Analyzes the sentiment of text.

**Result Structure**:
```python
{
    'analysis_type': 'sentiment',
    'sentiment': 'positive|negative|neutral',
    'positive_indicators': int,
    'negative_indicators': int
}
```

#### EntityExtractor
Extracts entities from text.

**Result Structure**:
```python
{
    'analysis_type': 'entity_extraction',
    'unique_words': int,
    'total_words': int,
    'entities': {
        'numbers': [list of numbers],
        'proper_nouns': [list of capitalized words]
    }
}
```

#### KeywordExtractor
Extracts important keywords from text.

**Result Structure**:
```python
{
    'analysis_type': 'keyword_extraction',
    'top_keywords': [
        {'keyword': str, 'frequency': int}
    ],
    'unique_keywords': int
}
```

---

## Data Models

### Document Class
```python
class Document:
    def __init__(self, path: str, content: str)
    def get_metadata() -> Dict[str, Any]
    def get_content() -> str
```

### AnalysisResult Class
```python
class AnalysisResult:
    def add_analysis(analysis: Dict[str, Any])
    def get_results() -> Dict[str, Any]
```

---

## Error Handling

All endpoints return standard error responses:

```json
{
  "statusCode": 400|500,
  "body": {
    "success": false,
    "error": "Error description"
  }
}
```

### Common Status Codes
- `200`: Success
- `400`: Bad Request (missing required parameters)
- `500`: Internal Server Error

---

## Usage Examples

### Document Processing Example
```python
from src.lambda.document_processor.document_processor import DocumentProcessor

processor = DocumentProcessor()
result = processor.process("documents/sample.txt")

if result['success']:
    print(f"Processed: {result['metadata']['path']}")
    print(f"Word count: {result['parsed_content'].get('word_count')}")
```

### AI Analysis Example
```python
from src.lambda.ai_analyzer.ai_analyzer import AIAnalyzer

analyzer = AIAnalyzer()
result = analyzer.analyze({
    'content': 'This is excellent work! Very positive feedback.'
})

if result['success']:
    for analysis in result['analyses']:
        if analysis['analysis_type'] == 'sentiment':
            print(f"Sentiment: {analysis['sentiment']}")
```
