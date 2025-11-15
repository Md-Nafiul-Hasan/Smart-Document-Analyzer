#!/usr/bin/env python3
"""Local testing script for Smart Document Analyzer."""

import sys
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.lambdas.document_processor.document_processor import DocumentProcessor
from src.lambdas.ai_analyzer.ai_analyzer import AIAnalyzer


def test_document_processor():
    """Test document processor functionality."""
    print("\n" + "="*60)
    print("Testing Document Processor")
    print("="*60)
    
    processor = DocumentProcessor()
    
    # Test with sample document
    sample_doc = Path(__file__).parent.parent / "tests/sample_documents/sample.txt"
    
    print(f"\nProcessing document: {sample_doc}")
    result = processor.process(str(sample_doc))
    
    if result['success']:
        print("✓ Document processing successful")
        print(f"  - Document size: {result['metadata']['size']} bytes")
        print(f"  - Content type: {result['parsed_content']['type']}")
        print(f"  - Word count: {result['parsed_content'].get('word_count', 'N/A')}")
        print(f"  - Line count: {result['parsed_content'].get('line_count', 'N/A')}")
    else:
        print(f"✗ Document processing failed: {result['error']}")
        return False
    
    return True


def test_ai_analyzer():
    """Test AI analyzer functionality."""
    print("\n" + "="*60)
    print("Testing AI Analyzer")
    print("="*60)
    
    analyzer = AIAnalyzer()
    
    test_content = """
    This is an excellent and great document with positive feedback.
    The analysis is performing perfectly with wonderful results.
    Machine learning provides amazing capabilities for data analysis.
    
    Numbers: 42, 100, 999
    Names: John Smith, Jane Doe
    """
    
    print("\nAnalyzing sample content...")
    result = analyzer.analyze({'content': test_content})
    
    if result['success']:
        print("✓ Analysis successful")
        print(f"  - Analysis count: {result['analysis_count']}")
        
        for analysis in result['analyses']:
            analysis_type = analysis['analysis_type']
            print(f"\n  {analysis_type.upper()}:")
            
            if analysis_type == 'sentiment':
                print(f"    - Sentiment: {analysis['sentiment']}")
                print(f"    - Positive indicators: {analysis['positive_indicators']}")
                print(f"    - Negative indicators: {analysis['negative_indicators']}")
            
            elif analysis_type == 'entity_extraction':
                print(f"    - Unique words: {analysis['unique_words']}")
                print(f"    - Total words: {analysis['total_words']}")
                print(f"    - Numbers found: {len(analysis['entities']['numbers'])}")
                print(f"    - Proper nouns: {len(analysis['entities']['proper_nouns'])}")
            
            elif analysis_type == 'keyword_extraction':
                print(f"    - Unique keywords: {analysis['unique_keywords']}")
                print(f"    - Top keywords:")
                for kw in analysis['top_keywords'][:3]:
                    print(f"      * {kw['keyword']}: {kw['frequency']}")
    else:
        print(f"✗ Analysis failed: {result['error']}")
        return False
    
    return True


def main():
    """Run all local tests."""
    print("\n" + "="*60)
    print("Smart Document Analyzer - Local Test Suite")
    print("="*60)
    
    results = []
    
    # Run tests
    results.append(("Document Processor", test_document_processor()))
    results.append(("AI Analyzer", test_ai_analyzer()))
    
    # Print summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    
    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    all_passed = all(result for _, result in results)
    
    print("="*60)
    if all_passed:
        print("All tests passed! ✓")
        return 0
    else:
        print("Some tests failed! ✗")
        return 1


if __name__ == '__main__':
    sys.exit(main())
