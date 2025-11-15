"""Unit tests for document processor module."""
import unittest
import tempfile
import os
from src.lambdas.document_processor.document_processor import (
    DocumentProcessor, Document, TextParser, PDFParser
)


class TestDocument(unittest.TestCase):
    """Test cases for Document class."""
    
    def test_document_creation(self):
        """Test document object creation."""
        content = "This is a test document."
        doc = Document("/path/to/doc.txt", content)
        
        self.assertEqual(doc.path, "/path/to/doc.txt")
        self.assertEqual(doc.content, content)
        self.assertEqual(doc.get_content(), content)
    
    def test_document_metadata(self):
        """Test document metadata extraction."""
        content = "Test content"
        doc = Document("/path/to/doc.txt", content)
        metadata = doc.get_metadata()
        
        self.assertIn('path', metadata)
        self.assertIn('size', metadata)
        self.assertEqual(metadata['size'], len(content))


class TestTextParser(unittest.TestCase):
    """Test cases for TextParser class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = TextParser()
    
    def test_text_validation(self):
        """Test text content validation."""
        self.assertTrue(self.parser.validate("Some text content"))
        self.assertFalse(self.parser.validate(""))
        self.assertFalse(self.parser.validate("   "))
    
    def test_text_parsing(self):
        """Test text parsing."""
        content = "This is a test document with multiple words."
        result = self.parser.parse(content)
        
        self.assertEqual(result['type'], 'TEXT')
        self.assertIn('word_count', result)
        self.assertIn('line_count', result)


class TestPDFParser(unittest.TestCase):
    """Test cases for PDFParser class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = PDFParser()
    
    def test_pdf_validation(self):
        """Test PDF content validation."""
        self.assertTrue(self.parser.validate("%PDF-1.4 content"))
        self.assertFalse(self.parser.validate("Not a PDF"))


class TestDocumentProcessor(unittest.TestCase):
    """Test cases for DocumentProcessor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = DocumentProcessor()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        # Clean up temporary files
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)
    
    def test_file_extension_extraction(self):
        """Test file extension extraction."""
        ext = self.processor._get_file_extension("document.txt")
        self.assertEqual(ext, "txt")
        
        ext = self.processor._get_file_extension("document.pdf")
        self.assertEqual(ext, "pdf")
    
    def test_process_text_document(self):
        """Test processing a text document."""
        # Create temporary text file
        test_file = os.path.join(self.temp_dir, "test.txt")
        content = "This is a test document for processing."
        
        with open(test_file, 'w') as f:
            f.write(content)
        
        # Process document
        result = self.processor.process(test_file)
        
        self.assertTrue(result['success'])
        self.assertIn('metadata', result)
        self.assertIn('parsed_content', result)
    
    def test_process_nonexistent_file(self):
        """Test processing a non-existent file."""
        result = self.processor.process("/nonexistent/file.txt")
        
        self.assertFalse(result['success'])
        self.assertIn('error', result)


if __name__ == '__main__':
    unittest.main()
