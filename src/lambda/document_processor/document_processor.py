"""Document processing module with OOP design."""
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any
import re

logger = logging.getLogger()


class DocumentParser(ABC):
    """Abstract base class for document parsers."""
    
    @abstractmethod
    def parse(self, content: str) -> Dict[str, Any]:
        """Parse document content."""
        pass
    
    @abstractmethod
    def validate(self, content: str) -> bool:
        """Validate document content."""
        pass


class PDFParser(DocumentParser):
    """Parser for PDF documents."""
    
    def parse(self, content: str) -> Dict[str, Any]:
        """Parse PDF content."""
        logger.info("Parsing PDF document")
        return {
            'type': 'PDF',
            'content': content,
            'pages': len(content.split('\n')) // 50  # rough estimate
        }
    
    def validate(self, content: str) -> bool:
        """Validate PDF content."""
        return content.startswith('%PDF')


class TextParser(DocumentParser):
    """Parser for plain text documents."""
    
    def parse(self, content: str) -> Dict[str, Any]:
        """Parse text content."""
        logger.info("Parsing text document")
        words = content.split()
        return {
            'type': 'TEXT',
            'content': content,
            'word_count': len(words),
            'line_count': len(content.split('\n'))
        }
    
    def validate(self, content: str) -> bool:
        """Validate text content."""
        return len(content.strip()) > 0


class Document:
    """Represents a document with metadata."""
    
    def __init__(self, path: str, content: str):
        """
        Initialize a document.
        
        Args:
            path: File path to the document
            content: Document content
        """
        self.path = path
        self.content = content
        self.metadata = {}
        self._extract_metadata()
    
    def _extract_metadata(self):
        """Extract basic metadata from document."""
        self.metadata = {
            'path': self.path,
            'size': len(self.content),
            'encoding': 'utf-8'
        }
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get document metadata."""
        return self.metadata
    
    def get_content(self) -> str:
        """Get document content."""
        return self.content


class DocumentProcessor:
    """Main document processor class using OOP principles."""
    
    def __init__(self):
        """Initialize the document processor."""
        self.parsers = {
            'pdf': PDFParser(),
            'txt': TextParser()
        }
        self.processed_documents = []
    
    def _get_file_extension(self, path: str) -> str:
        """Extract file extension from path."""
        return path.split('.')[-1].lower()
    
    def _get_parser(self, file_ext: str) -> DocumentParser:
        """
        Get appropriate parser for file type.
        
        Args:
            file_ext: File extension
            
        Returns:
            DocumentParser: Appropriate parser instance
        """
        return self.parsers.get(file_ext, self.parsers['txt'])
    
    def process(self, document_path: str) -> Dict[str, Any]:
        """
        Process a document.
        
        Args:
            document_path: Path to the document
            
        Returns:
            dict: Processing result
        """
        try:
            # Read document
            with open(document_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Create document object
            document = Document(document_path, content)
            
            # Get appropriate parser
            file_ext = self._get_file_extension(document_path)
            parser = self._get_parser(file_ext)
            
            # Validate document
            if not parser.validate(content):
                logger.warning(f"Document validation failed: {document_path}")
                return {
                    'success': False,
                    'error': 'Document validation failed'
                }
            
            # Parse document
            parsed_content = parser.parse(content)
            
            # Store processed document
            result = {
                'success': True,
                'metadata': document.get_metadata(),
                'parsed_content': parsed_content
            }
            
            self.processed_documents.append(result)
            logger.info(f"Successfully processed document: {document_path}")
            
            return result
            
        except FileNotFoundError:
            logger.error(f"Document not found: {document_path}")
            return {
                'success': False,
                'error': f'Document not found: {document_path}'
            }
        except Exception as e:
            logger.error(f"Error processing document: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_processed_documents(self) -> list:
        """Get list of processed documents."""
        return self.processed_documents
