"""Unit tests for AI analyzer module."""
import unittest
from src.lambdas.ai_analyzer.ai_analyzer import (
    AIAnalyzer, SentimentAnalyzer, EntityExtractor, KeywordExtractor, AnalysisResult
)


class TestSentimentAnalyzer(unittest.TestCase):
    """Test cases for SentimentAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = SentimentAnalyzer()
    
    def test_positive_sentiment(self):
        """Test positive sentiment detection."""
        content = "This is great and excellent work! Very good."
        result = self.analyzer.analyze(content)
        
        self.assertEqual(result['analysis_type'], 'sentiment')
        self.assertGreater(result['positive_indicators'], 0)
    
    def test_negative_sentiment(self):
        """Test negative sentiment detection."""
        content = "This is bad and terrible. Worst performance ever."
        result = self.analyzer.analyze(content)
        
        self.assertEqual(result['analysis_type'], 'sentiment')
        self.assertGreater(result['negative_indicators'], 0)
    
    def test_neutral_sentiment(self):
        """Test neutral sentiment detection."""
        content = "This is a document about data processing."
        result = self.analyzer.analyze(content)
        
        self.assertEqual(result['sentiment'], 'neutral')


class TestEntityExtractor(unittest.TestCase):
    """Test cases for EntityExtractor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.extractor = EntityExtractor()
    
    def test_entity_extraction(self):
        """Test entity extraction."""
        content = "John Smith works at Google. They have 123 employees."
        result = self.extractor.analyze(content)
        
        self.assertEqual(result['analysis_type'], 'entity_extraction')
        self.assertIn('unique_words', result)
        self.assertIn('total_words', result)
        self.assertIn('entities', result)
    
    def test_number_extraction(self):
        """Test number extraction."""
        content = "There are 42 apples and 99 oranges."
        result = self.extractor.analyze(content)
        
        entities = result['entities']
        self.assertIn('42', entities['numbers'])
        self.assertIn('99', entities['numbers'])


class TestKeywordExtractor(unittest.TestCase):
    """Test cases for KeywordExtractor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.extractor = KeywordExtractor()
    
    def test_keyword_extraction(self):
        """Test keyword extraction."""
        content = "Machine learning is important. Deep learning uses neural networks. Machine learning is powerful."
        result = self.extractor.analyze(content)
        
        self.assertEqual(result['analysis_type'], 'keyword_extraction')
        self.assertIn('top_keywords', result)
        self.assertGreater(result['unique_keywords'], 0)
    
    def test_stop_words_removal(self):
        """Test that stop words are removed."""
        content = "the quick brown fox jumps over the lazy dog"
        result = self.extractor.analyze(content)
        
        keywords = [k['keyword'] for k in result['top_keywords']]
        # 'the' should not be in keywords
        self.assertNotIn('the', keywords)


class TestAnalysisResult(unittest.TestCase):
    """Test cases for AnalysisResult class."""
    
    def test_analysis_result_creation(self):
        """Test analysis result object creation."""
        result = AnalysisResult()

        # Ensure the AnalysisResult exposes analysis_count and empty analyses list
        self.assertEqual(result.analysis_count, 0)
        self.assertEqual(len(result.analyses), 0)
    
    def test_add_analysis(self):
        """Test adding analysis results."""
        result = AnalysisResult()
        analysis = {'type': 'test', 'data': 'value'}
        
        result.add_analysis(analysis)
        
        self.assertEqual(len(result.analyses), 1)
        final = result.get_results()
        self.assertEqual(final['analysis_count'], 1)


class TestAIAnalyzer(unittest.TestCase):
    """Test cases for AIAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = AIAnalyzer()
    
    def test_complete_analysis(self):
        """Test complete analysis workflow."""
        document_data = {
            'content': 'This is a great document with excellent information. Machine learning is powerful.'
        }
        
        result = self.analyzer.analyze(document_data)
        
        self.assertTrue(result['success'])
        self.assertGreater(result['analysis_count'], 0)
        self.assertIn('analyses', result)
    
    def test_empty_content(self):
        """Test analysis with empty content."""
        document_data = {'content': ''}
        result = self.analyzer.analyze(document_data)
        
        self.assertFalse(result['success'])
        self.assertIn('error', result)
    
    def test_analysis_history(self):
        """Test analysis history tracking."""
        document_data = {'content': 'Test content for analysis.'}
        
        self.analyzer.analyze(document_data)
        history = self.analyzer.get_analysis_history()
        
        self.assertEqual(len(history), 1)


if __name__ == '__main__':
    unittest.main()
