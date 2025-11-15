"""Document processing module with OOP design (under src.lambdas.document_processor)."""
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any

logger = logging.getLogger(__name__)


class DocumentParser(ABC):
    """Abstract base class for document parsers."""

    @abstractmethod
    def parse(self, content: str) -> Dict[str, Any]:
        """Parse document content."""

    @abstractmethod
    def validate(self, content: str) -> bool:
        """Validate document content."""


class PDFParser(DocumentParser):
    """Parser for PDF documents."""

    def parse(self, content: str) -> Dict[str, Any]:
        logger.info("Parsing PDF document")
        return {
            'type': 'PDF',
            'content': content,
            'pages': len(content.split('\n')) // 50  # rough estimate
        }

    def validate(self, content: str) -> bool:
        return content.startswith('%PDF')


class TextParser(DocumentParser):
    """Parser for plain text documents."""

    def parse(self, content: str) -> Dict[str, Any]:
        logger.info("Parsing text document")
        words = content.split()
        return {
            'type': 'TEXT',
            'content': content,
            'word_count': len(words),
            'line_count': len(content.split('\n'))
        }

    def validate(self, content: str) -> bool:
        return len(content.strip()) > 0


class Document:
    """Represents a document with metadata."""

    def __init__(self, path: str, content: str):
        self.path = path
        self.content = content
        self.metadata = {}
        self._extract_metadata()

    def _extract_metadata(self):
        self.metadata = {
            'path': self.path,
            'size': len(self.content),
            'encoding': 'utf-8'
        }

    def get_metadata(self) -> Dict[str, Any]:
        return self.metadata

    def get_content(self) -> str:
        return self.content


class DocumentProcessor:
    """Main document processor class using OOP principles."""

    def __init__(self):
        self.parsers = {
            'pdf': PDFParser(),
            'txt': TextParser()
        }
        self.processed_documents = []

    def _get_file_extension(self, path: str) -> str:
        return path.split('.')[-1].lower()

    def _get_parser(self, file_ext: str) -> DocumentParser:
        return self.parsers.get(file_ext, self.parsers['txt'])

    def process(self, document_path: str) -> Dict[str, Any]:
        try:
            with open(document_path, 'r', encoding='utf-8') as f:
                content = f.read()

            document = Document(document_path, content)

            file_ext = self._get_file_extension(document_path)
            parser = self._get_parser(file_ext)

            if not parser.validate(content):
                logger.warning(f"Document validation failed: {document_path}")
                return {
                    'success': False,
                    'error': 'Document validation failed'
                }

            parsed_content = parser.parse(content)

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
        return self.processed_documents
