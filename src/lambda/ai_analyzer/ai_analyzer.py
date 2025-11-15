"""AI analysis module with OOP design."""
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, List
from datetime import datetime

logger = logging.getLogger()


class AnalysisStrategy(ABC):
    """Abstract base class for analysis strategies."""
    
    @abstractmethod
    def analyze(self, content: str) -> Dict[str, Any]:
        """Perform analysis on content."""
        pass


class SentimentAnalyzer(AnalysisStrategy):
    """Analyzes sentiment of document text."""
    
    def analyze(self, content: str) -> Dict[str, Any]:
        """
        Perform sentiment analysis.
        
        Args:
            content: Text content to analyze
            
        Returns:
            dict: Sentiment analysis results
        """
        logger.info("Performing sentiment analysis")
        
        # Simple sentiment scoring (in production, use ML model)
        positive_words = ['good', 'great', 'excellent', 'positive', 'best']
        negative_words = ['bad', 'poor', 'worst', 'negative', 'terrible']
        
        content_lower = content.lower()
        positive_count = sum(1 for word in positive_words if word in content_lower)
        negative_count = sum(1 for word in negative_words if word in content_lower)
        
        total = positive_count + negative_count
        sentiment = 'neutral'
        
        if total > 0:
            if positive_count > negative_count:
                sentiment = 'positive'
            elif negative_count > positive_count:
                sentiment = 'negative'
        
        return {
            'analysis_type': 'sentiment',
            'sentiment': sentiment,
            'positive_indicators': positive_count,
            'negative_indicators': negative_count
        }


class EntityExtractor(AnalysisStrategy):
    """Extracts entities from document text."""
    
    def analyze(self, content: str) -> Dict[str, Any]:
        """
        Extract entities from content.
        
        Args:
            content: Text content to analyze
            
        Returns:
            dict: Extracted entities
        """
        logger.info("Extracting entities")
        
        # Simple entity extraction (in production, use NLP model)
        words = content.split()
        
        return {
            'analysis_type': 'entity_extraction',
            'unique_words': len(set(words)),
            'total_words': len(words),
            'entities': {
                'numbers': [word for word in words if word.isdigit()],
                'proper_nouns': [word for word in words if word[0].isupper()][:10]
            }
        }


class KeywordExtractor(AnalysisStrategy):
    """Extracts keywords from document text."""
    
    def analyze(self, content: str) -> Dict[str, Any]:
        """
        Extract keywords from content.
        
        Args:
            content: Text content to analyze
            
        Returns:
            dict: Extracted keywords
        """
        logger.info("Extracting keywords")
        
        # Simple keyword extraction (in production, use TF-IDF or similar)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        words = content.lower().split()
        
        keywords = [word for word in words 
                   if word not in stop_words and len(word) > 3]
        
        # Count frequency
        keyword_freq = {}
        for keyword in keywords:
            keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1
        
        # Get top keywords
        top_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        return {
            'analysis_type': 'keyword_extraction',
            'top_keywords': [{'keyword': k, 'frequency': v} for k, v in top_keywords],
            'unique_keywords': len(keyword_freq)
        }


class AnalysisResult:
    """Represents analysis results."""
    
    def __init__(self):
        """Initialize analysis result."""
        self.analyses = []
        self.timestamp = datetime.now().isoformat()
    
    def add_analysis(self, analysis: Dict[str, Any]):
        """Add analysis result."""
        self.analyses.append(analysis)
    
    def get_results(self) -> Dict[str, Any]:
        """Get all analysis results."""
        return {
            'timestamp': self.timestamp,
            'analyses': self.analyses,
            'analysis_count': len(self.analyses)
        }


class AIAnalyzer:
    """Main AI analyzer class using strategy pattern."""
    
    def __init__(self):
        """Initialize the AI analyzer."""
        self.strategies = [
            SentimentAnalyzer(),
            EntityExtractor(),
            KeywordExtractor()
        ]
        self.analysis_history = []
    
    def analyze(self, document_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform comprehensive AI analysis on document.
        
        Args:
            document_data: Document data dictionary containing 'content'
            
        Returns:
            dict: Complete analysis results
        """
        try:
            content = document_data.get('content', '')
            
            if not content:
                logger.warning("No content provided for analysis")
                return {
                    'success': False,
                    'error': 'No content provided for analysis'
                }
            
            # Create result container
            result = AnalysisResult()
            
            # Run all strategies
            for strategy in self.strategies:
                analysis = strategy.analyze(content)
                result.add_analysis(analysis)
            
            final_result = result.get_results()
            final_result['success'] = True
            
            # Store in history
            self.analysis_history.append(final_result)
            
            logger.info("Analysis completed successfully")
            return final_result
            
        except Exception as e:
            logger.error(f"Error during analysis: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_analysis_history(self) -> List[Dict[str, Any]]:
        """Get history of analyses performed."""
        return self.analysis_history
